############################################################
# My head choice
############################################################
label Proto_StayQuiet:
    "I focus my gaze onto the person in front of me."
    "Too stunned to speak, it's as if their appearance alone locks my lips in place."

    show sb neutral

    sb "I'm surprised my neck hasn't snapped."

    show sb oh

    sb "...Oh, wait just a moment..!"

    show sb neutral

    sb "It seems the grass being a bit more 'cushiony' than normal wasn't just my imagination."
    sb "My apologies~"
    return

label Proto_TheyOk:
    # makes sure that the choice will give a happy emote when exit
    $ sbTrig = True
    # 1+ Attraction
    call sbLoveIncrease from _call_sbLoveIncrease_21
    call loveNotification from _call_loveNotification_57
    p "Are you alright?"
    p "You're not hurt, are you?"
    p "I don't particularly feel like dragging anyone to the hospital today."

    show sb oh

    sb "Oh dear– My apologies. It seems you were the one who broke my fall."

    show sb neutral

    sb "You're rather kind for someone who also just hurt themselves~"
    return

label Proto_Insult:
    # -1 Attraction
    call sbLoveDecrease from _call_sbLoveDecrease_13
    call loveNotification from _call_loveNotification_58

    show sb excited

    p "Hey! What the hell's wrong with you?!"
    p "How'd you even get up in that tree in the first place!?"
    p "You know if you damaged that tree, the administration is never gonna let us hear 
    the end of it!"
    p "Not to mention–Ouch!"

    show sb oh

    sb "Oh dear– My apologies. It seems you were the one who broke my fall."
    sb "I didn't mean to hurt you. Honestly~"
    return
############################################################
# Who sent choice
############################################################
label Proto_MomSent:

    show sb excited

    p "So…uh. Are you that guy?"
    p "You know. The one who was supposed to be here a couple hours ago?"

    show sb neutral

    sb "Honestly. Is it bad that I don't have an answer to that?"
    sb "I could be."
    show sb neutral
    sb "But I could also just be some random guy who just so happened to fall 
    out from that tree."
    show sb neutral
    sb "I'm thinking the second option might be more likely~"
    return
label Proto_WhyLate:

    show sb excited

    p "You kept me waiting for a while. Don't tell me you fell asleep in that tree."
    p "Honestly…how does my mom even come up with these guys?"

    show sb neutral

    sb "Kept you waiting, you say?"

    show sb neutral

    sb "Would it be bad to admit that I don't even know who you are~?"
    return
############################################################
# Concert Ticket choice
############################################################
label Proto_Ridiculous:
    p "This is ridiculous."
    p "There's no way some stupid fall could just cause you to suddenly blank out on who the Hell you are!!"
    p "I'm gonna call the cops-"
    show sb neutral
    sb "Why don't we just get started~"
    "[sb] casts a wink your way and lets out another lighthearted laugh." 
    "You can't tell whether your face flushes from endearment or annoyance."
    "It's almost infectious."
    "This person… there must be a reason which fate brought you both together."
    "Be it for some 'Divine Purpose', or just a pair of concert tickets."
    "One thing remains clear."
    "You were about to have quite the week ahead of you."
    return

label Proto_No:
    p "No."
    call situTriggerReset from _call_situTriggerReset_3
    return