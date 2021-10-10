# SP-GCTF-2021


## Writeup for Script Kiddie

[Solve Script Download](https://github.com/RyanNgCT/SP-GCTF-2021/blob/main/ScriptKiddie/solve.py) 

**Challenge Description:**
Are you a script kiddie or a math god?

`nc c1.2021.gryphonctf.com 9007`

Connecting to the host and port, we can see the following output:

```
Welcome math god! You will be given several questions and you have 5 seconds to 
solve each question for the flag! Good luck! :P
Solve [x] ADD [y]
>
```

So based on this, we can write a script to parse the data input.
```
import socket

host = 'c1.2021.gryphonctf.com'
port = 9007

bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bot.connect((host,port))
```

The above code initiates a connection to the bot (referenced from online scripts). Thereafter, we can try to get the "equation" we want to parse

```
#for first instance only
data = bot.recv(1024)
```

The above code ignores `Welcome math god! You will be given several questions and you have 5 seconds to 
solve each question for the flag! Good luck! :P` for the first instance. Again, the number `1024` is arbitrary. Read the recv() docs for more. The initial string is in bytecode so a `utf-8` decode is necessary for operator substitution later on.

```
    #2nd line onwards, decode from bytestring and remove redunant chars
    challenge = bot.recv(1024).decode("utf-8").replace("[", "").replace("]", "")

    # tokenize words to list
    challenge_splitted = challenge.split()
```

We then proceed on to tokenize the symbols i.e. the word `Solve`, `[x]` which represents the first number, `ADD/SUBTRACT/MULTIPLY/DIVIDE` which is the operator and `[y]` which represents the second number in the equation. We also need to rid the brackets.

Thereafter, we can substitute the operator with the appropriate representation in Python (e.g. `ADD` -> `+`, `SUBTRACT` -> `-` and so on...)

```
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
```

Lastly, we re-encode the results and send it back to the server.

```
    str(result).encode('utf-8')
    bot.send(str(result).encode('utf-8'))
```

We need to place this in a loop since there is more than 1 question. So it will look something like this when put together.

```
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

    challenge_splitted = challenge.split()

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
```

Note that the code causes an exception, but I was lazy to catch that. This gave us our flag at the end (I did not record this down).


![Partial Script Image](https://github.com/RyanNgCT/SP-GCTF-2021/blob/main/misc/image.jpeg)


## Solves

![img](https://github.com/RyanNgCT/SP-GCTF-2021/blob/main/misc/Solves.png)
