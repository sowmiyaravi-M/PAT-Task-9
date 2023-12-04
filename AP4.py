# Function to validate Regular Expression 
import re

def validate_email(email):
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) is not None

def validate_bangladesh_mobile_number(mobile_number):
    return re.match(r'^\+8801[3-9]\d{8}$', mobile_number) is not None

def validate_USA_telephone_number(telephone_number):
    return re.match(r'^\+1-\d{10}$', telephone_number) is not None

def validate_alpha_numeric_password(password):
    return re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$', password) is not None

email = "example@email.com"
mobile_number = "+8801712345678"
telephone_number = "+1-1234567890"
password = "Abcdef123!@#$5678"

print(f"Email is valid: {validate_email(email)}")
print(f"Bangladesh mobile number is valid: {validate_bangladesh_mobile_number(mobile_number)}")
print(f"USA telephone number is valid: {validate_USA_telephone_number(telephone_number)}")
print(f"Alpha numeric password is valid: {validate_alpha_numeric_password(password)}")
