f = open("yesterday.txt", 'r')
yesterday_lyric = ""
while True:
    line = f.readline()
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"
f.close()
n_of_Yesterday = yesterday_lyric.count("Yesterday") 
n_of_yesterday = yesterday_lyric.count("yesterday") 
print("Number of a Word 'Yesterday'", n_of_Yesterday)
print("Number of a Word 'yesterday'", n_of_yesterday)