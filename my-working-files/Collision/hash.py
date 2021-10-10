password = "xxxxxxxxxx"


def hash(password):
    output = 0
    # loop thru dict
    for index,i in enumerate(password):
        #XOR output with ord of key(?)
        output += output ^ ord(i)
    return output
        
hashed = hash(password)

with open('hashed.txt','w') as file:
    file.write(str(hashed))
