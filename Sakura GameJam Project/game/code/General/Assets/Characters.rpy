# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
############################################################
# User Input Standardization
############################################################
default userInput = ""
default specifiedName = "Bingus"
# input name
label InsertName:
    $ userInput = renpy.input("Put in the desired name", length=32)
    # strip any extra spacing
    $ userInput = userInput.strip()
    # if the player put nothing use this
    if userInput == "":
        $ userInput = specifiedName
    jump Capitalization
    return
# capitalization
label Capitalization:
    # if it has multiple words, split it
    $ sentences = userInput.split(" ")
    # always capitalize the first letter of each word in the sentence
    $ capitalSentence = [userInput[0].upper() + userInput[1:] for userInput in sentences]
    # use this in the outside to do the referal of who is who
    $ userInput = " ".join(capitalSentence)

    menu:
        "Is [userInput] the name you wish?"
        "yes":
            return
        "no":
            jump InsertName
    return

############################################################
# Player name
############################################################
default playerName = "Kiku"
define p = Character("[playerName]")
# Player pronouns
default pSub = "he"
default pCon = "he's"
default pOb = "him"
default pPos = "his"
default pPosAd = "his"
default pRef = "himself"
############################################################
# Sakura name
default sakuraName = "???"
define sb = Character("[sakuraName]")
