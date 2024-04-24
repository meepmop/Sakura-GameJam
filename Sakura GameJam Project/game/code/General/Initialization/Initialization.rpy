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
        "Love Notification Test":
            jump LoveNotifyTest
    
    # jump Protologue
    return
