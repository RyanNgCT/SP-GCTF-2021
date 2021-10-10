# ['7', 'S', '3', 'Z', 'Q', '8', 'Z', 'S', '8', 'Z', 'F', '6', 'Z', 'S', '6', 'Z', 'F', '9', 'Z', 'Q', '7', 'Z', 'T', '8', 'Z', 'S']

def split(word):
    return [char for char in word]


# convert each letter to its corresponding uppercase ==> ord() thing
plaintext = input("Enter plaintext: ").upper()

# tokenize letter
asc = [ord(c) for c in plaintext]
ltr = []

for each in asc:
    if each % 10 == 0:
        ltr.append(str(each)[-1])
        ltr.append("T")
    elif each % 9 == 0:
        ltr.append(str(each)[-1])
        ltr.append("N")
    elif each % 8 == 0:
        ltr.append(str(each)[-1])
        ltr.append("E")
    elif each % 7 == 0:
        ltr.append(str(each)[-1])
        ltr.append("S")
    elif each % 5 == 0:
        ltr.append(str(each)[-1])
        ltr.append("F")
    else:
        ltr.append(str(each)[-1])
        ltr.append("Z")
        if each % 6 == 0:
            ltr.append("S")
        elif each % 4 == 0:
            ltr.append("F")
        elif each % 3 == 0:
            ltr.append("T")
        elif each % 2 == 0:
            ltr.append("G")
        else:
            ltr.append("Q")

print(ltr)
