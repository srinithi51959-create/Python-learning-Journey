
number = 121
original = str(number)
reverse = ""

for digit in original:
    reverse = digit + reverse

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
