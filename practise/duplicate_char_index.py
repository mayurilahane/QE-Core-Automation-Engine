"""Practice Problem 2: The First Unique Character
The Goal: You are given a string like "aabbcdd". 
You need to find the very first letter that does not duplicate, 
and return its exact position (index) in the string."""

# word = "aabbcdd"
def find_unique(word):
    scorecard = {}

    # first pass
    for char in word:
        if char in scorecard:
            scorecard[char] = scorecard[char] + 1
        else:
            scorecard[char] = 1
    
    for index in range(len(word)):
        current_char = word[index]

        if scorecard[current_char] == 1:
            return f"Found '{current_char}' at index {index}"
        
    return "no uniqueness"


print(find_unique("aabbccd"))