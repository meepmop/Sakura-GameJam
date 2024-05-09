############################################################
# familiarSakura
############################################################
label Chap1_Familiar:
    call sbLoveIncrease from _call_sbLoveIncrease
    call loveNotification from _call_loveNotification
    p "It’s strange."
    p "The more I look. The more they seem to remind me of…"
    return
label Chap1_FocusPhone:
    "Paying little mind to the beautiful change of seasons which is taking place before you, 
    you decide to instead focus your attention towards the  fictional men on your smartphone."
    "To you, they’re all a symbol of divine perfection."
    "No faults. Just smiles and laughter." 
    "Well…all except–"
    return
############################################################
# Our classes?
############################################################
label Chap1_OurClasses:
    call sbLoveDecrease from _call_sbLoveDecrease
    call loveNotification from _call_loveNotification_1
    p "What do you mean our classes?"
    p "Didn’t you say something about not having any memories or anything?"
    "You can’t help but glance off to the side with a huff."
    p "Honestly. If you keep this up, I’m gonna call the cops."
    sb "Oh, come now."
    sb "If I get arrested, who else will I share these cookies with?!"

    return
label Chap1_YourMemories:
    p "Don’t we need to try and figure out what went wrong with your head?"
    p "If this is some form of prank, I’m surprised you’ve kept up with it for this long."
    sb "I can promise you, I’m just as brainless as I was last Friday~"
    "Right as [sb] says this, they hold up the bag of cookies which they’ve managed to obtain."
    sb "In fact, the kind older lady down the street felt so bad seeing me asleep on that bench 
    the past few nights, that she brought me these sweets~!"

    return
label Chap1_BranchHair:
    call sbLoveIncrease from _call_sbLoveIncrease_1
    call loveNotification from _call_loveNotification_2
    p "I almost regret asking this, but, is that an entire branch in your hair?"
    sb "Why, yes it is."
    "You instantly notice the almost prideful tone [sb] takes upon answering."
    "Their eyes glisten with joy, and they nearly drop the cookies which they were 
    holding from their sudden burst of excitement."
    p "...can I ask…why?"
    sb "Well, you see. The sweet old lady who gave me these cookies said I looked much more handsome with my hair tied back."
    sb "And how could I refuse after her incredible act of kindness?"
    sb "After all, we wouldn’t have these cookies to share were it not for her~"

    return
############################################################
# Where's Waldo/Sakuraboy?
############################################################
label Chap1_SearchChoice:
    menu whereTheyGo:
        "Knowing there’s only so many places they could be, you decide the following:"
        "Check the nearby classrooms.":
            # reset any trigs used
            call situTriggerReset from _call_situTriggerReset_1
            jump Chapter1_Cont_NearbyClass
        # player can only check the supply closet once
        "Check the supply closet" if not choice1Chosen:
            jump Chap1_SuppyCloset
        # game will end here if they choose this
        "Cut your losses and just leave.":
            jump Chap1_JustLeave
    return
label Chap1_SuppyCloset:
    $ choice1Chosen = True 
    "Figuring that perhaps there would be some spare decorations inside, you make your way to the supply closet located at the end of the hall."
    "You’re surprised to see how upon arrival, it was already torn through in a way which you could hardly imagine [sb] doing."
    "You frown, seeing the replica sakura petals so carelessly dirtied and stepped upon."
    "You also can’t help but spot the powered white streaks which coat areas of the now ruined decorations."
    "Surely someone was going to get in trouble for this."
    "Cutting your losses, you decide to try checking out the nearby classrooms for any signs of [sb]."
    jump Chap1_SearchChoice
label Chap1_JustLeave:
    "Seeing the absurdity beginning to start up once more, you let out a tired sigh and take out your phone."
    "There seems to be a new event about to start."
    "One which seemed far more interesting than whatever the Hell was taking place here."
    "You decide to walk in the direction opposite to [sb], letting fate take its course."
    "It wasn't your problem anyways."
    return
