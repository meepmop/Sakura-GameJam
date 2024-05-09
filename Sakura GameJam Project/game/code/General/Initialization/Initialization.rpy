# The script of the game goes in this file.
# The game starts here.

init:
    $ k_name = '???'
    $ a_name = '???'
    $ m_name = '???'
    default foodstalls = False
    default games = False
    default sbdecide = False

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
            $ k_name = "Kaito"
            $ a_name = "Amari"
            $ m_name = "Mikael"
            jump Chapter2
        "Chapter 3":
            # for debugging
            $ sb = "Sakura"
            $ k_name = "Kaito"
            $ a_name = "Amari"
            $ m_name = "Mikael"
            jump chapter3
    
    # jump Protologue
    return
