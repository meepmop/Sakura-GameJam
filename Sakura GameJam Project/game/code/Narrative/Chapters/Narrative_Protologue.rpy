label Protologue:
    # *Open with a black screen, and soft, hopeful music playing.*
    p "It seems like this year's bloom will be even better than the last."
    p "{i}Sigh{/i}"

    # *The screen slowly fades into YuraYura’s infamous cherry blossom tree.*
    "While this marks only my second year at YuraYura Academy, it will also serve as my 21st anniversary of being officially maidenless."
    "Or…in plain terms. Lacking a Partner."
    "I was never really interested in the whole 'Dating' thing." 
    "It honestly never seemed like a big deal to me."
    "At first, while my family approved of my partnerless lifestyle, it seems as though with a flip of a switch they’ve gone from 'Focus on your studies!' 
    to 'Have you found someone who could give us grandchildren yet?' "
    "First of all, I don’t even know why they want someone like me to produce offspring."
    "If they took just one look at my spending habits, they’d realize there’d be no room for a mini-me anywhere in that equation."
    "Though, of course I couldn’t tell my dear mom about that. That’d have to be a conversation for another day."
    "Speaking of days, I’ve spent the majority of it just waiting here."
    "Waiting…{w} Waiting…"
    "Sitting here in the hopes that the person my mom told me about would just show the hell up already."

    p "It’s no wonder everyone’s acting all lovey dovey."
    p "Holding hands, sharing Boba…"
    p "If it weren’t for the fact mom didn’t promise me front row tickets to that virtual idol concert, I’d honestly be none the wiser."
    # *A small icon of MCs phone with a virtual idol game appears briefly.*
    p "Who even needs love anyways when I already have it at the touch of my fingertips?"
    p "Ah~ My beloveds~"
    p "Don’t worry. Your Producer will be with you all soon enough~"
    p "...{w}..."
    p "At least…I hope so."
    p "If the guy mom set up for me hasn’t shown up in the last 5 hours, I doubt they’re gonna–"
    p "?!?!"
    # *The music cuts off and a loud thud plays while the screen goes black.*

    sb "Ow, ow, ow..!!"
    # *A shuffling sound effect plays, and the screen fades back into the image of sbwith their hair down looking all baby girl.*
    sb "My head…"
    menu:
        sb "My head…"
        "Stay Quiet":
            call Proto_StayQuiet
        "Ask if they’re okay":
            call Proto_TheyOk
        "Insult them":
            call Proto_Insult
    sb "Uhm..anyways!"
    # *Depending on the choice made, SB will have their face in the CG image change from ^-^ to a more ^-^;;; expression.*
    sb "It is uh, nice to...meet you? Haha~"
    menu:
        sb "It is uh, nice to...meet you? Haha~"
        "Ask if they’re the person your mom sent":
            call Proto_MomSent
        "Why are you late?":
            call Proto_WhyLate
    return
############################################################
label Proto_StayQuiet:
    "I focus my gaze onto the person in front of me."
    "Too stunned to speak, it’s as if their appearance alone locks my lips in place."
    sb "I’m surprised my neck hasn’t snapped."
    sb "...Oh, wait just a moment..!"
    sb "It seems the grass being a bit more ‘cushiony’ than normal wasn’t just my imagination."
    sb "My apologies~"
    return

label Proto_TheyOk:
    # 1+ Attraction
    p "Are you alright?"
    p "You’re not hurt, are you?"
    p "I don’t particularly feel like dragging anyone to the hospital today."
    sb "Oh dear– My apologies. It seems you were the one who broke my fall."
    sb "You’re rather kind for someone who also just hurt themselves~"
    return

label Proto_Insult:
    p "Hey! What the hell’s wrong with you?!"
    p "How’d you even get up in that tree in the first place!?"
    p "You know if you damaged that tree, the administration is never gonna let us hear the end of it!"
    p "Not to mention–Ouch!"
    sb "Oh dear– My apologies. It seems you were the one who broke my fall."
    sb "I didn’t mean to hurt you. Honestly~"
    return
############################################################
label Proto_MomSent:
    return
label Proto_WhyLate:
    return
