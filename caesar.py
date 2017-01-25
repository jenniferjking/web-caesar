def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    num_post = alphabet.index(letter.lower())
    return num_post

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha() == True:
        start_index = alphabet_position(char.lower())
        end_index = start_index + rot
        if end_index < 26:
            new_char = alphabet[end_index]
        else:
            new_char = alphabet[end_index % 26]
        if char == char.upper():
            new_char = new_char.upper()
        return new_char
    return char

def encrypt(text, rot):
    encrypted = ""
    for char in text:
        encrypted = encrypted + rotate_character(char, rot)
    return encrypted

