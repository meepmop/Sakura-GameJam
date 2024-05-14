############################################################
# lastChat
############################################################
label Chap2_Well:
    # + Affection (SB) + Affection (Amari)
    call sbLoveIncrease from _call_sbLoveIncrease_8
    call ahLoveIncrease from _call_ahLoveIncrease_4
    call loveNotification from _call_loveNotification_27
    p "Well– yeah! The guy's a walking weirdo!"
    p "I can't seem to stop running into them."
    p "How many are we up to, 4 now?!"
    p "It's not even halfway through the week yet!!"
    "[sb] can't help but snort at your dramatics."
    sb "Would you not be the fifth?"
    sb "After all, 5 is a much more lovely number, is it not?"
    return
label Chap2_RemainQuiet:
    # - Affection (SB) + Affection (Kaito)
    call sbLoveDecrease from _call_sbLoveDecrease_4
    call ksLoveIncrease from _call_ksLoveIncrease_4
    call loveNotification from _call_loveNotification_28
    "Feeling your face begin to redden, you quickly look away from [sb]."
    show sb annoyed
    "However, glancing back to check their reaction, you notice the slight frown which 
    tugs at their lips."
    sb "I must admit, he is a rather dashing fellow."
    show sb neutral
    sb "Perhaps he can be the one to share those tickets with~"
    return
############################################################
# letsDoThis
############################################################
label Chap2_ReachDoor:
    # + Affection (Mikael) - Affection (Kaito)
    call maLoveIncrease from _call_maLoveIncrease_6
    call ksLoveDecrease from _call_ksLoveDecrease_2
    call loveNotification from _call_loveNotification_29
    "Feeling [sb]'s eager gaze peering into you, you cautiously extend your hand out 
    to grasp at the doorknob."
    "However, right before you can turn it, you are met with a rather…unpleasant 
    looking face standing in the doorway."
    "What there even was of one, at least."
    show ks angry at right
    show sb oh at left
    with dissolve
    ks "I could hear you both from down the hall."
    ks "Just how stupid do you think I am?"
    return
label Chap2_Knock:
    # + Affection (Kaito) - Affection (Mikael) 
    call ksLoveIncrease from _call_ksLoveIncrease_5
    call maLoveDecrease from _call_maLoveDecrease_4
    call loveNotification from _call_loveNotification_30
    "Rationalizing that it would be stupid to suddenly enter one's office 
    without at the very least knocking, you close your eyes to brace yourself on 
    telling the Councilman of your presence."
    show ks angry at right
    show sb excited at left 
    with dissolve
    ks "Um. Excuse me."
    p "?!?"
    ks "What are you doing here?"
    ks "While I appreciate the effort to formally make yourselves known, you both were rather loud when disclosing your so-called \"plan.\""
    return
############################################################
# wallflowerStranger
############################################################
label Chap2_ForLastTime:
    # - Affection (SB) - Affection (Kaito) + Affection (Mikael)
    call sbLoveDecrease from _call_sbLoveDecrease_5
    call ksLoveDecrease from _call_ksLoveDecrease_3
    call maLoveIncrease from _call_maLoveIncrease_7
    call loveNotification from _call_loveNotification_31
    p "You know what."
    show sb annoyed
    show ks neutral
    sb "[p]!"
    p "If you're gonna keep insulting me, at least have the decency to do so face 
    to face!"
    sb "Wait–!"
    "Feeling your brow twitch, you let your anger get the better of you."
    "Reaching to yank the man's mask off, were it not for Kaito's reflexes, you would have gotten a one way ticket to the Dean's office."
    "Instead, you're met with yourself pathetically tumbling forward at what was the only neatly organized stack of papers in the room."
    return
label Chap2_RoomMess:
    # + Affection (SB) + Affection (Amari)
    call sbLoveIncrease from _call_sbLoveIncrease_9
    call ahLoveIncrease from _call_ahLoveIncrease_5
    call loveNotification from _call_loveNotification_32
    "Taking a better look around you, you decide to ignore the over-used insult 
    which was being flung your way."
    "Instead, you find yourself focusing on the area around you."
    "Paper everywhere."
    "The room, poorly lit."
    "And the person within it, clearly worse for wear."
    "Not that that mattered much to you anyways."
    p "You know I'd be focusing on other things were I in your shoes."
    p "For someone that's always enforcing the rules, clearly you need to brush up on whatever handbook you wrote."
    show sb neutral
    sb "Oooo~"
    show sb oh
    sb "I-I mean–! Ooo…oo…h my."
    return
