label ProtoName:
    ############################################################
    # name the player
    ############################################################
    e "Hi, What is your name?"
    # call the default name in this scenario
    $ specifiedName = playerName
    call InsertName from _call_InsertName_3
    $ playerName = userInput

    e "Nice to meet you, [p]!"

    ############################################################
    # name the other character
    ############################################################
    sb "Hey, how about picking a new name for me?"
    # call the default name in this scenario
    $ specifiedName = "Sakura"
    call InsertName from _call_InsertName_4
    $ sakuraName = userInput

    sb "Thanks for the name, [p]! I love being [sb]!"

    ############################################################
    # Pronouns
    ############################################################
    sb "Oh, I never asked about your pronouns!"
    call ChoosePronoun from _call_ChoosePronoun_2
    sb "So you go by [pSub!c]/[pOb!c]? Nice!"

    return
        


