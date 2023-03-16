# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    magic_letters = list(secret_word)
    for char in magic_letters:
      if char not in letters_guessed:
        return False
    return True
 
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    guessed = []
    for char in secret_word:
      if char in letters_guessed:
        guessed.append(char)
      else:
        guessed.append("_ ")
    guessed = ''.join(guessed)
    return guessed

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = list(string.ascii_lowercase)
    for char in letters_guessed:
      if char in available_letters:
        available_letters.remove(char)
      else:
        continue
    available_letters = ''.join(available_letters)
    return available_letters

def get_unique_letters(secret_word):
    '''
    secret_word: string, the secret word to guess.
    returns: int number of unique letters
    check how many unique letters is in word to guess
    '''
    unique_letters = []
    for letter in secret_word:
      if letter in unique_letters:
        continue
      else:
        unique_letters.append(letter)
    return len(unique_letters)
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    warnings_remaining = 3
    guesses_left = 6
    print("Welcome to the game Hangman !")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("You have", warnings_remaining, "warnings left.")
    while guesses_left > 0:
      message = ""
      print("-------------")
      print("You have", guesses_left, "guesses left.")
      print("Available letters: " + get_available_letters(letters_guessed))
      guess = input("Please guess a letter:").lower()
      if len(guess) == 1 and str.isalpha(guess) == True:
        if guess in letters_guessed:
          message = "Oops! You've already guessed that letter. "
          if warnings_remaining > 0:
            warnings_remaining -= 1
            message += "You have " + str(warnings_remaining) + " warnings left"
          else:
            message += "You have no warnings left so you lose one guess:"
            guesses_left -= 1
        else:
          letters_guessed.append(guess)
          if guess in secret_word:
            message ="Good guess: "
          else:
            message = "Oops! That letter is not in my word: "
            if guess in ["a", "e", "i", "o", "u"]:
              guesses_left -= 2
            else:
              guesses_left -= 1
      else:
        if warnings_remaining > 0:
          warnings_remaining -= 1
          message = "Oops! That is not a valid letter. You have " + str(warnings_remaining) + " warnings left:"
        else:
          message = "Oops! That is not a valid letter. "
          message += "You have no warnings left so you lose one guess:"
          guesses_left -= 1
      print( message + get_guessed_word(secret_word, letters_guessed))
      if (is_word_guessed(secret_word, letters_guessed) == True):
        print("-------------")
        print("Congratulation, you won!")
        total_score = guesses_left * get_unique_letters(secret_word)
        print("Your total score for this game is:", total_score)
        break
    if (guesses_left <= 0):
      print("-----------")
      print("You run out of guesses and lost. The word was " + secret_word)
      
      
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------
letters_guessed = []

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
      return False
    i = 0
    for letter in my_word:
      if letter != "_":
        if letter != other_word[i]:
          return False
      else:
        if other_word[i] in my_word:
          return False
      i += 1
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = []
    my_word = my_word.replace(" ", "")
    for word in wordlist:
      if match_with_gaps(my_word, word) == True:
        possible_matches.append(word)
    if len(possible_matches) == 0:
      print("No matches found")
    else:
      print(' '.join(possible_matches))


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    warnings_remaining = 3
    guesses_left = 6
    print("Welcome to the game Hangman !")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("You have", warnings_remaining, "warnings left.")
    while guesses_left > 0:
      message = ""
      print("-------------")
      print("You have", guesses_left, "guesses left.")
      print("Available letters: " + get_available_letters(letters_guessed))
      guess = input("Please guess a letter:").lower()
      if len(guess) == 1 and str.isalpha(guess) == True:
        if guess in letters_guessed:
          message = "Oops! You've already guessed that letter. "
          if warnings_remaining > 0:
            warnings_remaining -= 1
            message += "You have " + str(warnings_remaining) + " warnings left"
          else:
            message += "You have no warnings left so you lose one guess:"
            guesses_left -= 1
        else:
          letters_guessed.append(guess)
          if guess in secret_word:
            message ="Good guess: "
          else:
            message = "Oops! That letter is not in my word: "
            if guess in ["a", "e", "i", "o", "u"]:
              guesses_left -= 2
            else:
              guesses_left -= 1
      elif guess == "*":
        print("Possible word matches are:")
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
      else:
        if warnings_remaining > 0:
          warnings_remaining -= 1
          message = "Oops! That is not a valid letter. You have " + str(warnings_remaining) + " warnings left:"
        else:
          message = "Oops! That is not a valid letter. "
          message += "You have no warnings left so you lose one guess:"
          guesses_left -= 1
      print( message + get_guessed_word(secret_word, letters_guessed))
      if (is_word_guessed(secret_word, letters_guessed) == True):
        print("-------------")
        print("Congratulation, you won!")
        total_score = guesses_left * get_unique_letters(secret_word)
        print("Your total score for this game is:", total_score)
        break
    if (guesses_left <= 0):
      print("-----------")
      print("You run out of guesses and lost. The word was " + secret_word)
      


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
