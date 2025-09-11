def caesar_cipher(text, shift, mode):
    result = ""
    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Keep non-alphabetic characters as they are
    return result

message="Go to the citadel, Answer of the riddle is: the particle"
shift_amount=3

encrypted_message = caesar_cipher(message, shift_amount, 'encode')
