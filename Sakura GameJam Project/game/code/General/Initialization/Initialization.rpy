# The script of the game goes in this file.
# The game starts here.

init:
    $ k_name = '???'
    $ a_name = '???'
    $ m_name = '???'

label start:
    
    menu levelSelect:
        "Choose a chapter"
        "Prologue":
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
