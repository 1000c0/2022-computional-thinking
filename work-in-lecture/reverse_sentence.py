import re


sentence = "I love you"
reverse_sen = ""

for char in sentence:
    print("REVERSE #1", reverse_sen)
    reverse_sen = char + reverse_sen
    print("REVERSE #2", reverse_sen)
