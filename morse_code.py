from morse_code_dictionary import morse_code_dictionary
from art import art

print(art)

def create_morse_code(message):
    '''
    This function converts plain text to morse code.
    The Morse code is a sequence of dots and dashes (.-) that corresponds to the letters or characters held in the 
    Morse code dictionary (morse_code_dictionary).
    To keep all the (.-)'s together, a space is added after each value of the key-value pair from the dictionary.
    This added space will be used to split the string when decoding a messge ensuring the (.-)'s that belong to a key stays togeter.
    '''
    secret = ""
    for char in message: 
        if char in morse_code_dictionary: 
            secret += morse_code_dictionary[char] + " " 
    print(secret)
    return 

def decode_message(message):
    plain_text = ""
    message = message.split(" ")
    for code in message:
        for key, value in morse_code_dictionary.items():
            if value != code:
                print("Invalid code. Try again.")
                break
            else:
                plain_text += key
    print(plain_text)
    return 

def main():
    ''' 
    Here a user is given a choice to encode, decode or exit the application.
    The users choice is then used to run the appropriacte functions or to quit the application.
    '''
    while True:
        create_message = input("To create coded message press 1. To decode a message press 2. To Quit press q: ")
        if create_message == "1":
            message_to_encode = input("What is your message? ").upper()
            create_morse_code(message=message_to_encode)
        elif create_message == "2":
            message_to_decode = input("Enter code: ")
            decode_message(message=message_to_decode)
        elif create_message == 'q':
            print("Goodbye")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()












