#1. The Simple Loop Method 
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Usage
print(count_vowels("Hello World"))  # Output: 3


#2. The List Comprehension Method 
def count_vowels(text):
    vowels = "aeiouAEIOU"
    # Create a list of characters that are vowels
    vowel_list = [char for char in text if char in vowels]
    return len(vowel_list)

#3. The sum() and Generator Expression Method
def count_vowels(text):
    vowels = "aeiouAEIOU"
    # sum adds 1 for every True result found in the generator
    return sum(1 for char in text if char in vowels)
