label Protologue:
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
    # *Open with a black screen, and soft, hopeful music playing.*
    p "It seems like this year's bloom will be even better than the last."
    p "{i}Sigh{/i}"

    # *The screen slowly fades into YuraYura's infamous cherry blossom tree.*
    "While this marks only my second year at YuraYura Academy, it will also serve 
    as my 21st anniversary of being officially maidenless."
    "Or…in plain terms. Lacking a Partner."
    "I was never really interested in the whole 'Dating' thing." 
    "It honestly never seemed like a big deal to me."
    "At first, while my family approved of my partnerless lifestyle, it seems 
    as though with a flip of a switch they've gone from 'Focus on your studies!' 
    to 'Have you found someone who could give us grandchildren yet?' "
    "First of all, I don't even know why they want someone like me to produce offspring."
    "If they took just one look at my spending habits, they'd realize there'd be 
    no room for a mini-me anywhere in that equation."
    "Though, of course I couldn't tell my dear mom about that. That'd have to be 
    a conversation for another day."
    "Speaking of days, I've spent the majority of it just waiting here."
    "Waiting…{w} Waiting…"
    "Sitting here in the hopes that the person my mom told me about would just 
    show the hell up already."
    p "It's no wonder everyone's acting all lovey dovey."
    p "Holding hands, sharing Boba…"
    p "If it weren't for the fact mom didn't promise me front row tickets to that 
    virtual idol concert, I'd honestly be none the wiser."
    # *A small icon of MCs phone with a virtual idol game appears briefly.*
    p "Who even needs love anyways when I already have it at the touch of my fingertips?"
    p "Ah~ My beloveds~"
    p "Don't worry. Your Producer will be with you all soon enough~"
    p "...{w}..."
    p "At least…I hope so."
    p "If the guy mom set up for me hasn't shown up in the last 5 hours, I doubt 
    they're gonna–"
    p "?!?!"
    # *The music cuts off and a loud thud plays while the screen goes black.*

    sb "Ow, ow, ow..!!"
    # *A shuffling sound effect plays, and the screen fades back into the image of sbwith their hair down looking all baby girl.*
    sb "My head…"
    ############################################################
    menu MyHead:
        sb "My head…"
        "Stay Quiet":
            call Proto_StayQuiet
        "Ask if they're okay":
            call Proto_TheyOk
        "Insult them":
            call Proto_Insult
    ############################################################
    sb "Uhm..anyways!"
    # *Depending on the choice made, SB will have their face in the CG image change from ^-^ to a more ^-^;;; expression.*
    sb "It is uh, nice to...meet you? Haha~"
    ############################################################
    menu WhoSent:
        sb "It is uh, nice to...meet you? Haha~"
        "Ask if they're the person your mom sent":
            call Proto_MomSent
        "Why are you late?":
            call Proto_WhyLate
    ############################################################
    sb "Though, if it's already this late…that so-called other person must be a real 
    jerk to have left a beautiful flower alone to wilt away into the night."
    sb "Tell me, what even was their name anyways?"
    ############################################################
    # put the name of the character
    $ targetPerson = 1
    $ specifiedName = "Sakura"
    call InsertName
    # name has been established
    ############################################################
    sb "Hmm…"
    sb "Hmmmm…"
    p "..?"
    # *A picture of Sakura Boi taking MC's hands into their own all excited “:D" appears.*
    ############################################################
    # delayed name change
    $ sakuraName = userInput
    ############################################################
    sb "While I am not a fan of outright abandonment, that sounds like quite the 
    exquisite name!"
    p "Eh?!?!"
    p "Don't you have a name of your own?! Don't go taking other people's–!"
    sb "How am I to take what never even bothered to show up in the first place~?"
    sb "If anything, consider it that person's 'tax' for failing to accompany you."
    sb "Besides~ It's not like I could come up with a name of my own."
    sb "It seems that fall did quite the number on my memories~"
    p "Okay. Maybe we should actually get you to a hospital–"
    sb "Nonsense! While I may lack my memories, I just know that it must be fate 
    that we met this way uhm… What's your name again?"
    p "...[p]"
    sb "Simply Divine. [p].~ I will cherish that name for the rest of my days."
    sb "Tell me, will you help recover my lost memories?"
    sb "If you do, you have my word that those concert tickets will be ours~!"
    menu ConcertTicket:
        sb "If you do, you have my word that those concert tickets will be ours~!"
        "This is ridiculous–":
            call Proto_Ridiculous
        "No.":
            # game ends prematurely
            jump Proto_No

    return