############################################################
# tellMeFiend
############################################################
label Chap1_Scream:
    call ahLoveIncrease from _call_ahLoveIncrease
    call loveNotification from _call_loveNotification_3
    p "What the Hell!? G-Get your hands off of me!!"
    "Amari's lips seem to curl into a full on grin at your discontent."

    show ah vhappy

    "He laughs, gripping onto your hands with an even more firm grip than before."
    ah "Yes! Scream for me! Sing out your woes in the form of absolute fear for which 
    shall serve as your divine punishment!!"
    
    return
label Chap1_YankHand:
    show ks neutral
    p "I don’t have time for this."
    "You scowl as you forcibly yank your hands away."
    "Looking beyond displeased with this display of dramatics, you focus your 
    gaze onto the man behind him."
    "Judging by how said guy’s fists were clenched, you could tell that he felt similar."

    return
label Chap1_StayStill:
    call ahLoveDecrease from _call_ahLoveDecrease
    call loveNotification from _call_loveNotification_4
    "You remain still as a statue."
    show ah neutral
    "Unmoving, you can only lazily direct your gaze to the equally unimpressed man behind them."
    "It’s almost as if by locking eye contact, you both seem to ask if Amari had 
    finished with their antics."

    return
############################################################
# excuseMePathethic
############################################################
label Chap1_Pathetic:
    # Amari liked that
    call ahLoveIncrease from _call_ahLoveIncrease_1
    call loveNotification from _call_loveNotification_5
    p "Who’re you calling pathetic?!"
    "You feel a mix of embarrassment and rage swell up in your chest."
    "You don’t know why, but for some reason just looking at this guy 
    makes you wish you made the move to punch him."
    show ks thinking

    ks "Need I repeat myself?"
    ks "You’re a nobody. So, why don’t you just go back to being the wallflower you were with that stupid Idol game of yours?"
    p "...okay how do you know about–"
    ks "We’ve more important matters to tend to."

    show ks neutral

    "Despite having his face covered, you can practically feel the man’s scowl."
    "It seems as it stood, you were the least of his priorities."

    return
label Chap1_IllShowYou:
    # kaito did not like that
    call ksLoveDecrease from _call_ksLoveDecrease
    call loveNotification from _call_loveNotification_6
    "Deciding not to let this insult stand, you find yourself rolling up one of your sleeves."
    "After all, a little well earned violence never hurt no one."
    p "Oh yeah? I’ll show you pathetic..!"
    show ks oh
    ks "?!?!"
    "Winding your arm back, you’re prepared to give Kaito a good hit to the face."
    "However, right before you connect with the cloth layer above it, you’re met 
    with a well-timed block."
    show ah twt
    ah "Unfortunately, Kaito-Kun can only be harmed by one person."
    ah "And they’d be rather upset if I allowed it to be you~"

    return
label Chap1_WellActually:
    # kaito liked that
    call ksLoveIncrease from _call_ksLoveIncrease
    # amari did not like that
    call ahLoveDecrease from _call_ahLoveDecrease_1
    call loveNotification from _call_loveNotification_7
    "Feeling yourself deflate, you hang your head low at the other’s insults."
    "Doing so, out of the corner of your eye, you catch the slight creasing of Kaito’s eyes."
    show ah bored
    "However, Amari appears less than pleased."
    ah "How dull."
    ah "I’d have at least appreciated a show of expression."
    ks "I rather like it when someone knows when to keep their mouth shut~"

    return
############################################################
# whatJustHappened
############################################################
label Chap1_WhoThatGuy:
    # - Affection Kaito + Affection (Amari) 
    call ksLoveDecrease from _call_ksLoveDecrease_1
    call ahLoveIncrease from _call_ahLoveIncrease_2
    call loveNotification from _call_loveNotification_8
    p "Uh. Can I ask who this guy even is?"
    "As soon as the question leaves your lips, you instantly feel Kaito’s growing animosity."
    
    show ks angry

    p "I just can’t win today, can I…"
    ks "They’re a menace, that’s who they are!"
    ks "Who would even waste such good flour in the first place?!"
    
    show ah owo

    ah "Now, now. Just because you and your little ‘partner’  had a falling out, 
    doesn’t mean you have to take it out on poor little [p] here~"
    ks "W-We were not–"

    return
