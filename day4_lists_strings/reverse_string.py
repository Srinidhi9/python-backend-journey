text = input("Enter string: ")

reversed_text = ""

for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

print("Reversed:", reversed_text)