password = '\0sdfs)+}@%'

def encode_password(password):
    unicode_pass = [ord(x) - 1 if ord(x) > 0 else ord(x) for x in password]
    encrypt_pass = ''.join(chr(x) for x in unicode_pass)
    return encrypt_pass
        
def decode_password(encrypted_password):
    unicode_pass = [ord(x) + 1 if ord(x) > 0 else ord(x) for x in encrypted_password]
    decrypt_pass = ''.join(chr(x) for x in unicode_pass)
    return decrypt_pass

def main():
    encrypted_pass = encode_password(password)
    decrypted_pass = decode_password(encrypted_pass)
    print("Pawword is " + password)
    print("Encrypted pass is " + encrypted_pass)
    print("Decrypted pass is " + decrypted_pass)

    if password == decrypted_pass:
        print("password matched")

if __name__ == '__main__':
    main()
