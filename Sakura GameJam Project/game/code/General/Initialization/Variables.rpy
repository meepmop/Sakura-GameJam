# Variables used througout the game
############################################################
# notify function
############################################################
default sbLoveState = 0
default ksLoveState = 0
default ahLoveState = 0
default maLoveState = 0
default loveStateTotal = 0
# 0 = neutral, 1 = Liked, 2 = Disliked
label loveNotification:
    # add the total of the love and hate
    $ loveStateTotal = sbLoveState + ksLoveState + ahLoveState + maLoveState
    # only one person liked it
    if loveStateTotal == 1:
        if sbLoveState == 1:
            $ renpy.notify("[sb] liked that")
        if ksLoveState == 1:
            $ renpy.notify("[ks] liked that")
        if ahLoveState == 1:
            $ renpy.notify("[ah] liked that")
        if maLoveState == 1:
            $ renpy.notify("[ma] liked that")
    # only one person did not like that or 2 ppl liked it
    elif loveStateTotal == 2:
        # sb ###################################################
        # if the 2 comes all from sb then it's a hate
        if sbLoveState == 2:
            $ renpy.notify("[sb] disliked that")
        # if it's only 1 that adds to 2 then it's a like
        if sbLoveState == 1:
            # minus from the lovestate total from sb contribution so we know that the other person
            # needs to end the notification system
            $ loveStateTotal = loveStateTotal - sbLoveState
            $ notices.append("[sb] liked that")
        # ks ###################################################
        if ksLoveState == 2:
            $ renpy.notify("[ks] disliked that")
        if ksLoveState == 1:
            $ loveStateTotal = loveStateTotal - ksLoveState
            if loveStateTotal == 0:
                $ notify_me("[ks] liked that")
            elif loveStateTotal >= 1:
                $ notices.append("[ks] liked that")
        # ah ###################################################
        if ahLoveState == 2:
            $ renpy.notify("[ah] disliked that")
        if ahLoveState == 1:
            $ loveStateTotal = loveStateTotal - ahLoveState
            if loveStateTotal == 0:
                $ notify_me("[ah] liked that")
            elif loveStateTotal >= 1:
                $ notices.append("[ah] liked that")
        # ma ###################################################
        if maLoveState == 2:
            $ renpy.notify("[ma] disliked that")
        if maLoveState == 1:
            $ loveStateTotal = loveStateTotal - maLoveState
            if loveStateTotal == 0:
                $ notify_me("[ma] liked that")
    # if multiple people are disliking and liking
    elif loveStateTotal >= 3:
        # sb ###################################################
        # if the 2 comes all from sb then it's a hate
        if sbLoveState == 2:
            # minus from the lovestate total from sb contribution so we know that the other person
            # needs to end the notification system
            $ loveStateTotal = loveStateTotal - sbLoveState
            $ notices.append("[sb] disliked that")
        # if it's only 1 that adds to 2 then it's a like
        if sbLoveState == 1:
            # minus from the lovestate total from sb contribution so we know that the other person
            # needs to end the notification system
            $ loveStateTotal = loveStateTotal - sbLoveState
            $ notices.append("[sb] liked that")
        # ks ###################################################
        if ksLoveState == 2:
            $ loveStateTotal = loveStateTotal - ksLoveState
            # if that is the end of the line -- end of the line message
            if loveStateTotal == 0:
                $ notify_me("[ks] disliked that")
            # if not, continue along
            $ notices.append("[ks] disliked that")
        if ksLoveState == 1:
            $ loveStateTotal = loveStateTotal - ksLoveState
            # if that is the end of the line -- end of the line message
            if loveStateTotal == 0:
                $ notify_me("[ks] liked that")
            # if not, continue along
            elif loveStateTotal >= 1:
                $ notices.append("[ks] liked that")
        # ah ###################################################
        if ahLoveState == 2:
            $ loveStateTotal = loveStateTotal - ahLoveState
            if loveStateTotal == 0:
                $ notify_me("[ah] disliked that")
            elif loveStateTotal >= 1:
                $ notices.append("[ah] disliked that")
        if ahLoveState == 1:
            $ loveStateTotal = loveStateTotal - ahLoveState
            if loveStateTotal == 0:
                $ notify_me("[ah] liked that")
            elif loveStateTotal >= 1:
                $ notices.append("[ah] liked that")
        # ma ###################################################
        if maLoveState == 2:
            $ loveStateTotal = loveStateTotal - maLoveState
            $ notify_me("[ma] disliked that")
        if maLoveState == 1:
            $ loveStateTotal = loveStateTotal - maLoveState
            $ notify_me("[ma] liked that")
    # reset the numbers
    $ sbLoveState = 0
    $ ksLoveState = 0
    $ ahLoveState = 0
    $ maLoveState = 0
    $ loveStateTotal = 0
    return
############################################################
# Love
############################################################
# sakura boy Attraction level
default sbLove = 0
# sb Attraction level calling
label sbLoveIncrease:
    # $ notices.append("{image=Items/Placeholder/logo_sb_approve.png} [sb] liked that")
    # $ notify_me("nice")
    # $ renpy.notify("{image=Items/Placeholder/logo_sb_approve.png} [sb] liked that")
    $ sbLoveState = 1
    $ sbLove += 1
    return
label sbLoveDecrease:
    # "[sb] disliked that"
    $ sbLoveState = 2
    $ sbLove -= 1
    return
############################################################
# kaito Attraction level
default ksLove = 0
# ks Attraction level calling
label ksLoveIncrease:
    # $ renpy.notify("{image=Items/Placeholder/logo_ks_approve.png} [ks] liked that")
    $ ksLoveState = 1
    $ ksLove += 1
    return
label ksLoveDecrease:
    # "[ks] disliked that"
    $ ksLoveState = 2
    $ ksLove -= 1
    return
############################################################
# amari Attraction level
default ahLove = 0
# ah Attraction level calling
label ahLoveIncrease:
    $ ahLoveState = 1
    # "[ah] liked that"
    $ ahLove += 1
    return
label ahLoveDecrease:
    $ ahLoveState = 2
    # $ renpy.notify("{image=Items/Placeholder/logo_ah_disapprove.png} [ah] disliked that")
    $ ahLove -= 1
    return
############################################################
# michael Attraction level
default maLove = 0
# ma Attraction level calling
label maLoveIncrease:
    $ maLoveState = 1
    # "[ma] liked that"
    $ maLove += 1
    return
label maLoveDecrease:
    $ maLoveState = 2
    # "[ma] disliked that"
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