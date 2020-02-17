def find_in_list(query, mainlist):
    mainlist_len = len(query)
    range_for_loop = len(mainlist)
    i=0
    while i < (range_for_loop):
        element = mainlist[i]
        if element == query:
            index = i
        i=i+1
    return index
# this should return the position of the "query" in the "mainlist"

chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

def encrypt_message(plain_msg):
# this fucnction takes "plain_msg" as an argument and print/return the encrypted message. The "plain_msg" is tranfered into "encrypted_msg" using "shifted_chars" list. Example, if plain_msg = "ng" then n => p, g => i  and hence encrypted_msg = "pi"
    encrypted_msg = ""
    character=0
    while character <len(plain_msg):
        if plain_msg[character] in chars:
            char_index = find_in_list(plain_msg[character], chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = encrypted_msg + new_char 
        character=character+1
    return encrypted_msg 
    

# decrypt_message function defined here but not called
def decrypt_message(encrypted_msg):
# this fucnction takes "encrypted_msg" as an argument and print/return the encrypted message. The "encrypted_msg" is tranfered into "decrypted_msg" using "shifted_chars" list. Example, if encrypted_msg = "pi" then p => n, i => g  and hence decrypted_msg = "ng"
    decrypted_msg = ""
    character=0
    while character<len(encrypted_msg):
        if encrypted_msg[character] in shifted_chars:
            char_index = find_in_list(encrypted_msg[character], shifted_chars)
            new_char = chars[char_index]
            decrypted_msg = decrypted_msg + new_char
        character=character+1
    return decrypted_msg
    

flag=True
while flag:
    choice = raw_input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
    if choice == 'e':
        plain_message = raw_input("Enter message to encrypt??")
        encrypt_message1=encrypt_message(plain_message)
        print encrypt_message1
    elif choice == 'd':
        encrypted_msg = raw_input("Enter message to decrypt?")
        decrypt_message1=decrypt_message(encrypted_msg)
        print decrypt_message1
    play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N)")
    if play_again == 'Y':
        continue
    elif play_again == 'N':
        break 