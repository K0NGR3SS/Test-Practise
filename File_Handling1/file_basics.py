#read and print with line numbers
with open('practice_log.txt', 'r') as f:
    line_num = 1
    for line in f:
        print(f"{line_num}: {line.strip()}")
        line_num += 1

#write filtered lines and display
with open('practice_log.txt', 'r') as infile:
    with open('successful_logins.txt', 'w') as outfile:
        for line in infile:
            if "logged in" in line:
                outfile.write(line)
                print(line.strip())