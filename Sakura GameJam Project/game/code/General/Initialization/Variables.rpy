# Variables used througout the game
############################################################
# Love
############################################################
# sakura boy Attraction level
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
# kaito Attraction level
default ksLove = 0
# ks Attraction level calling
label ksLoveIncrease:
    "[ks] liked that"
    $ ksLove += 1
    return
label ksLoveDecrease:
    "[ks] disliked that"
    $ ksLove -= 1
    return
############################################################
# amari Attraction level
default ahLove = 0
# ah Attraction level calling
label ahLoveIncrease:
    "[ah] liked that"
    $ ahLove += 1
    return
label ahLoveDecrease:
    "[ah] disliked that"
    $ ahLove -= 1
    return
############################################################
# michael Attraction level
default maLove = 0
# ma Attraction level calling
label maLoveIncrease:
    "[ma] liked that"
    $ maLove += 1
    return
label maLoveDecrease:
    "[ma] disliked that"
    $ maLove -= 1
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