label Chap2_YouMess:
    # + Affection (Kaito) - Affection (Amari)
    call ksLoveIncrease from _call_ksLoveIncrease_6
    call sbLoveDecrease from _call_sbLoveDecrease_6
    call loveNotification from _call_loveNotification_33
    "Instead of focusing on the haphazard insult, you hone your attention to the 
    man who spoke it."
    "Despite the layer of confidence which he wore, you could easily see the 
    signs of exhaustion taking their toll."
    p "You know, a mask can't hide everything."
    p "When was the last time you even took a break?"
    p "Shouldn't that dramatic looking guy be the one asking you these things??"
    show ks angry
    ks "Well…they're…"
    p "Not here. Exactly."
    return
############################################################
# sbSendMichievous
############################################################
label Chap2_SaySomething:
    # - Affection (SB) + Affection (Kaito) + Affection (Mikael)
    call sbLoveDecrease from _call_sbLoveDecrease_7
    call ksLoveIncrease from _call_ksLoveIncrease_7
    call maLoveIncrease from _call_maLoveIncrease_8
    call loveNotification from _call_loveNotification_34
    "Taking notice of [sb]'s sudden look of excitement, you try and pick up the conversation from where it left off."
    "Unfortunately, before you can get a word out, [sb] quickly asserts their vocal dominance upon you."
    "They almost seem like they enjoy it, too."
    return
label Chap2_RemainQuietAgain:
    # + Affection (SB) + Affection (Amari) - Affection (Mikael)
    call sbLoveIncrease from _call_sbLoveIncrease_10
    call ahLoveIncrease from _call_ahLoveIncrease_6
    call maLoveDecrease from _call_maLoveDecrease_5
    call loveNotification from _call_loveNotification_35
    return
############################################################
# greaterThorn
############################################################
label Chap2_Uhh:
    # + Affection (Kaito) + Affection (Amari) 
    call ksLoveIncrease from _call_ksLoveIncrease_8
    call ahLoveIncrease from _call_ahLoveIncrease_7
    call loveNotification from _call_loveNotification_36
    "As much as you'd love to tear into Kaito yourself, judging from the genuine hurt which laced the man's voice, you gathered that [sb]'s words hit a bit too close to home."
    "In fact, you noticed how rather than sit there and take [sb]'s wrath, 
    Kaito was beginning to roll up his sleeves."
    p "Uh…[sb]?"
    p "Something tells me that we should…get out of here–"
    show ks neutral
    ks "No, no. I insist."
    ks "If you're to use such heinous tactics on me, then allow me to repay it in kind with some of my own."
    ks "After all, I'm already late for my duties."
    ks "What's a few more minutes?"

    return
label Chap2_FutherPush:
    # - Affection (Kaito) + Affection (SB) - Affection (Amari) + Affection (Mikael)
    call ksLoveDecrease from _call_ksLoveDecrease_4
    call sbLoveIncrease from _call_sbLoveIncrease_11
    call ahLoveDecrease from _call_ahLoveDecrease_3
    call maLoveIncrease from _call_maLoveIncrease_9
    call loveNotification from _call_loveNotification_37
    "Figuring this would be a good opportunity to deal some sweet, sweet, emotional 
    damage, you clear your throat loudly enough to get the room's attention."
    p "I may not know half of what [sb] was referring to, but clearly you must be 
    pretty screwed up if just referencing that Mikael guy has you so bothered."
    p "Not just anyone would make me wanna shove some poor guy's ice cream out of 
    their hands."
    p "I mean, not unless we were lovers. But who could ever love a stuck up, pompous, 
    prick like you–"
    "Pausing mid sentence, you suddenly felt a heavy sense of dread pooling in your 
    stomach."
    "It seemed like in the time it took you to have your little \"moment,\" Kaito 
    had already taken to rolling up his sleeves."
    ks "Are you finished?"
    p "...What're you doing?"
    show ks neutral
    ks "Isn't it obvious?"
    ks "I am giving both you and your unknown companion here time to run."
    ks "While I am not particularly fond of encouraging on-campus violence, as President of the Student Council, I'm sure I can grant myself this one exception."
    return
############################################################
# cherryBlossomEscape
############################################################
label Chap2_ListenToSakura:
    # + Affection (SB) + Affection (Amari) 
    call sbLoveIncrease from _call_sbLoveIncrease_12
    call ahLoveIncrease from _call_ahLoveIncrease_8
    call loveNotification from _call_loveNotification_38
    "You figured that while cheesy, [sb]'s intuition regarding an escape route was about as 
    good as yours."
    "Letting out a rushed sigh, you turn the corner and continue to run."
    show sb oh
    "However, while beautifully decorated, this hallway only had a few lecture halls and no staircase to secure your escape."
    "With your eye now noticeably twitching, you began to count your seconds until Kaito's 
    promised ass-whooping."
    "That is…until you heard a painstakingly familiar voice."
    return
