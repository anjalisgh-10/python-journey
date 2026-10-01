"""
Email Validation

Take an email as input. Validate that it contains exactly exactly one @ and at 
least one.
Print "valid" or "Invalid".
"""
def check_email(email:str):
    if email.count("@") == 1 and "." in email:
        return "Valid"
    return"Invalid"

email = "info@code.and.debug.in"
print(check_email(email))