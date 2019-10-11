# Program to convert a normal word into gibberish

# variable for the outer while loop
menu = True

# list of vowels to check for in the word given by the user
vowels = "aeiouAEIOU"

# outer while loop for restarting/ending the game
while menu:

    # Explaining the program
    print("The program will ask for 2 syllables and a word.")
    print("The program will then insert the syllables into the word, placing the first syllable")
    print("before the first vowel, and the second syllable before the any other vowel.")
    print("If you enter a * in the syllable it will use the vowel as part of the syllable.")
    print("* can only appear at the begging of the syllable")
    print("")

    # asking the user to input the Gibberish and the word to translate
    syl1 = input("Enter your first Gibberish syllable: ")
    syl2 = input("Enter your second Gibberish syllable: ")
    word = input("Enter the word you would like to translate: ")
    print("")

    # initialising a blank variable for the new word
    gibberish_word = ""
    # bool to track whether the first syllable has been used
    syl1_used = False

    # for loop add the gibberish syllables to the word
    for i in word:
        if i in vowels:
            if not syl1_used:
                if '*' not in syl1:
                    gibberish_word = gibberish_word + syl1 + i
                    syl1_used = True
                else:
                    syl1 = i + syl1[1::]
                    gibberish_word = gibberish_word + syl1 + i
                    syl1_used = True
            else:
                if '*' not in syl2:
                    gibberish_word = gibberish_word + syl2 + i
                else:
                    syl2 = i + syl2[1::]
                    gibberish_word = gibberish_word + syl2 + i
        else:
            gibberish_word += i

    # printing the new word
    print("The Word in Gibberish is: ", gibberish_word)

    # asking the user if they would like to play the game again
    var_invalid = True
    while var_invalid:
        var = input("Would you like to play again? (y / n) ")

        if var == "n":
            print("Game Ending...")
            menu = False
            var_invalid = False
        elif var == "y":
            print("Game restarting...")
            var_invalid = False
        else:
            print("Invalid input please enter y or n")
