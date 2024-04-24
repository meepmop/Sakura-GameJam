############################################################
# lastChat
############################################################
label Chap2_Well:
    # + Affection (SB) + Affection (Amari)
    call sbLoveIncrease
    call ahLoveIncrease
    call loveNotification
    p "Well– yeah! The guy’s a walking weirdo!"
    p "I can’t seem to stop running into them."
    p "How many are we up to, 4 now?!"
    p "It’s not even halfway through the week yet!!"
    "[sb] can’t help but snort at your dramatics."
    sb "Would you not be the fifth?"
    sb "After all, 5 is a much more lovely number, is it not?"
    return
label Chap2_RemainQuiet:
    # - Affection (SB) + Affection (Kaito)
    call sbLoveDecrease
    call ksLoveIncrease
    call loveNotification
    "Feeling your face begin to redden, you quickly look away from [sb]."
    "However, glancing back to check their reaction, you notice the slight frown which 
    tugs at their lips."
    sb "I must admit, he is a rather dashing fellow."
    sb "Perhaps he can be the one to share those tickets with~"
    return
############################################################
# letsDoThis
############################################################
label Chap2_ReachDoor:
    # + Affection (Mikael) - Affection (Kaito)
    call maLoveIncrease
    call ksLoveDecrease
    call loveNotification
    "Feeling [sb]'s eager gaze peering into you, you cautiously extend your hand out 
    to grasp at the doorknob."
    "However, right before you can turn it, you are met with a rather…unpleasant 
    looking face standing in the doorway."
    "What there even was of one, at least."
    ks "I could hear you both from down the hall."
    ks "Just how stupid do you think I am?"
    return
label Chap2_Knock:
    # + Affection (Kaito) - Affection (Mikael) 
    call ksLoveIncrease
    call maLoveDecrease
    call loveNotification
    "Rationalizing that it would be stupid to suddenly enter one’s office 
    without at the very least knocking, you close your eyes to brace yourself on 
    telling the Councilman of your presence."
    ks "Um. Excuse me."
    p "?!?"
    ks "What are you doing here?"
    ks "While I appreciate the effort to formally make yourselves known, you both 
    were rather loud when disclosing your so-called ‘Plan’."
    return
############################################################
# wallflowerStranger
############################################################
label Chap2_ForLastTime:
    # - Affection (SB) - Affection (Kaito) + Affection (Mikael)
    call sbLoveDecrease
    call ksLoveDecrease
    call maLoveIncrease
    call loveNotification
    p "You know what."
    sb "[p]!"
    p "If you’re gonna keep insulting me, at least have the decency to do so face 
    to face!"
    sb "Wait–!"
    "Feeling your brow twitch, you let your anger get the better of you."
    "Reaching to yank the man’s mask off, were it not for Kaito’s reflexes, 
    you would have gotten a one way ticket to the Dean’s office."
    "Instead, you’re met with yourself pathetically tumbling forward at what 
    was the only neatly organized stack of papers in the room."
    return
label Chap2_RoomMess:
    # + Affection (SB) + Affection (Amari)
    call sbLoveIncrease
    call ahLoveIncrease
    call loveNotification
    "Taking a better look around you, you decide to ignore the over-used insult 
    which was being flung your way."
    "Instead, you find yourself focusing on the area around you."
    "Paper everywhere."
    "The room, poorly lit."
    "And the person within it, clearly worse for wear."
    "Not that that mattered much to you anyways."
    p "You know I’d be focusing on other things were I in your shoes."
    p "For someone that’s always enforcing the rules, clearly you need to brush up 
    on whatever handbook you wrote."
    sb "Oooo~"
    sb "I-I mean–! Ooo…oo…h my."
    return
label Chap2_YouMess:
    # + Affection (Kaito) - Affection (Amari)
    call ksLoveIncrease
    call sbLoveDecrease
    call loveNotification
    "Instead of focusing on the haphazard insult, you hone your attention to the 
    man who spoke it."
    "Despite the layer of confidence which he wore, you could easily see the 
    signs of exhaustion taking their toll."
    p "You know, a mask can’t hide everything."
    p "When was the last time you even took a break?"
    p "Shouldn’t that dramatic looking guy be the one asking you these things??"
    ks "Well…they’re…"
    p "Not here. Exactly."
    return