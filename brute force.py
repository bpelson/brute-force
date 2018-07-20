alphabet = "abcdefghijklmnopqrstuvwxyz"
newalphabet = ""

def decode(secretmessage):
    for key in range(0, len(alphabet)):
        newalphabet = alphabet[key:] + alphabet[:key]

        attempt = ""

        for i in range (len(secretmessage)):
            index = alphabet.find(secretmessage[i])

            if index < 0:
                attempt += secretmessage[i]
            else:
                attempt += newalphabet[index]

        print("Key: " + str(key) + " - " + attempt)



message = input("Enter the code: ")
decode(message)
