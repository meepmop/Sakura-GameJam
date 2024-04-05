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

label New_Pronoun:
    $ pSub = renpy.input("Pronoun Subjective (he/she/they)")
    $ pSub = pSub.strip()
    if pSub == "":
        $ pSub = "he"

    $ pCon = renpy.input("Pronoun Contraction (he's/she's/they're)")
    $ pCon = pCon.strip()
    if pCon == "":
        $ pCon = "he's"

    $ pOb = renpy.input("Pronoun Object (him/her/them)")
    $ pOb = pOb.strip()
    if pOb == "":
        $ pOb = "him"

    $ pPos = renpy.input("Pronoun Possessive (his/hers/theirs)")
    $ pPos = pPos.strip()
    if pPos == "":
        $ pPos = "his"

    $ pPosAd = renpy.input("Pronoun Possessive Adjective (his/her/their)")
    $ pPosAd = pPosAd.strip()
    if pPosAd == "":
        $ pPosAd = "his"

    $ pRef = renpy.input("Pronoun Reflective (himself/herself/themselves)")
    $ pRef = pRef.strip()
    if pRef == "":
        $ pRef = "himself"

    jump New_Pronoun_Confirm
    return

label New_Pronoun_Confirm:
    menu:
        "is this correct: Subjective ([pSub]), Contraction ([pCon]), Object ([pOb]), 
        Possessive ([pPos]), Possessive Adjective ([pPosAd]), Reflective ([pRef])?"

        "Yes":
            return
        "No":
            jump New_Pronoun
    return
############################################################
# Sakura name
default sakuraName = "???"
define sb = Character("[sakuraName]")
