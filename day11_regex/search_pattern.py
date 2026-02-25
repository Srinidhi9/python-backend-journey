import re

text = "Server started on port 8080"

pattern = r"\d+"

match = re.search(pattern, text)

if match:
    print("Found:", match.group())