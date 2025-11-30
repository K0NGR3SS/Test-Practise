from collections import defaultdict

def ip_parse(line):
    if "from " in line:
        parts = line.split()
        try:
            anchor = parts.index("from")
            return parts[anchor + 1].strip()
        except (ValueError, IndexError):
            return None
        return None
#Count failures of ips
counts = defaultdict(int)
with open ('server_log.txt', 'r') as f:
    for line in f:
        if "Failed password" in line:
            ip = ip_parse(line)
            if ip:
                counts[ip] += 1
#print all counts
print("Failed login attempts per ip")
for ip, count in counts.items():
    print(f"{ip}: {count}")

#top3
def top_n(counts, n=3):
    return sorted(counts.items(), key=lambda kv: kv[1], reverse= True)[:n]

print ("Top 3 attackers: ")
for rank, (ip,count) in enumerate(top_n(counts, 3), 1):
    print (f"{rank}. {ip} - {count}")