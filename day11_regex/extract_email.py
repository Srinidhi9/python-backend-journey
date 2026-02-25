import re

text = """
Contact admin at admin@example.com
Support: helpdesk@company.org
"""

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(email_pattern, text)

print("Emails Found:")
for email in emails:
    print(email)