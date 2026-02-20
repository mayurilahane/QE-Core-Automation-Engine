# Task: Write a function to check if a string is a palindrome.

def palindrome_validation(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    s = input("Enter a string: ")
    if palindrome_validation(s):
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")
