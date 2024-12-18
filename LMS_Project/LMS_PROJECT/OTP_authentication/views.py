import requests
from rest_framework import status
import time
import random
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

otp_storage = {}

class GenerateOTPView(APIView):
    def post(self, request):
        # Get phone number from request
        phone_number = request.data.get('phone')

        # Check if phone number is provided
        if not phone_number:
            return Response({"status": "error", "message": "Phone number is required."}, status=400)
        
        # Make sure phone number includes country code, e.g., +91 for India
        if not phone_number.startswith('+'):
            # Example for India, you can change this to dynamic based on user's location or other logic
            phone_number = '+91' + phone_number.strip()

        # Generate OTP
        otp = random.randint(100000, 999999)

        # 2Factor API URL
        # url = f"https://2factor.in/API/V1/{settings.TWOFACTOR_API_KEY}/SMS/OTP"
        template_name = 'OTP_Template'

        url = f"https://2factor.in/API/V1/{settings.TWOFACTOR_API_KEY}/SMS/{phone_number}/{otp}/{template_name}"


        # Prepare payload
        payload = {
            'From': 'TXTLCL',  # Sender ID
            'To': phone_number,  # Recipient's phone number
            'TemplateName': 'OTP_Template',  # Template (if needed)
            'OTP': otp  # Generated OTP
        }

        # Send OTP request via 2Factor API
        response = requests.post(url, data=payload)

        if response.status_code == 200:
            data = response.json()
            if data['Status'] == 'Success':
                otp_storage[phone_number] = {'otp': otp, 'timestamp': time.time()}
                print(phone_number,otp)
                return Response({"status": "success", "message": "OTP sent successfully."}, status=200)
            else:
                return Response({"status": "error", "message": data['Message']}, status=400)
        else:
            return Response({"status": "error", "message": response.text}, status=400)


class VerifyOTPView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone')
        entered_otp = request.data.get('otp')

        if phone_number in otp_storage:
            stored_data = otp_storage[phone_number]
            stored_otp = stored_data['otp']

            # Verify OTP
            if entered_otp == str(stored_otp):
                return Response({"status": "success", "message": "OTP verified successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "message": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"status": "error", "message": "No OTP generated for this phone number."}, status=status.HTTP_400_BAD_REQUEST)