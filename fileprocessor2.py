#!/usr/bin/python3
import sys

print("Printing out User Data:\n")

for line in sys.stdin:
    line = line.strip()
    if not line.startswith('#'):
        user_data = line.split(':')
        print(f"The user {user_data[0]} has a password of {user_data[1]} and has userid {user_data[2]} and groupid {user_data[3]}")
    else:
        print(f"{line.lstrip('#').split(':')[0]} is skipped because it starts with a hashtag (is commented out)\n")

print("End of User Data")
