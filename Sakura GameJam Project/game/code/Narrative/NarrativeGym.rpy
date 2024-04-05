############################################################
# Tutorial
############################################################
# Heyoooo, I'm assumming you know the basics of renpy after playing
# through the tutorial from Renpy, so I'll tell you the acronyms
############################################################
# Characters
# p = player character
#### [e.g] p "Hello! This is the player speaking"
# sb = sakura boy
#### [e.g] sb "Sakura boy is talking" 
############################################################
# Pronouns
# pSub = Subject - "he"
# pCon = Contraction - "he's"
# pOb = Object - "him"
# pPos = Possesive - "his"
# pPosAd = possesive adjdective - "his"
# pRef = reflective - "himself"

# so when you want to do dialogue that refers to the player's pronoun
# use [] to do so and don't put in "is" or "are" in
#### [e.g] Code: sb "Sakura boy is talking to [pOb]"
#### [e.g] Game: sb "Sakura boy is talking to him"
# [tip] use !c to capitalize
#### [e.g] Code: "[pSub!c] speaketh!"
#### [e.g] Game: "He speaketh!"
############################################################
# Any questions lmk but do all your work in the Narrative Gym for now
# I have set up the game to look at the Narrative Gym so you can test out things
############################################################

label GameStart:
    "Hello! Game Starts here!"
    return