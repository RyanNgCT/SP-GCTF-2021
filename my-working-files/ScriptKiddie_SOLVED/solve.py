#!/usr/bin/python2.7
import socket

host = 'c1.2021.gryphonctf.com'
port = 9007

bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bot.connect((host,port))

#for first instance only
data = bot.recv(1024)

while True:
    #2nd line onwards, decode from bytestring and remove redunant chars
    challenge = bot.recv(1024).decode("utf-8").replace("[", "").replace("]", "")

    # tokenize words to list
    if challenge != []:
        challenge_splitted = challenge.split()
    #print(challenge_splitted)
    else:
        break

    # initalize variable 
    result = 0

    #substitutions
    if (challenge_splitted[2] == "DIVIDE"):
        result = int(challenge_splitted[1]) / int(challenge_splitted[3])
    elif (challenge_splitted[2] == "ADD"):
        result = int(challenge_splitted[1]) + int(challenge_splitted[3])
    elif (challenge_splitted[2] == "SUBTRACT"):
        result = int(challenge_splitted[1]) - int(challenge_splitted[3])
    elif (challenge_splitted[2] == "MULTIPLY"):
        result = int(challenge_splitted[1]) * int(challenge_splitted[3])
    else:
        print("Invalid operation")

    str(result).encode('utf-8')


    bot.send(str(result).encode('utf-8'))

    #receive congrats message
    print(bot.recv(1024))

