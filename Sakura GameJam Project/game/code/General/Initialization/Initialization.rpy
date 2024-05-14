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
    
    jump Protologue
    
    return
