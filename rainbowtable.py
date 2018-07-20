import hashlib
rainbow_table = {}
stolen_data = {}

def hasher(password):
    b = bytes(password, 'utf-8')
    m = hashlib.sha256(b)
    m = m.hexdigest()
    return m

def make_RT():
    file = open("top_passwords.txt", "r")
    for password in file:
        hashed = hasher(password.strip('\n'))
        rainbow_table[hashed] = password.strip('\n')
    file.close

def get_stolen_data():
    file = open("accounts.txt", "r")
    for accounts in file:
        words = accounts.split(" ")
        hashed = words[1]
        username = words[0]
        stolen_data[hashed] = username
    file.close()

def crack_password():
    file = open("cracked_password.txt", "a+")
    for hpass in rainbow_table:
        if stolen_data.get(hpass):
            file.write("username: " + stolen_data[hpass])
            file.write("password: " + rainbow_table[hpass])
            file.write('\n')
    file.close()

make_RT()
get_stolen_data()
crack_password()