label Chap1_IsThatFlour:
    # ~ Affection (Kaito) - Affection (Amari)
    call ahLoveDecrease from _call_ahLoveDecrease_2
    call loveNotification from _call_loveNotification_9
    p "That white stuff. Is that..?"
    show ks sad
    ks "Perfectly good flour."
    show ah twt
    ah "And about a few kilos worth too~"
    p "Why’d someone even do such a thing?"
    show ah bored
    ah "Is it not obvious? They’re simply dying for attention."

    return
label Chap1_RemainQuiet:
    # + Affection (Kaito) ~ Affection (Amari)
    call ksLoveIncrease from _call_ksLoveIncrease_1
    call loveNotification from _call_loveNotification_10
    "You decide to keep your mouth shut and instead mentally investigate 
    the scene taking place before you."
    "Judging from how the room was practically white, it seems as though someone had a 
    blast just throwing the stuff everywhere."
    ks "If it means anything. I appreciate your silence."
    ks "With how frequently this has been happening, I can’t afford any more distractions."

    return
############################################################
# turnToTheVoice
############################################################
label Chap1_IgnoreVoice:
    # - Affection (SB)
    call sbLoveDecrease from _call_sbLoveDecrease_1
    call loveNotification from _call_loveNotification_11
    "Fixated on the sheer chaos that has been the past couple of days, 
    you barely pay mind to your surroundings."
    "In fact, you can feel quite the headache coming on."
    "It irritates you to the point that when you finally decide to direct your 
    attention towards the source of said voice, your face is ice cold."
    show sb happy
    $ renpy.music.play("audio/Music/Sakura_Intro.ogg", fadein=1.0)
    $ renpy.music.queue("audio/Music/Sakura_Loop.ogg", clear_queue=False,loop=True,fadein=1.0)
    sb "[p]?? It’s me– I…just wanted to check back in with you, haha~"

    return
label Chap1_TurnHead:
    # + Affection (SB)
    call sbLoveIncrease from _call_sbLoveIncrease_2
    call loveNotification from _call_loveNotification_12
    "Despite how utterly crazy these last few days have been, you figure it 
    can’t possibly get any worse and begrudgingly turn towards the source of the voice."
    $ renpy.music.play("audio/Music/Sakura_Intro.ogg", fadein=1.0)
    $ renpy.music.queue("audio/Music/Sakura_Loop.ogg", clear_queue=False,loop=True,fadein=1.0)
    show sb neutral
    sb "Are you alright..?"
    show sb happy
    sb "You know, once I’d ran off…I realized I’d forgotten my new companion, haha~"

    return
############################################################
# newCharacter
############################################################
label Chap1_WhoHellYou:
    # + Affection (Mikael)
    call maLoveIncrease from _call_maLoveIncrease
    call loveNotification from _call_loveNotification_13
    p "Who the Hell are you?!"
    p "Don’t tell me you’re with the masked guy!"
    p "I’m not looking to get my character insulted twice in one day!!"
    "It’s as if the sudden burst of emotion ignites a spark of sheer joy within the 
    mysterious man’s eyes."
    "Their lips part into a wide grin, and they pull [sb] close into their embrace."
    "Now resting their chin against [sb]'s shoulder blade, both you and them can feel as 
    though that despite the other’s excitement, it’d be best not to get on their bad side."
    show ma vhappy
    jd "Who the Hell am I?"

    $ m_name = 'Mikael'

    ma "Why, I’m the one and Mikael Amoris! Current President of YuraYura’s Baking Club as 
    well as the one and only flour bomber~"
    return
label Chap1_NotAnother:
    # ~ Affection (Mikael)
    p "How many more people are gonna just randomly appear today?"
    "You can visibly see the man before you’s face twitch from discontent."
    jd "You know…"
    "Their lips part into a wide grin, and they pull [sb] close into their embrace."
    "It causes both you and [sb] to further tense, and part of you wishes you 
    hadn’t spoken up at all."
    "Now resting their chin against [sb]'s shoulder blade, both of you can only wait to see 
    what this lunatic’s next moves were."
    show ma vhappy
    ma "If anyone were to appear before you, you’d best be glad that it was YuraYura’s very own 
    Mikael Amoris, current President of the infamous Baking Club~"

    return
