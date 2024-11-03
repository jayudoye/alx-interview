#!/usr/bin/python3
"""
Write a method that determines if a given data set represents a valid UTF-8
encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only
need to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """Checks if data is valid UTF-8"""
    # Function to check if a given integer represents a valid UTF-8 character
    def is_valid_utf8_char(byte):
        # Check if the byte is a single byte character (0xxxxxxx)
        if byte & 0b10000000 == 0:
            return True
        # Check if the byte is a leading byte of a multi-byte character
        elif byte & 0b11100000 == 0b11000000:
            return True
        elif byte & 0b11110000 == 0b11100000:
            return True
        elif byte & 0b11111000 == 0b11110000:
            return True
        else:
            return False

    # Iterate through the list of integers
    i = 0
    while i < len(data):
        # Get the first byte of the character
        byte = data[i]
        # If it's not a valid UTF-8 character, return False
        if not is_valid_utf8_char(byte):
            return False
        # If it's a multi-byte character, check if the subsequent bytes
        # are valid
        if byte & 0b11100000 == 0b11000000:
            if i + 1 >= len(data) or data[i + 1] & 0b11000000 != 0b10000000:
                return False
            i += 1
        elif byte & 0b11110000 == 0b11100000:
            if (i + 2 >= len(data) or data[i + 1] & 0b11000000 != 0b10000000 or
                    data[i + 2] & 0b11000000 != 0b10000000):
                return False
            i += 2
        elif byte & 0b11111000 == 0b11110000:
            if (i + 3 >= len(data) or data[i + 1] & 0b11000000 != 0b10000000 or
                    data[i + 2] & 0b11000000 != 0b10000000 or data[i + 3] &
                    0b11000000 != 0b10000000):
                return False
            i += 3
        i += 1

    return True
