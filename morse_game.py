import random
from typing import List, Tuple
from morse import morse

two_letter_words = [
    "am", "an", "as", "at", "be", "by", "do", "go", "he", "if",
    "in", "is", "it", "me", "my", "no", "of", "on", "or", "so",
    "to", "up", "us", "we"
]


three_letter_words = [
    "and", "are", "but", "for", "had", "has",
    "her", "him", "his", "how", "man", "one", "our", "out",
    "she", "the", "too", "two", "use", "was", "way", "who",
    "you", "new", "see"
]

four_letter_words = [
    "also", "been", "came", "down", "even", "find",
    "from", "give", "good", "have", "here", "just",
    "know", "like", "make", "many", "more", "much", "must",
    "next", "only", "over", "said", "same",
    "take", "than", "that", "them", "then", "they", "this",
    "time", "what", "when", "will", "with", "work", "year", "your"
]


def generate_random_word_and_answer(no_of_letters: int) -> Tuple[str, List[str]]:
    random_word, random_word_morse, option2, option3 = "", "", "", ""
    
    if no_of_letters < 1 or no_of_letters > 4:
        no_of_letters = 2
    
    match no_of_letters:
        
        case 1:
            letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            random_word = random.choice(letters)
            random_word_morse = morse(random_word)
            
            option2 = random.choice(letters)
            option3 = random.choice(letters)
            
            while option2 == random_word:
                option2 = random.choice(letters)
            while option3 == random_word or option3 == option2:
                option3 = random.choice(letters)
                
        case 2:
            random_word = random.choice(two_letter_words)
            random_word_morse = morse(random_word)
            
            option2 = random.choice(two_letter_words)
            option3 = random.choice(two_letter_words)
            
            while option2 == random_word:
                option2 = random.choice(two_letter_words)
            while option3 == random_word or option3 == option2:
                option3 = random.choice(two_letter_words)
                
        case 3:
            random_word = random.choice(three_letter_words)
            random_word_morse = morse(random_word)
            
            option2 = random.choice(three_letter_words)
            option3 = random.choice(three_letter_words)
            
            while option2 == random_word:
                option2 = random.choice(three_letter_words)
            while option3 == random_word or option3 == option2:
                option3 = random.choice(three_letter_words)
                
        case 4:
            random_word = random.choice(four_letter_words)
            random_word_morse = morse(random_word)
            
            option2 = random.choice(four_letter_words)
            option3 = random.choice(four_letter_words)
            
            while option2 == random_word:
                option2 = random.choice(four_letter_words)
            while option3 == random_word or option3 == option2:
                option3 = random.choice(four_letter_words)
    
    options = [random_word, option2, option3]
    random.shuffle(options)
    return random_word_morse, options