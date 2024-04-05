label Proto_Name:
    ############################################################
    # name the player
    ############################################################
    e "Hi, What is your name?"
    # call the default name in this scenario
    $ specifiedName = playerName
    call InsertName
    $ playerName = userInput

    e "Nice to meet you, [p]!"

    ############################################################
    # name the other character
    ############################################################
    sb "Hey, how about picking a new name for me?"
    # call the default name in this scenario
    $ specifiedName = "Sakura"
    call InsertName
    $ sakuraName = userInput

    sb "Thanks for the name, [p]! I love being [sb]!"

    ############################################################
    # Pronouns
    ############################################################
    sb "Oh, I never asked about your pronouns!"
    
    call New_Pronoun

    sb "So you go by [pSub]/[pOb]? Nice!"

    return

label New_Pronoun:
    $ pSub = renpy.input("Pronoun Subjective (he/she/they)")
    $ pSub = pSub.strip()

    $ pCon = renpy.input("Pronoun Contraction (he's/she's/they're)")
    $ pCon = pCon.strip()

    $ pOb = renpy.input("Pronoun Object (him/her/them)")
    $ pOb = pOb.strip()

    $ pPos = renpy.input("Pronoun Possessive (his/hers/theirs)")
    $ pPos = pPos.strip()

    $ pPosAd = renpy.input("Pronoun Possessive Adjective (his/her/their)")
    $ pPosAd = pPosAd.strip()

    $ pRef = renpy.input("Pronoun Reflective (himself/herself/themselves)")
    $ pRef = pRef.strip()

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
        


