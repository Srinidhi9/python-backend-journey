import re

log = """
Server running on port 8080
Database started at port 3306
Proxy listening on port 443
"""

port_pattern = r"\b\d{2,5}\b"

ports = re.findall(port_pattern, log)

print("Ports Found:")
for port in ports:
    print(port)