# Task: Reverse a list without using the .reverse() method or [::-1] slicing.

def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string


if __name__ == "__main__":
    s = input("Enter a string: ")
    reversed_s = reverse_string(s)
    print(f"Reversed string: {reversed_s}")