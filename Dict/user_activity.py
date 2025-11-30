from collections import defaultdict

total_actions = defaultdict(int)
login_counts = defaultdict(int)

with open ('activity_log.txt', 'r') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 2:
            user = parts[0]
            action = parts[1]

            total_actions[user] += 1
            if action == "login":
                login_counts[user] += 1

# Print results
print("User Activity Summary:")
for user in total_actions:
    print(f"{user}: {total_actions[user]} actions, {login_counts[user]} logins")

    with open ('user_stats.txt', 'w') as f:
        f.write("username, total_actions, login_count\n")
        for user in sorted(total_actions.keys()):
            f.write(f"{user}, {total_actions[user]},{login_counts[user]}\n")