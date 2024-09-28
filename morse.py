# Morse code utilities

morse_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.', 
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---', 
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---', 
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-', 
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--', 
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ' ': '/',
}

# Reverse mapping for Morse to text
morse_dict_reverse = {v: k for k, v in morse_dict.items()}


def text_to_morse(text: str) -> str:

    words = text.split()  # Split text into words
    morse_words = []

    for word in words:
        morse_word = ' '.join(morse_dict.get(char.upper(), '') for char in word if char.upper() in morse_dict)
        morse_words.append(morse_word)

    return '\n'.join(morse_words)  # Join each Morse word with a newline


def morse_to_text(morse: str) -> str:
    
    # Normalize input by replacing underscores with hyphens
    morse = morse.replace('_', '-')
    
    # Split Morse code into individual characters, treating double spaces as new words
    words = morse.split('  ')  # assume words are split by double spaces
    text_output = []
    
    for word in words:
        characters = word.split(' ')  # Split each word into characters
        text_word = []
        
        for char in characters:
            if char in morse_dict_reverse:
                text_word.append(morse_dict_reverse[char])
            else:
                text_word.append('?')  # Handle unknown Morse code

        text_output.append(''.join(text_word))  # Join characters to form the word
    
    result = ' '.join(text_output)     # Join words with a single space
    return result  


def is_morse_code(input_string: str) -> bool:
    # A simple check based on allowed Morse code characters
    return all(char in ('.', '-', ' ') for char in input_string.replace('_', '-'))



# main function (checks if it is morse or not and translates)
def morse(input_string: str) -> str:
    output = ""
    if(is_morse_code(input_string)):
        output = morse_to_text(input_string)
    else:
        output = text_to_morse(input_string)
    
    return output



## testing here

# print(text_to_morse("Hello World"), '\n')
# print(morse_to_text(".... . .-.. .-.. ---  .-- --- .-. .-.. -.."))
# print(morse("Hello World"), '\n')