label Chap2_Ignore:
    # - Affection (SB) - Affection (Amari) 
    call sbLoveDecrease from _call_sbLoveDecrease_8
    call ahLoveDecrease from _call_ahLoveDecrease_4
    call loveNotification from _call_loveNotification_39
    "Having had enough of [sb]'s antics for one day, you decided to drag them in the direction opposite of where they'd suggested."
    show sb oh
    "Much to their displeasure, you were met with a rather bland looking hallway in appearance." 
    "Not to mention, there were crowds of students flocking in every direction."
    "However, it seemed as though despite this, the elevators which would lead to your escape were currently occupied, and with the nearby staircases looking no better."
    return
############################################################
# sufferHands
############################################################
label Chap2_TakeAmariHand:
    # + Affection (Amari) 
    call ahLoveIncrease from _call_ahLoveIncrease_9
    call loveNotification from _call_loveNotification_40
    "Considering Amari had a point, you reach out your hand for the other to take."
    "Surprisingly, despite the slender appearance, you find both you and [sb] are easily lifted onto their steed."
    return
label Chap2_StandStill:
    # - Affection (Amari) + Affection (SB)
    call ahLoveDecrease from _call_ahLoveDecrease_5
    call sbLoveIncrease from _call_sbLoveIncrease_13
    call loveNotification from _call_loveNotification_41
    "Finding yourself frozen, it takes [sb] pushing you forward for you to get a grip."
    "However, despite this, you still couldn't help but wonder how the hell there was 
    a damn horse in front of you."
    "Where did it even come from?"
    "Did the damned thing ride the elevator to get up here!?"
    "There were so many questions just waiting to be answered."
    return
label Chap2_AcceptFate:
    # *Choosing this option will immediately end the game*
    "Rather than accept the offer of being spared Kaito's wrath from Amari, you 
    instead turn away from them."
    sb "[p]?!"
    p "You know, I've had a lot of weird things happen to me this week, but I think I draw the line at equestrians."
    p "I'm sure Kaito wouldn't dare lay a hand on us with all these people around–"
    ks "I beg to differ!"
    play sound "audio/punch.mp3"
    scene black with Dissolve(0.5)
    stop music fadeout 1.0
    pause 2.0
    # *The screen fades to black as a loud punching sound plays*
    return
############################################################
# partOfShow
############################################################
label Chap2_WarnKaito:
    # + Affection (Kaito) + Affection (Mikael)
    call ksLoveIncrease from _call_ksLoveIncrease_9
    call maLoveIncrease from _call_maLoveIncrease_10
    call loveNotification from _call_loveNotification_42
    p "What're you doing?!"
    p "It's like you want to die!!!!"
    return
label Chap2_TauntKaito:
    # - Affection (Kaito) + Affection (SB) + Affection (Amari)
    call ksLoveDecrease from _call_ksLoveDecrease_5
    call sbLoveIncrease from _call_sbLoveIncrease_14
    call ahLoveIncrease from _call_ahLoveIncrease_10
    call loveNotification from _call_loveNotification_43
    p "Looks like you can keep that spot in the infirmary open, huh?!"
    p "Charge!!"
    return
############################################################
# strugglingSakura
############################################################
label Chap2_HelpThem:
    # + Affection (SB) 
    call sbLoveIncrease from _call_sbLoveIncrease_15
    call loveNotification from _call_loveNotification_44
    show sb neutral
    "Reaching your hand for [sb] to grasp, you're met with an embarrassed \"Thank you.\""
    sb "It seems like I didn't meet the height requirements~"
    sb "I'm so glad to have someone like you by my side, [p]."

    return
label Chap2_HandleIt:
    # - Affection (SB) + Affection (AH)
    call sbLoveDecrease from _call_sbLoveDecrease_9
    call ahLoveIncrease from _call_ahLoveIncrease_11
    call loveNotification from _call_loveNotification_45
    "Rolling your eyes at the pitiful display of shortness before you, you turn away from [sb]."
    "This causes them to let out a pathetic whine, and after a few more attempts to safely dismount, [sb] ends up with their face smacked right against the unforgiving 
    dirt below."
    show sb annoyed
    sb "Ouch…"
    return
############################################################
# startSwinging
############################################################
label Chap2_WeBully:
    # + Affection (Amari) + Affection (SB) + Affection (Mikael)
    call ahLoveIncrease from _call_ahLoveIncrease_12
    call sbLoveIncrease from _call_sbLoveIncrease_16
    call maLoveIncrease from _call_maLoveIncrease_11
    call loveNotification from _call_loveNotification_46
    p "Well, that Mikael guy just told us to keep him busy for a bit."
    p "He looked like he hadn't slept in a few days…so that part wasn't too hard."
    p "Honestly, I have to admit. Were it not for [sb]'s weird prying, I don't think we'd have been able to do it."

    return
