# The script of the game goes in this file.
# The game starts here.

label start:
    
    menu levelSelect:
        "Choose a chapter"
        "Protologue":
            jump Protologue
        "Chapter 1":
            # for debugging
            $ sb = "Sakura"
            jump Chapter1
        "Chapter 2":
            # for debugging
            $ sb = "Sakura"
            jump Chapter2
    
    # jump Protologue
    return