label Chap1_IDoneDay:
    # - Affection (Mikael) - (SB)
    call maLoveDecrease from _call_maLoveDecrease
    call sbLoveDecrease from _call_sbLoveDecrease_2
    call loveNotification from _call_loveNotification_14
    p "I think I’ve had enough."
    show sb ouch
    "About to turn on your heels and leave this mess of a day behind, you can see [sb]'s eyes glisten."
    "It was almost as if they had asked you not to leave."
    "Not like that mattered to you anyways."
    jd "Ya know, maybe you and Sakuraba ain’t so different after all."
    "Now pulling [sb] closer to him, the mysterious man opts to rest their face against 
    his prey’s shoulder blade."
    show ma vhappy
    ma "Be careful abandoning your friends, lest I, Mikael Amoris, current President of the 
    infamous Baking Club, set you as my next target!"

    return
############################################################
# littleHelp
############################################################
label Chap1_OfferAssist:
    # + Affection (SB)
    call sbLoveIncrease from _call_sbLoveIncrease_3
    call loveNotification from _call_loveNotification_15
    p "Would you mind letting go of my friend here?"
    "You instantly notice how [sb]'s face lights up at your acceptance of your friendship."
    "However, before they can say anything to further embarrass you, Mikael reluctantly 
    releases their grip with a huff."

    return
label Chap1_Shrug:
    # - Affection (SB)
    call sbLoveDecrease from _call_sbLoveDecrease_3
    call loveNotification from _call_loveNotification_16
    "You shrug."
    "Not knowing what exactly to do, you watch helplessly as Mikael further interrogates your 
    so-called companion."
    "However, after a few more minutes of this, Mikael decides that they’ve had their 
    fill, and opts to free [sb] with a disgruntled huff."

    return
label Chap1_PraiseMikael:
    # + Affection (Mikael)
    call maLoveIncrease from _call_maLoveIncrease_1
    call loveNotification from _call_loveNotification_17
    p "If it means anything…I understood you perfectly."
    p "Were it not for your accent, I’d have thought it was your native language."
    "Instantly, you can see Mikael’s expression brighten as he almost excitedly 
    releases [sb] from his grip."

    return
############################################################
# clearThroatDecide
############################################################
label Chap1_Sakuraba:
    # + Affection (Mikael)
    call maLoveIncrease from _call_maLoveIncrease_2
    call loveNotification from _call_loveNotification_18
    p "It sounds like you and that Sakuraba guy don’t really get along."
    p "Did he make you drop your ice cream too?"
    "Mikael reaches to scratch at the back of his head."
    "It appears as though despite the frown which paints his lips, his eyes 
    hold a story which only he could tell."
    ma "Sakuraba. Or, as that theater chick usually calls him, Kaito."
    ma "Let’s just say we’ve got history."
    ma "I wouldn’t be wastin’ all that flour if we didn’t."
    ma "Though~ I ain’t wanna trouble you with all that."
    return
label Chap1_BeCleaning:
    # - Affection (Mikael) + Affection (Kaito)
    call maLoveDecrease from _call_maLoveDecrease_1
    call ksLoveIncrease from _call_ksLoveIncrease_2
    call loveNotification from _call_loveNotification_19
    p "If you’re the one responsible for this, shouldn’t you be the one to clean it up?"
    p "You know, I can bet the custodial staff aren't too thrilled either."
    p "Surely if you’ve got some sort of grudge, it can be held without involving others in 
    your dirty work."
    ma "Oh C’mon! Surely a little flour never hurt no one."
    "While Mikael takes a more confident tone, you can see his body language shift in a way 
    that makes him seem less confident."
    ma "But…I guess I’ll help clean. At least this classroom, that is."

    return
label Chap1_Cookies:
    # + Affection (SB)
    call sbLoveIncrease from _call_sbLoveIncrease_4
    call loveNotification from _call_loveNotification_20
    show sb ouch
    p "What ever happened to those Sakura cookies, [sb]?"
    "Just as you ask this, you see [sb]'s face darken, and you are met with a rather sheepish smile."
    sb "I…uh…traded them for that ice cream~"
    sb "Though, I guess that’s out the window now, huh?"
    show ma vhappy
    ma "My offer still stands, ya know!"

    return
