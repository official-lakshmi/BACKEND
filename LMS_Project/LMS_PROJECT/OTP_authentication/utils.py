import requests
from django.conf import settings
import random
import time


def generate_otp(phone_number):
    # Generate a 6-digit OTP
    otp = random.randint(100000, 999999)
    
    # Send OTP to the phone number via 2Factor API
    url = f"https://2factor.in/API/V1/{settings.TWOFACTOR_API_KEY}/SMS/OTP"
    payload = {
        'To': phone_number,
        'TemplateName': 'OTP_Template',
        'OTP': otp
    }
    
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        data = response.json()
        if data['Status'] == 'Success':
            # Store OTP and expiration time in the session or a database
            return otp
        else:
            raise Exception(f"Failed to send OTP: {data['Message']}")
    else:
        raise Exception(f"Error sending OTP: {response.text}")


def verify_otp(phone_number, entered_otp, original_otp):
    if entered_otp == str(original_otp):
        return True
    return False
