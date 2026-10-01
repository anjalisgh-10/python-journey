"""
Clean Phone Number

Take a phone number as input in the formae +91-98765-43210. 
Remove all dashes and the country code.
Print the cleaned 10-digit number.
"""
def clean_number(phone_number: str):
    phone_number = phone_number.replace("-","")
    phone_number = phone_number.replace("+","")
    print(phone_number)

phone = "+91-98765-43210"
clean_number(phone)