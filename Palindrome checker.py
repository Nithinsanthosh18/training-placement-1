def is_palindrome(string):
    return string == string[::-1]

word = input("Enter a word: ").lower()
if is_palindrome(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")
