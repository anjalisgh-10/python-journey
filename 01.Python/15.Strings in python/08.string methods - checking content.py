"""
CHECKING CONTENT (T/F)
isalpha(): All Letters?
isdigit(): All Digits?
isalnum(): AlphaNumeric Only?
isspace(): All Whitespace?
startswith() and endswith()
"""
text = "AnjaliSingh&$#"
if text.isalpha():
    print("Yes the name is good")
else:
    print("No the name is not good")