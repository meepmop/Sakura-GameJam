label Protologue:
    # establish identity
    ############################################################
    # put the name of the character
    $ targetPerson = 0
    $ specifiedName = playerName
    call InsertName
    $ playerName = userInput
    # name has been established
    call ChoosePronoun
    call ConfirmIdentity
    ############################################################
    # game actually starts
    # *Open with a black screen, and soft, hopeful music playing.*
    $ renpy.music.play("audio/Music/DayBegins_Intro.ogg", fadein=1.0)
    $ renpy.music.queue("audio/Music/DayBegins_Loop.ogg", clear_queue=False,loop=True)
    p "It seems like this year's bloom will be even better than the last."
    p "{i}Sigh{/i}"
    
    scene BG YYFront with Fade(0.0,0.0,1.0)
    # *The screen slowly fades into YuraYura's infamous cherry blossom tree.*
    
    "While this marks only my second year at YuraYura Academy, it will also serve 
    as my 21st anniversary of being officially maidenless."
    "Or…in plain terms: lacking a partner."
    "I was never really interested in the whole \"dating\" thing." 
    "It honestly never seemed like a big deal to me."
    "At first, while my family approved of my partnerless lifestyle, it seems as though with a flip of a switch they've gone from \"Focus on your studies!\" 
    to \"Have you found someone who could give us grandchildren yet?\""
    "First of all, I don't even know why they want someone like me to produce offspring."
    "If they took just one look at my spending habits, they'd realize there'd be 
    no room for a mini-me anywhere in that equation."
    "Though, of course I couldn't tell my dear mom about that. That'd have to be a conversation for another day."
    "Speaking of days, I've spent the majority of it just waiting here."
    "Waiting...{w} Waiting..."
    "Sitting here in the hopes that the person my mom told me about would just 
    show the hell up already."
    p "It's no wonder everyone's acting all lovey dovey."
    p "Holding hands, sharing boba…"
    p "If it weren't for the fact mom didn't promise me front row tickets to that 
    virtual idol concert, I'd honestly be none the wiser."
    
    # *A small icon of MCs phone with a virtual idol game appears briefly.*
    show IT PlayerPhone at centerMiddle with easeinbottom

    p "Who even needs love anyways when I already have it at the touch of my fingertips?"
    p "Ah~ My beloveds~"
    p "Don't worry. Your Producer will be with you all soon enough~"
    
    # get rid of the phone
    hide ITPlayerPhone

    p "...{w}..."
    p "At least…I hope so."
    p "If the guy mom set up for me hasn't shown up in the last 5 hours, I doubt 
    they're gonna–"
    
    play sound "audio/branch-shake.mp3"
    stop music fadeout 1.0
    # add a little shake
    scene BG YYFront with hpunch
    
    p "?!?!"
    # *The music cuts off and a loud thud plays while the screen goes black.*
    play sound "audio/body-fall.mp3"
    scene black with hpunch
    sb "Ow, ow, ow..!!"
    # *A shuffling sound effect plays, and the screen fades back into the image of sbwith their hair down looking all baby girl.*
    scene BG YYFront
    show sb annoyed
    with Fade(0.0,0.0,1.0)
    $ renpy.music.play("audio/Music/Sakura_Intro.ogg", fadein=1.0)
    $ renpy.music.queue("audio/Music/Sakura_Loop.ogg", clear_queue=False,loop=True)
    ############################################################
    menu MyHead:
        sb "My head..."
        "Stay Quiet":
            call Proto_StayQuiet
        "Ask if they're okay":
            call Proto_TheyOk
        "Insult them":
            call Proto_Insult
    ############################################################
    sb "Uhm..anyways!"
    # *Depending on the choice made, SB will have their face in the CG image change from ^-^ to a more ^-^;;; expression.*
    # if specific choice is chosen to trigger different emote
    if sbTrig == True:
        show sb neutral
    else:
        show sb neutral
    sb "It is uh, nice to...meet you? Haha~"
    ############################################################
    menu WhoSent:
        sb "It is uh, nice to...meet you? Haha~"
        "Ask if they're the person your mom sent":
            show sb neutral
            call Proto_MomSent
        "Why are you late?":
            show sb neutral
            call Proto_WhyLate

    ############################################################
    show sb neutral

    sb "Though, if it's already this late…that so-called other person must be a real 
    jerk to have left a beautiful flower alone to wilt away into the night."
    sb "Tell me, what even was their name anyways?"
    ############################################################
    # naming the sakura boy
    ############################################################
    # put the name of the character
    $ targetPerson = 1
    $ specifiedName = "Sakura"
    call InsertName
    # name has been established
    ############################################################
    show sb thinking
    sb "Hmm…"
    sb "Hmmmm…"
    p "..?"
    # delayed name change
    $ sakuraName = userInput

    # *A picture of Sakura Boi taking MC's hands into their own all excited “:D" appears.*
    show sb neutral
    sb "While I am not a fan of outright abandonment, that sounds like quite the 
    exquisite name!"
    p "Eh?!?!"
    show sb neutral
    p "Don't you have a name of your own?! Don't go taking other people's–!"
    sb "How am I to take what never even bothered to show up in the first place~?"

    show sb neutral

    sb "If anything, consider it that person's 'tax' for failing to accompany you."
    sb "Besides~ It's not like I could come up with a name of my own."
    sb "It seems that fall did quite the number on my memories~"

    show sb neutral

    p "Okay. Maybe we should actually get you to a hospital–"
    show sb neutral
    sb "Nonsense! While I may lack my memories, I just know that it must be fate 
    that we met this way" 
    show sb thinking
    sb "uhm… What's your name again?"
    p "...[p]"
    show sb neutral
    sb "Simply Divine. [p].~ I will cherish that name for the rest of my days."
    show sb excited
    sb "Tell me, will you help recover my lost memories?"
    sb "If you do, you have my word that those concert tickets will be ours~!"
    ############################################################
    menu ConcertTicket:
        sb "If you do, you have my word that those concert tickets will be ours~!"
        "This is ridiculous–":
            show sb neutral
            call Proto_Ridiculous
        "No.":
            # game ends prematurely
            jump Proto_No
    ############################################################
    call situTriggerReset
    $ quick_menu = False
    window auto hide
    scene black with fade
    stop music fadeout 1.5
    pause 2.0
    jump Chapter1
    return
