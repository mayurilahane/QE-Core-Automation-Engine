def check_anagram(word1, word2):
    # Step 1: Separate each char into a list
    list1 = list(word1)
    list2 = list(word2)
    
    # Step 2: Sort both lists alphabetically so they line up perfectly
    list1.sort()
    list2.sort()
    
    # Step 3: Check if the one list fully matches the second list
    return list1 == list2

print(check_anagram("listen", "silent")) # Returns True!

# ----------------------------------------------------------------

def check_anagram(word1, word2):
    return sorted(word1) == sorted(word2)
