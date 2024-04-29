from morse_code_dictionary import morse_code_dictionary
from art import art

print(art)

message_to_encode = input("What is your message? ").upper()
def create_morse_code(message):
    secret = ""
    for char in message:
        # We need to keep all .- together.
        if char in morse_code_dictionary: # Return the value that corresponds to the key in the message. Then, add a space. 
            secret += morse_code_dictionary[char] + " " # This added space will be used to split the string ensuring the .- that belong to a key stays togeter. 
    print(secret)
    return 
create_morse_code(message=message_to_encode)

message_to_decode = input("Enter code: ")
def decode_message(message):
    plain_text = ""
    message = message.split(" ")
    for code in message:
        for key, value in morse_code_dictionary.items():
            if value == code:
                plain_text += key
    print(plain_text)
    return 
 
decode_message(message=message_to_decode)










