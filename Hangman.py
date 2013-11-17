def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
 
    Starts up an interactive game of Hangman.
 
    * At the start of the game, let the user know how many
      letters the secretWord contains.
 
    * Ask the user to supply one guess (i.e. letter) per round.
 
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
 
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
 
    Follows the other limitations detailed in the problem write-up.
    '''
    nguesses=8
    print('Welcome to the game Hangman!')
    nletters=len(secretWord)
    print('I am thinking of a word that is '+str(nletters)+ ' letters long.')
    print('-------------')
    lettersGuessed=[]
 
    while nguesses>0:
        print('You have '+str(nguesses)+ ' guesses left')
        print('Available Letters: '+ str(getAvailableLetters(lettersGuessed)))
        guess=str(raw_input('Please guess a letter: '))
        guessLowerCase=guess.lower()
 
       
        if guessLowerCase not in lettersGuessed:
                lettersGuessed.append(guessLowerCase)
               
                if guessLowerCase in secretWord:
                    print('Good guess: ' +str(getGuessedWord(secretWord, lettersGuessed)))
                else:
                    print('Oops! That letter is not in my word: ' +str(getGuessedWord(secretWord, lettersGuessed)))
                    nguesses-=1
        else:
            print('Oops! You'+"'"+'ve already guessed that letter: '+str(getGuessedWord(secretWord, lettersGuessed)))
           
        print('-------------')
   
        if isWordGuessed(secretWord, lettersGuessed)==True:
            print('Congratulations, you won!')
            return None
       
    if isWordGuessed(secretWord, lettersGuessed)==False:
        print(('Sorry, you ran out of guesses. The word was '+str(secretWord)+'.'))
        return None
