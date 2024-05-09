label Chapter1:
    show text "Day: Monday\n\nSetting: Streets of Tokyo leading towards YuraYura Academy\n\nTime:Morning" with dissolve
    pause 3.0
    hide text with dissolve
    
    # *There would be casual/’lighthearted’ musical beats happening here.*
    $ renpy.music.play("audio/Music/DayBegins_Intro.ogg", fadein=1.0)
    $ renpy.music.queue("audio/Music/DayBegins_Loop.ogg", clear_queue=False,loop=True,fadein=1.0)
    scene BG YYFront with fade
    "The weekend passes by just as quickly as it came."
    ############################################################
    menu familiarSakura:
        "As Cherry Blossoms continue to litter the streets with their iconic Sakura Pink hue, you can’t help but admire their beauty."
        "The petals remind me of…":
            call Chap1_Familiar
        "Focus your attention back to your phone.":
            call Chap1_FocusPhone
    ############################################################
    sb "Oiii~ [p]!"
    sb "Oi, Oiiiii! Over here~!"
    "You quickly shift your gaze towards the direction which the voice is coming from.
    However, you can’t help but feel your brow twitch at the display."
    scene CG C1 sbrunning
    # *Insert Picture of [sb] waving with their hair now tied up, a 
    # cherry blossom tree branch sticking out to neatly keep it in place. 
    # They seem to be holding a small clear bag of cherry blossom infused 
    # cookies in their free hand. A mix of people/businessmen are clearly 
    # trying to get past them.*
    sb "You finally looked my way~"
    sb "Are you ready for our classes?"
    ############################################################
    menu ourClasses:
        sb "Are you ready for our classes?"
        "Our?":
            call Chap1_OurClasses
        "What about your memories?":
            call Chap1_YourMemories
        "Is that a branch in your hair?":
            call Chap1_BranchHair
    ############################################################
    "After [sb]’s mention of cookies, you decide to walk past them and in the 
    direction of YuraYura Academy."
    "They eagerly follow, face alit with an unmatchable passion."
    "Part of you honestly couldn’t believe you were even in this situation in the first place."
    "However, as your mom always would say. Everything happens for a reason."
    "And if you wanted to attend that Idol Concert, you had to accept it."
    # *The scene transitions to the inside of one of the class buildings of YuraYura. 
    scene BG YYInside
    # There seems to be signs of the upcoming cherry blossom festival everywhere, 
    # ranging from posters in the background to decorative flowers hung up all 
    # around the hall.*
    show sb neutral

    p "Here we are."
    p "This is where we’ll start, I guess."

    show sb oh

    sb "Woooow~! How pretty..~!"
    sb "It’s as though nature itself has reflected itself in this very hallway..!"

    show sb happy

    sb "I simply must see more of it!!"
    p "We can but–"

    hide sb

    "Before you can properly finish your sentence, [sb] takes it upon themselves 
    to go ahead and rush ahead of you."
    "It isn’t long before you lose sight of them and their noises of pure excitement 
    become muffled in the crowd of students making their way to their next class."
    p "I can’t believe this."
    p "I’m beginning to question whether or not I really want those Idol tickets."
    p "I mean…maybe I can bribe someone else from the Anime Club to just pretend to be my partner…"
    p "Though last I heard. They’ve all been hauled off somewhere binge watching Two Piece."
    p "I probably won’t see any of them until at least next Semester…"
    "Cutting your losses, you decide to follow in [sb]'s trail."
    "Knowing there’s only so many places they could be, you decide the following:"
    ############################################################
    # will jump to a search choice in the choices script and return back when chosen correctly
    jump Chap1_SearchChoice
    ############################################################

