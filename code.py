alphabet = "abcdefghijklmnopqrstuvwxyz"
newAlphabet = ""
newmessage = ""

message = input( "Please enter a secret message: ").lower();
key = int(input("Please enter a number to shift by: "))


if key > 26:
    key = key%26
    
if key == 0:
    newAlphabet = alphabet
else:
    if key < 0:
        key = key + 26
    p1 = alphabet[:key]
    p2 = alphabet[key:]
    newAlphabet = p2 + p1

for i in range (0, len(message)):
    index=alphabet.find(message[i])
    if index < 0:
        newmessage += message[i]
    else:
        newmessage += newAlphabet[index]


print(newmessage)
