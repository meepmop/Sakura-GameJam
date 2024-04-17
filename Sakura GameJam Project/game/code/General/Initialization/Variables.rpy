# Variables used througout the game
############################################################
# Love
############################################################
# sb Attraction level
default sbLove = 0
# sb Attraction level calling
label sbLoveIncrease:
    "[sb] liked that"
    $ sbLove += 1
    return
label sbLoveDecrease:
    "[sb] disliked that"
    $ sbLove -= 1
    return
############################################################
# Situational 
############################################################
# if choice trigger something that sb likes to the images or actions
# only per chapter usage
default sbTrig = False
# need a choice to go away? use this to tag
default choice1Chosen = False

# reset any situational triggers
label situTriggerReset:
    $ sbTrig = False
    $ choice1Chosen = False
    return