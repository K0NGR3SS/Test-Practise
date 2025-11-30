def ip_parse(line):
    "Extract ip using token-based parsing"
    if " from " in line:
        parts = line.split()
        try:
            anchor = parts.index(" from ")
            ip = parts[anchor + 1]
            return ip.strip()
        except (ValueError, IndexError):
            return None
    return None

#Extracting ips
ips = []
with open('server_log.txt', 'r') as f:
    for line in f:
        ip = ip_parse(line)
        if ip:
            ips.append(ip)
unique_ips = set(ips)

#printing results
print (f"Total ips: {len(ips)}")
print (f"Unique IPs: {len(unique_ips)}")

#saving unique ips to unique.ips.txt
with open ('unique_ips.txt', 'w') as f:
        for ip in sorted(unique_ips):
             f.write(ip)
