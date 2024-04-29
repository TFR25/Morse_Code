from morse_code_dictionary import morse_code_dictionary
from art import art

print(art)

message_to_encode = input("What is your message? ").upper()
def create_morse_code(message):
    secret = ""
    for char in message:
        if char in morse_code_dictionary:
            secret += morse_code_dictionary[char]
        elif char == " ":
            secret += "|"
    print(secret)
    return 

create_morse_code(message=message_to_encode)





