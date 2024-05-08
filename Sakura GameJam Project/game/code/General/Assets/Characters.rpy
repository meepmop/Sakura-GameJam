# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen")
############################################################
# User Input Standardization
############################################################
default userInput = ""
default specifiedName = "Bingus"
default targetPerson = 0
# input name
label InsertName:
    if targetPerson == 0:
        $ userInput = renpy.input("Put in your name", length=32)
    if targetPerson == 1:
        $ userInput = renpy.input("Put in your love interest's name", length=32)
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
        "Yes":
            return
        "No":
            jump InsertName
    return

label ConfirmIdentity:
    menu YouSureAboutIdentity:
        "Do you wish to be [p] with the pronouns of [pSub]/[pOb]?"
        "Yes":
            return
        "No":
            $ specifiedName = playerName
            call InsertName
            $ playerName = userInput
            # name has been established
            call ChoosePronoun
            jump ConfirmIdentity

############################################################
# Player name
############################################################
default playerName = "Kiku"
define p = Character("[playerName]", who_color="#df78ff")
# Player pronouns
default pSub = "he"
default pCon = "he's"
default pOb = "him"
default pPos = "his"
default pPosAd = "his"
default pRef = "himself"

label ChoosePronoun:
    menu:
        "What are your pronouns?"
        "he/him":
            $ pSub = "he"
            $ pCon = "he's"
            $ pOb = "him"
            $ pPos = "his"
            $ pPosAd = "his"
            $ pRef = "himself"
            return
        "she/her":
            $ pSub = "she"
            $ pCon = "she's"
            $ pOb = "her"
            $ pPos = "hers"
            $ pPosAd = "her"
            $ pRef = "herself"
            return
        "they/them":
            $ pSub = "they"
            $ pCon = "they're"
            $ pOb = "them"
            $ pPos = "theirs"
            $ pPosAd = "their"
            $ pRef = "themselves"
            return
        "Make your own":
            call NewPronoun
            return

label NewPronoun:
    # player input their pronoun
    $ pSub = renpy.input("Pronoun Subjective (he/she/they) (he ate the cookie)")
    # stip any extra spacing
    $ pSub = pSub.strip()
    # if player put nothing it will default to he/him
    if pSub == "":
        $ pSub = "he"

    $ pCon = renpy.input("Pronoun Contraction (he's/she's/they're) (she's sleeping)")
    $ pCon = pCon.strip()
    if pCon == "":
        $ pCon = "he's"

    $ pOb = renpy.input("Pronoun Object (him/her/them) (are you going to invite them)")
    $ pOb = pOb.strip()
    if pOb == "":
        $ pOb = "him"

    $ pPos = renpy.input("Pronoun Possessive (his/hers/theirs) (that bag is theirs)")
    $ pPos = pPos.strip()
    if pPos == "":
        $ pPos = "his"

    $ pPosAd = renpy.input("Pronoun Possessive Adjective (his/her/their) (their cookie is red)")
    $ pPosAd = pPosAd.strip()
    if pPosAd == "":
        $ pPosAd = "his"

    $ pRef = renpy.input("Pronoun Reflective (himself/herself/themselves) (she bought the bag herself)")
    $ pRef = pRef.strip()
    if pRef == "":
        $ pRef = "himself"

    jump NewPronounConfirm
    return

label NewPronounConfirm:
    menu:
        "is this correct: Subjective ([pSub]), Contraction ([pCon]), Object ([pOb]), 
        Possessive ([pPos]), Possessive Adjective ([pPosAd]), Reflective ([pRef])?"

        "Yes":
            return
        "No":
            jump NewPronoun
    return
############################################################
# Sakura name
############################################################
default sakuraName = "???"
define sb = Character("[sakuraName]", who_color="#ffa6f5", callback = name_callback, cb_name = "sakura")
############################################################
# General Characters
############################################################
# John doe -- aka any character we idk
define jd = Character("???")
define ks = DynamicCharacter("k_name", who_color="#61f288", callback = name_callback, cb_name = "kaito") #Kaito
define ah = DynamicCharacter("a_name",  who_color="#618ff2", callback = name_callback, cb_name = "amari") #amari
define ma = DynamicCharacter("m_name", who_color="#ff6363", callback = name_callback, cb_name = "mikael") #mikael

############################################################
# Mob Characters
############################################################
define sta = Character("Student A")
define stb = Character("Student B")
define stc = Character("Student C")