# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word_1 = input()
word_2 = input()
if (sorted(word_1) == sorted(word_2)):
        print("True")
else:
        print("False")

