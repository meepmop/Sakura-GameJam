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
############################################################
# sbSendMichievous
############################################################
label Chap2_SaySomething:
    # - Affection (SB) + Affection (Kaito) + Affection (Mikael)
    call sbLoveDecrease
    call ksLoveIncrease
    call maLoveIncrease
    call loveNotification
    "Taking notice of [sb]'s sudden look of excitement, you try and pick up 
    the conversation from where it left off."
    "Unfortunately, before you can get a word out, [sb] quickly asserts their 
    vocal dominance upon you."
    "They almost seem like they enjoy it, too."
    return
label Chap2_RemainQuietAgain:
    # + Affection (SB) + Affection (Amari) - Affection (Mikael)
    call sbLoveIncrease
    call ahLoveIncrease
    call maLoveDecrease
    call loveNotification
    return
############################################################
# greaterThorn
############################################################
label Chap2_Uhh:
    # + Affection (Kaito) + Affection (Amari) 
    call ksLoveIncrease
    call ahLoveIncrease
    call loveNotification
    "As much as you’d love to tear into Kaito yourself, judging from the genuine 
    hurt which laced the man’s voice, you gathered that [sb]'s words hit a bit too 
    close to home."
    "In fact, you noticed how rather than sit there and take [sb]'s wrath, 
    Kaito was beginning to roll up his sleeves."
    p "Uh…[sb]?"
    p "Something tells me that we should…get out of here–"
    ks "No, no. I insist."
    ks "If you’re to use such heinous tactics on me, then allow me to repay it in kind 
    with some of my own."
    ks "After all, I’m already late for my duties."
    ks "What’s a few more minutes?"

    return
label Chap2_FutherPush:
    # - Affection (Kaito) + Affection (SB) - Affection (Amari) + Affection (Mikael)
    call ksLoveDecrease
    call sbLoveIncrease
    call ahLoveDecrease
    call maLoveIncrease
    call loveNotification
    "Figuring this would be a good opportunity to deal some sweet, sweet, emotional 
    damage, you clear your throat loudly enough to get the room’s attention."
    p "I may not know half of what [sb] was referring to, but clearly you must be 
    pretty screwed up if just referencing that Mikael guy has you so bothered."
    p "Not just anyone would make me wanna shove some poor guy’s ice cream out of 
    their hands."
    p "I mean, not unless we were lovers. But who could ever love a stuck up, pompous, 
    prick like you–"
    "Pausing mid sentence, you suddenly felt a heavy sense of dread pooling in your 
    stomach."
    "It seemed like in the time it took you to have your little ‘moment’, Kaito 
    had already taken to rolling up his sleeves."
    ks "Are you finished?"
    p "...What’re you doing?"
    ks "Isn’t it obvious?"
    ks "I am giving both you and your unknown companion here time to run."
    ks "While I am not particularly fond of encouraging on-campus violence, as 
    President of the Student Council, I’m sure I can grant myself this one exception."
    return
############################################################
# cherryBlossomEscape
############################################################
label Chap2_ListenToSakura:
    # + Affection (SB) + Affection (Amari) 
    call sbLoveIncrease
    call ahLoveIncrease
    call loveNotification
    "You figured that while cheesy, [sb]'s intuition regarding an escape route was about as 
    good as yours."
    "Letting out a rushed sigh, you turn the corner and continue to run."
    "However, while beautifully decorated, this hallway only had a few lecture halls and no 
    staircase to secure your escape."
    "With your eye now noticeably twitching, you began to count your seconds until Kaito’s 
    promised ass-whooping."
    "That is…until you heard a painstakingly familiar voice."
    return
label Chap2_Ignore:
    # - Affection (SB) - Affection (Amari) 
    call sbLoveDecrease
    call ahLoveDecrease
    call loveNotification
    "Having had enough of [sb]’s antics for one day, you decided to drag them in the direction 
    opposite of where they’d suggested."
    "Much to their displeasure, you were met with a rather bland looking hallway in appearance." 
    "Not to mention, there were crowds of students flocking in every direction."
    "However, it seemed as though despite this, the Elevators which would lead to your 
    escape were currently occupied, and with the nearby staircases looking no better."
    return