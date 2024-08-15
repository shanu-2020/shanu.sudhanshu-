import random

# Define categories and word lists
word_categories = {
    'Animals': ['elephant', 'tiger', 'zebra', 'giraffe'],
    'Countries': ['canada', 'brazil', 'india', 'germany'],
    'Movies': ['inception', 'titanic', 'gladiator', 'avatar']
}

# ASCII art for hangman graphics
hangman_graphics = [
    '''
       ------
       |    |
       |
       |
       |
       |
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |
       |
       |
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    '''
]

def choose_category():
    print("Choose a category:")
    for i, category in enumerate(word_categories.keys(), 1):
        print(f"{i}. {category}")
    choice = int(input("Enter the number of your choice: ")) - 1
    return list(word_categories.keys())[choice]

def choose_word(category):
    return random.choice(word_categories[category])

def display_hangman(tries):
    print(hangman_graphics[tries])

def play_game():
    category = choose_category()
    word = choose_word(category)
    word_letters = set(word)
    guessed_letters = set()
    correct_letters = set()
    tries = 0
    max_tries = 6

    print(f"\nCategory: {category}")

    while tries < max_tries and correct_letters != word_letters:
        display_hangman(tries)
        print(f"Word: {' '.join([letter if letter in guessed_letters else '_' for letter in word])}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Remaining tries: {max_tries - tries}")
        
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        if guess in word_letters:
            correct_letters.add(guess)
        else:
            tries += 1

    if correct_letters == word_letters:
        print(f"Congratulations! You guessed the word '{word}'.")
    else:
        display_hangman(tries)
        print(f"Sorry, you lost. The word was '{word}'.")

def main():
    play_game()

if __name__ == "__main__":
    main