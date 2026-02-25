import re

with open("sample_log.txt", "r") as file:
    data = file.read()

ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

ips = re.findall(ip_pattern, data)

print("IP Addresses Found:")
for ip in ips:
    print(ip)