label Chap2_SakuraBully:
    # + Affection (Kaito) - Affection (SB) + - Affection (Amari)
    call ksLoveIncrease from _call_ksLoveIncrease_10
    call sbLoveDecrease from _call_sbLoveDecrease_10
    call ahLoveDecrease from _call_ahLoveDecrease_6
    call loveNotification from _call_loveNotification_47
    p "Don't ask me, [sb] was the one who went ahead and pried into the guy's past."
    p "I was only doing that Mikael guy a favor so that he wouldn't flour bomb us!"
    show sb excited
    sb "H-Hey! I couldn't help it~"
    sb "Just looking at him caused all sorts of emotions to swell up within me…"
    sb "It almost made me want to cry~"
    return
############################################################
# sparkTheFire
############################################################
label Chap2_NudgeSB:
    # - Affection (SB) + Affection (Amari)
    call sbLoveDecrease from _call_sbLoveDecrease_11
    call ahLoveIncrease from _call_ahLoveIncrease_13
    call loveNotification from _call_loveNotification_48
    p "C'mon, [sb]~ Try peering into their past or something…"
    p "Unless what you pulled back there was just for show~"
    show sb oh
    sb "Way to put me on the spot…" 
    sb "So cruel~"
    return
label Chap2_StandAwkward:
    # + Affection (SB) - Affection (Amari)
    call sbLoveIncrease from _call_sbLoveIncrease_17
    call ahLoveDecrease from _call_ahLoveDecrease_7
    call loveNotification from _call_loveNotification_49
    "When [sb] casts a worried look your way, you match it with an awkward upwards tug 
    of your lips."
    "Unsure of who's side to take in this situation, you opt to just let fate take 
    its course."
    "After all, part of you did wish to see what was the deal with [sb]'s 
    whole…peering into the past situation."

    return
############################################################
# beginningForCharacter
############################################################
label Chap2_StayQuiet:
    # + Affection (Amari) - Affection (SB)
    call ahLoveIncrease from _call_ahLoveIncrease_14
    call sbLoveDecrease from _call_sbLoveDecrease_12
    call loveNotification from _call_loveNotification_50
    scene BG YYFront
    show ah angry at center
    show sb annoyed at right
    with dissolve
    "Trusting Amari's word to not try and attack you both, you simply stare in awe at the vivid image which [sb] once again paints for you."
    "It's almost scary."
    "How could this guy know the memories of others but not their own?!"

    return
label Chap2_SpeakUp:
    # - Affection (Amari) + Affection (SB)
    call ahLoveDecrease from _call_ahLoveDecrease_8
    call sbLoveIncrease from _call_sbLoveIncrease_18
    call loveNotification from _call_loveNotification_51
    p "Are you sure that you actually want to hear this stuff?"
    p "Seems…kinda like an invasion of your privacy, don't you think–"
    ah "Nonsense!"
    return
############################################################
# wouldntAgree
############################################################
label Chap2_Touching:
    # + Affection (Amari)
    call ahLoveIncrease from _call_ahLoveIncrease_15
    call loveNotification from _call_loveNotification_52
    p "T-Touching…you're–"
    ah "Ah~ The way you squirm is quite wonderful~"
    ah "However, I'll spare you…"
    ah "For now, that is~"

    return
label Chap2_OnlyTragic:
    # - Affection (Amari) + Affection (SB)
    call ahLoveDecrease from _call_ahLoveDecrease_9
    call sbLoveIncrease from _call_sbLoveIncrease_19
    call loveNotification from _call_loveNotification_53
    "Forcing yourself not to react to the firm touch of Amari, you force yourself 
    to put on the farce of being unaffected."
    p "You know, t-the only thing that's tragic is here is how you're viewing this as some sort of \"show.\""
    p "[sb] isn't some form of entertainment."
    p "They're human."
    p "Just…a kind of messed up one at the moment."
    return
############################################################
# accomplishFriday
############################################################
label Chap2_MentionMikael:
    # + Affection (Mikael)
    call maLoveIncrease from _call_maLoveIncrease_12
    call loveNotification from _call_loveNotification_54
    p "At least we don't have to worry about being flour bombed 
    now that we did that guy's dirty work…"
    return
label Chap2_MentionKaito:
    # + Affection (Kaito)
    call ksLoveIncrease from _call_ksLoveIncrease_11
    call loveNotification from _call_loveNotification_55
    p "I'm just hoping that jerk loses his grudge by then…"
    return
label Chap2_MentionIdol:
    # + Affection (SB)
    call sbLoveIncrease from _call_sbLoveIncrease_20
    call loveNotification from _call_loveNotification_56
    p "I just need a body to take to that damn concert…"
    return