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
import time

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
    
    ct = 0
    for letter in letters_guessed:
        for x in secret_word:  
            if x == letter:
                ct += 1
    if ct == len(secret_word):
        return True 
    else:
        return False           
        
# =============================================================================
#         if secret_word.contains(letter)
# =============================================================================



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    underscores = []
    final = ""
    ct = 0

    for z in range(len(secret_word)):
        underscores.append("_ ")
      
    for letter in letters_guessed:
        ct = 0
        for x in secret_word:    
            if x == letter:
                underscores[ct] = x
                ct += 1
            else:
                ct += 1 
            
    for x in underscores:
        final += x
    return(final)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_left = string.ascii_lowercase

    for x in string.ascii_lowercase:
        for y in letters_guessed:
            if x == y:
                letters_left = letters_left.replace(x,'')
    return(letters_left)
    
    

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
    letters_guessed = ""
    
    warning_left = 3
    guess_left = 6
    print("Welcome to the Hangman!")
    print("I am thinking of a word", len(secret_word), "letters long!")
    print("-----------")

    p = get_guessed_word(secret_word, letters_guessed)
    

    while is_word_guessed(secret_word, letters_guessed) == False and guess_left > 0:
        print("You have", warning_left, "warnings left.")
        print("You have", guess_left, "guesses left.")
        x = get_available_letters(letters_guessed)
        print("Available letters: ", x)
        player_guess = str(input("Please guess a letter: "))
        player_guess = str.lower(player_guess)
        
        same_word = False        
        for g in letters_guessed:
            for h in player_guess:
                if g == h:
                    same_word = True
        
        letters_guessed += player_guess  
        y = get_guessed_word(secret_word, letters_guessed)
        
        w = player_guess.isalpha()
                                                          
        if y != p:        
            print("Good guess: ", y)
        elif w != True or same_word == True:
            if warning_left <= 0:
                if w != True:
                    w == True
                    print("Oops! That not a valid letter. You have no warnings left, so you lose one guess: ", y)
                    guess_left -= 1
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left, so you lose one guess ", y)
                    guess_left -= 1
                
            elif ((same_word) == True):
                warning_left -= 1
                print("Ooops! You've already guessed that letter. You have", warning_left, "warnings left. ", y)
                
                    
            else:
                warning_left -= 1
                print("Oops! That is not a valid letter. You have", warning_left, "warnings left:", y)
        else:
            print("Oops! That letter is not in my word: ", y)
            guess_left -= 1
        p = y
        
        
    if secret_word == y:
        print("You won! The word was: ", secret_word)
    else:
        print("You lost! The correct word was: ", secret_word)
    time.sleep(5.0)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_nogaps = my_word.replace(" ", "")
    possible_word = False
    
    if len(other_word) == len(my_word_nogaps):
        for i in range(len(my_word_nogaps)):
            if my_word_nogaps[i] == "_":
                pass
            elif my_word_nogaps[i] == other_word[i] and my_word_nogaps.count(my_word_nogaps[i]) == other_word.count(other_word[i]) :                
                possible_word = True
                
            else:
                possible_word = False                
                break            
        if possible_word == True:
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
    
    all_possible_words = ""
    word_list = []
    
    for word in wordlist:
            if match_with_gaps(my_word, word) == True:
                word_list.append(word)
                all_possible_words += ((str(word)) + " ") 
    if len(all_possible_words) > 40000:
        pass
    else:
        print(all_possible_words)
                                                           
                
            


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
    letters_guessed = ""
    
    warning_left = 3
    guess_left = 6
    print("Welcome to the Hangman With Hints!")
    print("I am thinking of a word", len(secret_word), "letters long!")
    print("-----------")

    p = get_guessed_word(secret_word, letters_guessed)
    
    
    while is_word_guessed(secret_word, letters_guessed) == False and guess_left > 0:
        
        show_possible_matches(p)
        print("You have", warning_left, "warnings left.")
        print("You have", guess_left, "guesses left.")
        x = get_available_letters(letters_guessed)
        print("Available letters: ", x)
        player_guess = str(input("Please guess a letter: "))
        player_guess = str.lower(player_guess)
        
        same_word = False        
        for g in letters_guessed:
            for h in player_guess:
                if g == h:
                    same_word = True
        
        letters_guessed += player_guess  
        y = get_guessed_word(secret_word, letters_guessed)
        
        w = player_guess.isalpha()
                                            
        if y != p:        
            print("Good guess: ", y)
            
        elif w != True or same_word == True:
            if warning_left <= 0:
                if w != True:
                    w == True
                    print("Oops! That not a valid letter. You have no warnings left, so you lose one guess: ", y)
                    guess_left -= 1
                else:
                    print("Oops! You've already guessed that letter. You have no warnings left, so you lose one guess ", y)
                    guess_left -= 1
                
            elif ((same_word) == True):
                warning_left -= 1
                print("Ooops! You've already guessed that letter. You have", warning_left, "warnings left. ", y)
                
                    
            else:
                warning_left -= 1
                print("Oops! That is not a valid letter. You have", warning_left, "warnings left:", y)
        else:
            print("Oops! That letter is not in my word: ", y)
            guess_left -= 1
        p = y
    if secret_word == y:
        print("!!!!!YOU WON!!!!! \n YOU ARE AMAZING ")
    else:
        print("You lost! The correct word was: ", secret_word)
    time.sleep(5.0)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
# =============================================================================
#     secret_word = choose_word(wordlist)
#     hangman(secret_word)
# =============================================================================
    

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
