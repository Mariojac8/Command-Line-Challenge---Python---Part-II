import base64

print("Immaculata Soccer Secret Message Decoder")

secret_message = "R28gTWlnaHR5IE1hY3Mh"

decoded_message = base64.b64decode(secret_message).decode("utf-8")

print("Encoded message:", secret_message)
print("Decoded message:", decoded_message)
