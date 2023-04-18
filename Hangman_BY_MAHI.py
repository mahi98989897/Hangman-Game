import random
words = ['python', 'rabbit', 'home', 'dog', 'elephant', 'beer', 'cow', 'boy', 'morning', 'java','javascript', 'chocolate', 'tiger', 'night', 'dark', 'whitebeer', 'mouse', 'eye', 'pankaj', 'abhishek', 'mahendra', 'money', 'sky', 'balloon', 'car', 'moon', 'sun','cat', 'hanuman', 'hangman']
word =  random.choice(words)
attempts = 0
guess_letters = []
masked_word = ['_'] * len(word)
hangman_body_parts = ['|--------------------_|_---', '☻', '/|\\', '/ \\']
while True:
    #Hangman.
    print('                                     |`,')
    print('                                     '+hangman_body_parts[0] if attempts>0 else '')
    print('                                     |                     '+hangman_body_parts[1] if attempts>1 else '')
    print("                                     |	                  "+hangman_body_parts[2] if attempts>2 else '')
    print("                                     |	                  "+hangman_body_parts[3] if attempts>3 else '')
    print('                              _______|________')
    print('                        ______|_______________|______')
    print('                  ______|__________________________ _|______')
    print('                 |__________________________________________|')
    print(' '.join(masked_word))
    print('First letter:-',word[0])
    guess = input('Enter your guess:-').lower()
    if len(guess)==1 and guess.isalpha() and guess not in guess_letters:
        guess_letters.append(guess)
        if guess in word:
                    # Update the masked word to reveal the guessed letter
                    for i in range(len(word)):
                        if word[i] == guess:
                            masked_word[i] = guess

                    # Check if the user has guessed the whole word
                    if "_" not in masked_word:
                        print("Congratulations! You guessed the word.")
                        print('The word is:-',word)
                        break
        else :
            attempts = attempts+1
            print('Wrong letter guess Again!')
            print('attempts:-',attempts)
            if attempts==5:
                break
    else:
        attempts = attempts+1
        print('Wrong letter guess Again!')
        print('attempts:-',attempts)
        if attempts==4:
             print('Last chance!')
        elif attempts==5:
             break
if attempts==4:
     print('Last chance!')
elif attempts==5:
     print('Sorry you lose!')
     print('The word is:-',word)
      
    
       
        
