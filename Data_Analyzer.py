with open("B:/Programming Projects/Pyhton/Twitter Cracker/New Version/final_data.txt","r") as file:
    for line in file:
        username,password,email,emailpass = line.strip().split(":",maxsplit=4)
        print(f"{username}:{password}:{email},{emailpass}")