############################################################
# almostUnnerving
############################################################
label Chap1_RemainQuietAgain:
    # + Affection (SB)
    call sbLoveIncrease from _call_sbLoveIncrease_5
    call loveNotification from _call_loveNotification_21
    "Seemingly lost in the thought of the other’s rather large hands, 
    you’re unable to catch their question."
    "You blink. Once. Twice."
    "Trying to recall what they said, you’re about to shamefully ask Mikael to repeat himself."
    sb "Oh, I can answer this~ [pCon] [p]!"
    sb "[pCon] helping me recover my memories~"
    return
label Chap1_IntroduceSelf:
    # ~ Affection (Mikael)
    "Looking less than thrilled, you reach out to shake Mikael’s hand."
    "It’s warm."
    "So much so that you nearly stumble over your bland introduction."
    p "[p]..."
    p "I’m…[p]."
    ma "Oh wow…you really are a wallflower!"
    return
label Chap1_IntroduceSelfWithConfidence:
    # + Affection (Mikael, Amari)
    call ahLoveIncrease from _call_ahLoveIncrease_3
    call maLoveIncrease from _call_maLoveIncrease_3
    call loveNotification from _call_loveNotification_22
    "Figuring you’d try and take a page from Amari’s book, you steady yourself."
    "Briefly closing your eyes, you snap them open once more with a cheesy at best 
    grin and clasp Mikael’s hand into your own."
    p "I am [p]! And I am not a wallflower!!!"
    ma "That’s the spirit!!!"
    return
############################################################
# michaelTenses
############################################################
label Chap1_WhatAboutHim:
    # - Affection (Mikael)
    call maLoveDecrease from _call_maLoveDecrease_2
    call loveNotification from _call_loveNotification_23
    p "You..?"
    "You’re met with a heavy sigh from the redhead before you."
    ma "It’s nothin’."
    ma "Just, stupid memories, I guess."
    ma "Two idiots doin’ idiot things."
    return
label Chap1_SwitchSubject:
    # + Affection (Mikael) + Affection (SB)
    call maLoveIncrease from _call_maLoveIncrease_4
    call sbLoveIncrease from _call_sbLoveIncrease_6
    call loveNotification from _call_loveNotification_24
    "You fumble with your phone, awkwardly pulling up your idol game to show 
    off one of your virtual ‘husbandos’."
    "They look strikingly similar to Kaito."
    p "Do you mean..?"
    sb "Oh~ He’s rather pretty."
    sb "He even has the serious look down~"
    "Mikael huffs out a small laugh at the forced change in conversation."
    "However, the gesture does not go unappreciated."
    ma "Not bad~"
    ma "I can see why you’re such a wallflower around here."
    ma "Especially if you’re constantly lookin’ at virtual men like that."
    return
############################################################
# whatDoYouNeedInReturn
############################################################
label Chap1_AbsolutelyNo:
    # - Affection (Mikael) + Affection (Kaito)
    call maLoveDecrease from _call_maLoveDecrease_3
    call ksLoveIncrease from _call_ksLoveIncrease_3
    call loveNotification from _call_loveNotification_25
    p "Listen. As much as I appreciate just how unbelievable these past few days have been…"
    p "I’m pretty sure teaming up with the infamous Flour Bomber will make getting [sb]'s 
    memories back even more difficult."
    p "Besides, no one here even cared about who I was prior to their existence."
    ma "Hey!"
    ma "It’s not my fault that you decided to be a wallflower up until this point~"
    "[sb] can be seen trying to hold back their laughter at the frequent comparison."
    return
label Chap1_AndThatIs:
    # + Affection (Mikael) + Affection (SB)
    call maLoveIncrease from _call_maLoveIncrease_5
    call sbLoveIncrease from _call_sbLoveIncrease_7
    call loveNotification from _call_loveNotification_26
    p "You’re not gonna make us flour someone, are you?"
    "Mikael lets out a hearty laugh at the assumption."
    "They seem to say something which you cannot fully comprehend."
    "However, as someone with a grand total of 1 year of elementary English Skills, you assume 
    it was something along the lines of \"Kitten.\""
    return
