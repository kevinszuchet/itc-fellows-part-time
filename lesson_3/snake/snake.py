"""Program that tries to beat the cyber monster."""

from monster import substitution_cipher_dict, ciphered_message


def decipher_message(monster_message, decipher_dict):
    """
    Given a ciphered message and a dictionary to decode characters,
    it resolves the monster puzzle and returns the deciphered message.
    """
    message = ""
    word = ""
    for monster_char in monster_message:
        if monster_char.isdigit():
            # Is a space -> Let's add the deciphered word to the message.
            message += " " + word if message else word
            # Clean the word before deciphered the next one.
            word = ""
            continue

        # Get the real character deciphering it from the monster dictionary.
        # If the char isn't in the dict, use the value of the char itself.
        char = decipher_dict.get(monster_char, monster_char)
        # Add the char at the beginning of the word to get the original word back.
        word = char + word

    # The last word isn't following by a space (a digit speaking like the monster), so I need to append the last word.
    if word:
        message += word

    return message


def main():
    """Main function. It calls the deciphered function."""
    decipher_dict = {value: key for key, value in substitution_cipher_dict.items()}
    message = decipher_message(ciphered_message, decipher_dict)
    print(message)


if __name__ == "__main__":
    main()
