# MIT-HangmanGame
Hello, I made this project/game as an assignment to learn and understand the fundamentals of programming. 
I took the 'Introduction to Computer Science and Programming in Python' class from MIT Open Courseware. 
This project/game is an assignment from that class.

The Game Explanation:

It is a hangman game

1- The game is going to generate a random word and it is going print something like --> I am thinking of a word 9 letters long!
2- You will have 3 warnings and 6 guesses at the beginning of the game.
3- Available letters will be written every round. 
4- If you try to make a guess of a same letter twice you will lose one warning right so it will be 2 if it was 3 for example.
5- If you have 0 warnings left and you guess of a same letter again, you will lose from your guess right.
6- If you find a letter the letter you find will be displayed. Example: the secret word is apple --> _ _ _ _ _ --> If you make a guess of the letter 'p' --> _ p p _ _

Bonus: You can play the game in two versions --> With hints or without hints. You can open the file named Hangman_With_Hints to play with hints, open the file named Hangman_Without_Hints to play without hints.

If you play the game with hints it is going to print out all the possible words when you find a letter.

Here is a Game Example Without Hints:

Loading word list from file...
   55900 words loaded.
Welcome to the Hangman!
I am thinking of a word 5 letters long!
-----------
You have 3 warnings left.
You have 6 guesses left.
Available letters:  abcdefghijklmnopqrstuvwxyz

Please guess a letter: a
Good guess:  _ a_ _ _ 
You have 3 warnings left.
You have 6 guesses left.
Available letters:  bcdefghijklmnopqrstuvwxyz

Please guess a letter: 
Oops! That is not a valid letter. You have 2 warnings left: _ a_ _ _ 
You have 2 warnings left.
You have 6 guesses left.
Available letters:  bcdefghijklmnopqrstuvwxyz

Please guess a letter: s
Oops! That letter is not in my word:  _ a_ _ _ 
You have 2 warnings left.
You have 5 guesses left.
Available letters:  bcdefghijklmnopqrtuvwxyz

Please guess a letter: e
Good guess:  ea_ e_ 
You have 2 warnings left.
You have 5 guesses left.
Available letters:  bcdfghijklmnopqrtuvwxyz

Please guess a letter: g
Good guess:  eage_ 
You have 2 warnings left.
You have 5 guesses left.
Available letters:  bcdfhijklmnopqrtuvwxyz

Please guess a letter: r
Good guess:  eager
You won! The word was:  eager
