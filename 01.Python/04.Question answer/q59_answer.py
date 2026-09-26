"""
String Characters and length

Take a name as input from the user. Print its first character, its last character,
and the total length of the name.

"""
def print_details(name):
    first=name[0]
    last = name[-1]
    n = len(name)
    print(f"First = {first}, last = {last} and length = {n}")

print_details("Anjali Singh is a coder")