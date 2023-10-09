def split_into_sections(s):
    """
    This functions takes a string and normalizes it

    This function expects only binary strings that represents UTF-8 charecters
    The number of characters in the string has to be a multiple of 8  

    per example:

        '01100001' ('a')
        '01100010' ('b')
        '01100010 0101' ( Invalid string )
        '011000 01 01100010' => '0110000101100010' ('ab')
        ...

    """

    if type(s) != str:
        raise ValueError('The parameter needs to be a string (str)')


    if not set(s).issubset({'1', '0', ' '}):
        raise ValueError("The string needs to be a binary string, no other charecters other than '1', '0' and ' ' are permited")
    
    s = s.replace(" ", '')
    
    if ( len(s) % 8 ) != 0:
        raise ValueError("The total charecters of the string is not a multiple of 8")

    # splits the string in sections of 8 for UTF-8 processing
    return [s[i:i+8] for i in range(0, len(s), 8)]


def binary_to_decimal(binary_str):
    """
    Convert a binary string to its decimal representation.
    """
    decimal = 0
    for digit in binary_str:
        decimal = decimal * 2 + int(digit)
    return decimal

def char_to_utf8_number(char):
    utf8_encoded = char.encode('utf-8')
    return [byte for byte in utf8_encoded][0]

def binary_to_utf8(string):

    characters = split_into_sections(string)
    characters = map(lambda x: binary_to_decimal(x), characters)
    characters = map(lambda x: chr(x), characters)
    final_string = ''.join(characters)

    return final_string

def decimals_to_utf8(string):

    characters = string.split()
    characters = map(lambda x: chr(int(x)), characters)
    final_string = ''.join(characters)

    return final_string

def utf8_to_decimal(string):

    tmp = []

    for character in string:
        number = int(char_to_utf8_number(character))
        tmp.append(str(number))
    
    final_string = ' '.join(tmp)

    return final_string

def utf8_to_binary(string, with_spaces: bool = False):

    tmp = []

    for character in string:
        number = int(char_to_utf8_number(character))
        binary = bin(number)[2:].zfill(8)
        tmp.append(str(binary))
    
    if with_spaces:
        final_string = ' '.join(tmp)
    
    else:
        final_string = ''.join(tmp)

    return final_string


