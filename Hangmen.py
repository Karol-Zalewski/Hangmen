
# import the json library to open the file with the words to chose from
import json

# import the random library to chose the random word from the list
import random

# import the string to later import the list of the letters in the english alphabet
import string

def get_valid_word():

    # Read the json file with the list of the words
    with open ('words.json', "r", encoding= "UTF-8") as file:
        data = json.load(file)
        list_of_words = []

        for word in data['data']:

            # add the words in data to the list
            list_of_words.append(word)
    
    # chose one word from the list
    chosen_word = random.choice(list_of_words)

    # if chosen word has empty spaces or - in it chose again
    while '-' in chosen_word or ' ' in chosen_word:
        chosen_word = random.choice(list_of_words)
    return(chosen_word.upper())

def hangman(number_of_fails):
    word_to_guess = get_valid_word()

    # create a list containing all of the letters in the chosen word
    letters = list(word_to_guess)

    # import the list of upper case letters in the english dictionary
    alphabet = set(string.ascii_uppercase)

    # create the sets to keep track of the letters used and guessed right
    used_letters = set()
    unknown_letters = []
    letters_guessed_right = []

    # count to keep a track over the wrong guesses
    count = 0

    for letter in letters:
        unknown_letters.append('_')
    
    # give the user the number of letters
    print(f'The world to guess contains {len(letters)} letters: {unknown_letters} ')

    while count < number_of_fails and len(letters_guessed_right) != len (letters):

        # ask the user to give a letter and save it
        print(f'Possible number of mistakes: {number_of_fails - count}\
              Used letters: {used_letters}')
        user_letter = input('Guess a letter: ').upper()

        # if the letter already has been used ask again
        while user_letter in used_letters:
            print ("You have already chosen that letter. ")
            user_letter = input('Try again: ').upper()
        
        # check if the letter belongs to the english alphabet, it also doesn't allow for words
        while user_letter not in alphabet:
            print ("Only a single letters belonging to the english alphabet are allowed. ")
            user_letter = input('Try again: ').upper()
    
        # if guessed right add the letter to the used_letters and letters guessed right
        if user_letter in letters:
            print('Gratulation you guessed right! ')
            used_letters.add(user_letter)

            # since the letters in the word can show up more than once there is the need to check every letter and
            # add the right number of letters to the list
            for letter in letters:
                if letter == user_letter:
                    letters_guessed_right.append(user_letter)

        # if guessed wrong add the letter to the used_letters and increase the count
        else:
            print('Unfortunately you guessed wrong! ')
            used_letters.add(user_letter)
            count += 1

        # by going through all the letters used and letters in the word print all of the letters and _ (spaces for letters)
        unknown_letters = []
        for letter in letters:
            if letter in used_letters:
                unknown_letters.append(letter)
            else:
                unknown_letters.append('_')
        print (unknown_letters)

        # if the count riches the number of possible fails the game ends with the 
        # lost if the length of the letters to guess is equal to the number of guest letters
        if count == number_of_fails:
            print ('You have lost the game! ')
            print (f'The word: {word_to_guess}')
        elif len(letters_guessed_right) == len(letters):
            print ('You have won the game! ')
            print (f'The word: {word_to_guess}')


if __name__ == "__main__":
    hangman(100)