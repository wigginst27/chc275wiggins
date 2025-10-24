print("welcome to the palindrome detector")
palindrome = input("what word would you like to detect").strip().lower().split()
palindrome = "" . join(palindrome)
reverse = ""
for char in palindrome:
    reverse = char + reverse
if palindrome == reverse:
    print ("thats a palindrom")
else:
    print ("thats not a palindrome")