# had to break it in two so I can go back to the Search Choice and end the game prematurely
label Chapter1_Cont_NearbyClass:
    "Recalling that your friend’s class had planned to rehearse some aspects of 
    Friday’s festival, you decide to see if [sb] would be naturally drawn to its 
    alluring presence."
    "You quickly make your way through the hallways, passing by many groups of 
    lovers in the process."
    "More hand holding. More Boba. More cheesy words of adoration."
    "How did love come so easy to these people?"
    "Why couldn’t it be that way for you?"
    "It honestly makes your chest tighten."
    # *The Scene now changes to that of a traditional Japanese Classroom. 
    scene BG Classroom
    # It holds hints of the upcoming festival within it.*
    show ah neutral at left:
        xzoom -1.0
    show ks angry at right
    with dissolve

    ks "Unbelievable!!"
    p "Huh–"
    ks "When I get my hands on him..!"

    show ah happy

    ah "Oho~ Kaito-Kun~ I can practically see your hair graying by the second! Please, calm yourself~"

    $ k_name = 'Kaito'

    ks "You’re not helping."
    
    show ah owo

    ah "Ah~ Would you rather me join in your rage?"

    show ah twt

    $ a_name = 'Amari'

    ah "Ahem. I, Haruka Amari, shall swear vengeance on the one foolish enough to oppose YuraYura’s student council!"
    
    "Before you’ve the chance to leave, you find yourself cornered by the louder of the two people."
    
    show ah shine
    show ks shine

    "Their eyes glisten with a manic fire as they firmly take your hands into their own."

    show ah twt

    ah "You!!"
    ah "Tell me, have you seen the fiend responsible for this tragedy!?!"
    ############################################################
    menu tellMeFiend:
        ah "Tell me, have you seen the fiend responsible for this tragedy!?!"
        "Scream":
            call Chap1_Scream
        "Yank your hands away":
            call Chap1_YankHand
        "Remain still":
            call Chap1_StayStill
    ############################################################
    show ks neutral
    ks "Enough."
    # *A CG of both Amari and Kaito standing side by side appears. Kaito looks less than impressed while Amari is seen striking a pose.*
    # *Kaito’s theme will now play.*
    call Music_ksTheme
    show ah owo
    ah "Aww...you’re no fun~!"
    "Now moving back to Kaito’s side, Amari strikes a pose."
    "Or rather…a few poses. Much to Kaito’s displeasure."
    ks "It’s obvious that [pSub] got nothing to do with him."
    ks "I mean…just look at how utterly clueless [pSub] seem."
    ks "In fact, if I recall correctly, [pPosAd] files mention that outside of classes, 
    they’ve hardly any involvement in the student-life here."
    ks "Pathetic."
    ############################################################
    menu excuseMePathethic:
        ks "Pathetic."
        "Pathetic?!":
            call Chap1_Pathetic
        "I’ll show you pathetic..!":
            call Chap1_IllShowYou
        "Well actually…":
            call Chap1_WellActually
    ############################################################
    "Taking the time to adjust his vest, Kaito makes his way towards the 
    opposite end of the classroom."

    show ks sad
    
    "Running his fingers across the powdered white substance which coats the 
    desk in front of him, you notice the glint of sorrow which lingers behind his mask."
    ks "There’s no doubt about it. This is his work."
    
    show ah neutral
    
    ah "Gone just as quickly as they came too, no?"
    ah "A true master of stealth~"
    
    show ks angry

    ks "You mean a true pain in the ass."
    
    show ks neutral

    ks "Though…it’s rather strange."
    ks "Typically they opt to target one of our councilmen and not some 
    obscure classroom."
    ############################################################
    menu whatJustHappened:
        ks "Typically they opt to target one of our councilmen and not some 
        obscure classroom."
        "Who is this guy?":
            call Chap1_WhoThatGuy
        "Is that…flour?":
            call Chap1_IsThatFlour
        "Remain Quiet":
            call Chap1_RemainQuiet
    ############################################################
    show ks neutral
    show ah neutral

    "Suddenly, before another word can be spoken, a loud scream can be 
    heard coming from outside of the classroom."
    sta "HELP ME! PRESIDENT-SAMA!! IT’S EVERYWHERE!!!!"
    stb "The flour bomber is back again! Run!!"
    stc "My eyes!! They’re so dry!!!!"
    show ks oh
    ks "..!"
    ks "Mikael!!!"
    hide ks
    "Without skipping a beat, Kaito can be seen bolting out of the area."
    ks "Out of my way!"
    # *Some clattering sound effects could be heard*
    ks "I said MOVE!"
    show ah owo
    stop music fadeout 1.0
    ah "Oh dear…there he goes again~"
    ah "I shouldn’t leave poor Kaito-Kun alone too long."
    ah "May we cross paths once more in the near future! My beloved [p]~!"
    hide ah
    "With a dramatic twirl, Amari decides to take their leave, leaving you alone 
    in the room just as, if not, even more confused than when you had entered it."
    "Once finally alone, you can’t help but let out a heavy sigh."
    jd "Um…[p]?"
    ############################################################
    menu turnToTheVoice:
        jd "Um…[p]?"
        "Ignore the voice":
            call Chap1_IgnoreVoice
        "Turn your head":
            call Chap1_TurnHead
    ############################################################
    sb "You know, I had originally planned on giving you this ice cream as a 
    form of apology…"
    sb "However, that rather scary looking guy with the mask went ahead and knocked 
    it right from my hands!"
    sb "Talk about a bummer. Huh..~?"
    jd "If you’d like, I can get you somethin’ even better~"
    sb "Oh. That’d be wonderful~"
    show sb neutral
    "[sb]’s lips curl into a warm smile." 
    show sb oh at left
    show ma happy at right
    "However, following a moment of thought, [sb] quickly tenses, and you can feel 
    your eyes widening."
    ############################################################
    menu newCharacter:
        "However, following a moment of thought, [sb] quickly tenses, and you can feel 
        your eyes widening."
        "Who the hell are you?!":
            call Chap1_WhoHellYou
        "Not another one…":
            call Chap1_NotAnother
        "I think I’m done for the day.":
            call Chap1_IDoneDay
    ############################################################
    # *A CG of Mikael with [SB] in their hold shows up. They both are looking 
    # towards the MC. Mikael appears to be grinning while [SB] looks like they’re currently fearing for their life.*
    # *Mikael’s theme plays.*
    $ renpy.music.play("audio/Music/Mikael2_Intro.ogg", fadein=1.0)
    $ renpy.music.queue("audio/Music/Mikael2_Loop.ogg", clear_queue=False,loop=True,fadein=1.0)
    scene CG C1 mahug with dissolve
    sb "Uhh…is it really necessary to be this close?"
    sb "You know, personal space is a thing."
    p "You’re one to talk."
    sb "W-Well! This is different! I don’t even know this person!"
    ma "What do you mean you don’t know me?!"
    ma "I had just taken the time to give my whole introduction and everythin’!!"
    "Mikael can be seen pouting as he moves to grab at [sb]'s chin and yank it in his direction."
    ma "I. Am. Mikael. Amoris."
    ma "Are you sayin’ my Japanese hasn’t gotten’ better these past few years??"
    sb "W-Well…I would not have known you prior to this exchange–so–"
    "[sb] casts a worried glance your way."
    sb "A little help here?"
    ############################################################
    menu littleHelp:
        sb "A little help here?"
        "Offer Assistance":
            call Chap1_OfferAssist
        "Shrug":
            call Chap1_Shrug
        "Praise Mikael":
            call Chap1_PraiseMikael
    ############################################################
    scene BG Classroom
    show sb oh at left
    show ma happy at right
    with dissolve
    ma "So, about that ice cream~"
    ma "How ‘Bout I whip y’all up some as an apology for Sakuraba’s bitchiness?"
    sb "Doesn’t that require less baking and more, uh, freezing?"
    show ma wink2
    ma "Well. Yeah. But."
    "You visibly notice Mikael fluster."
    "It almost brings a smile to your face."
    "Despite having only just met the man, it was as if his presence alone 
    was enough to shine some positivity on this already hectic morning."
    "Clearing your throat, you decide to ask the following:"
    ############################################################
    menu clearThroatDecide:
        "Clearing your throat, you decide to ask the following:"
        "Who’s Sakuraba?":
            call Chap1_Sakuraba
        "Shouldn’t you be cleaning?":
            call Chap1_BeCleaning
        "Didn’t you just have those cookies?":
            call Chap1_Cookies
    ############################################################
    ma "Hey…now that I think about it."
    ma "I never got your name."
    "Mikael extends his hand out to you."
    "It’s huge in comparison to yours."
    "In fact, you can only compare it to the ‘Yaoi’ hands you see in your idol game."
    "It’s almost unnerving."
    ############################################################
    menu almostUnnerving:
        "It’s almost unnerving."
        "Remain quiet":
            call Chap1_RemainQuietAgain
        "Introduce yourself":
            call Chap1_IntroduceSelf
        "Introduce yourself!!!":
            call Chap1_IntroduceSelfWithConfidence
    ############################################################
    ma "Now, with introductions out the way."
    ma "Would you mind tellin’ me what you two are doin’ here anyways?"
    ma "While I somewhat recognize your face, I know for sure I haven’t seen flower 
    boy over here before."
    "You quickly cast a glance [sb]'s way, taking notice of how embarrassed they look 
    at Mikael’s makeshift 'title'."
    p "Well, apparently they don’t remember who they are."
    "You sigh heavily while pulling out your phone and flashing it Mikael’s way."
    "On it, it shows your interpretation of what’s happened so far."
    "You figured it’d be best to write it all down in the event someone called you crazy."
    "However, judging from how the man before you was scratching their chin, you 
    feared that still might be the case."
    ma "So you’re sayin’ they just fell from some tree?!"
    ma "Talk about cool!!"
    sb "It was rather painful, you see~"
    ma "Oh, I bet!"
    ma "You see, one time Kaito ‘n I–"
    "You quickly see Mikael’s body tense as he cuts himself off mid sentence."
    ############################################################
    menu michaelTenses:
        "You quickly see Mikael’s body tense as he cuts himself off mid sentence."
        "What about him":
            call Chap1_WhatAboutHim
        "Switch Subjects":
            call Chap1_SwitchSubject
    ############################################################
    "After a few moments of prolonged silence, [sb] decides to break it by stepping 
    in between both yourself and Mikael."
    "Now clasping their hands together, you feel as though that they were about to 
    turn this supposedly one off interaction into a recurring occurrence."
    sb "Say…Mikael."
    ma "That’s my name~"
    sb "You know…"
    sb "Despite your hand in wreaking havoc in this school, I feel as though I can 
    trust you."
    sb "Those eyes of yours, I can sense the lingering sorrow behind them."
    sb "You’re seeking answers as well."
    sb "That's why you’ve taken up the mantle of being YuraYura’s ‘Flour Bomber’, yes?"
    p "?!?!"
    p "You can’t just go saying stuff like that!"
    p "What if he targets us next?!"
    p "You’ll never get your memories back if I have to send you to the damn hospital–!"
    ma "Heh. I knew I knew somethin’ was off about ya."
    "Mikael cards his fingers through his hair."
    "Shaking his head, you can tell that the redhead was more impressed if anything 
    that someone had called him out on his feelings."
    ma "Yeah. I want answers."
    ma "In fact, I want lots more than that."
    ma "That bastard of a President didn’t always make me wanna punch his face in."
    ma "But, that’s a story for another day~"
    ma "Tell ya what."
    ma "From now on, whatever weird memory thing y'all got goin’. I’m gonna help!"
    ma "Though…I’ll need somethin’ in turn~"
    ############################################################
    menu whatDoYouNeedInReturn:
        ma "Though…I’ll need somethin’ in turn~"
        "Absolutely not":
            call Chap1_AbsolutelyNo
        "And that is…?":
            call Chap1_AndThatIs
    ############################################################
    ma "Of course not~"
    ma "All I ask, is that you keep Sakuraba busy until Friday’s festival."
    scene black
    call situTriggerReset
    stop music fadeout 1.0
    jump Chapter2
    return