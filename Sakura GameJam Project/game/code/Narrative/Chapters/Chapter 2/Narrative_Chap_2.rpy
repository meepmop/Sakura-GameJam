label Chapter2:
    # Open up with asset of the school Hallway*
    # General lighthearted music is playing.*
    # A slightly transparent sprite of Mikael is used*
    ma "It’s simple, really~"
    ma "Ya just gotta keep him busy, butter him up, smooze him. Ya know?"
    ma "If ya do, ya got my word. Both you and Flower Boy over there won’t be gettin’ any of 
    my white stuff on ya~"
    "You can’t help but hang your head low at the redhead’s choice of wording."
    "Though, given the circumstances, both you and [sb] had nothing better to do while on 
    your quest to help recall their memories."
    "After all, with Mikael’s reputation, you’d be an idiot to get on his bad side."
    "If he even had one, that is."
    "Now walking side by side [sb], you passively direct your gaze up from your phone and 
    towards them."
    p "What does ‘smooze’ even mean??"
    sb "I believe it’s a term more commonly used abroad~"
    sb "I’m to assume you’ve had your head wrapped around Mikael’s ever since our last ‘chat’?"
    ############################################################
    menu lastChat:
        sb "I’m to assume you’ve had your head wrapped around Mikael’s ever since our last ‘chat’?"
        "Well–":
            call Chap2_Well
        "Remain quiet":
            call Chap2_RemainQuiet
    ############################################################
    "Deciding to put an end to this conversation, you gesture towards the room marked ‘Student Council Office’." 
    "Unlike the rest of the Campus, this particular part of it was lacking any sort of festive flair." 
    # *When Mikael is talking here once more, he’s still transparent to convey that this 
    # conversation took place in the past.*
    ma "Just keep him busy for a bit!"
    ma "On Wednesday, I’ve got some errands to run, so if ya can, make sure he doesn’t leave his 
    office until at least 1:30."
    ma "I’m sure with Flower boy here, it’ll be a piece of cake!"
    "Briefly taking a look back at your phone, you see that the current time is 12:45."
    "From what you recall Mikael saying, you know that Kaito typically leaves for his 1 PM 
    ‘rounds’ at this time."
    "Whatever that means."
    sb "You ready?" 
    sb "Remember, we’ve just gotta prevent the guy from leaving until the time Mikael said."
    sb "If anything, I’ve got a few ‘tricks’ up my sleeve~"
    sb "So…let’s do this!"
    ############################################################
    menu letsDoThis:
        sb "So…let’s do this!"
        "Reach for the door":
            call Chap2_ReachDoor
        "Knock":
            call Chap2_Knock
    ############################################################
    "Kaito takes a moment to survey the area."
    "When he notices it seems to be just you two here, you see him step aside 
    to gesture for you both to step inside."
    # *The Background changes to the student council office. It has papers scattered everywhere and looks rather messy.*
    # *Kaito’s Theme Plays*
    ks "I’m assuming Amoris is up to something yet again?"
    ks "He must be reaching the bottom of the barrel if he’s enlisting the help of not only 
    a wallflower, but a complete stranger nonetheless."
    ############################################################
    menu wallflowerStranger:
        ks "He must be reaching the bottom of the barrel if he’s enlisting the help of not only 
        a wallflower, but a complete stranger nonetheless."
        "For the last time…":
            call Chap2_ForLastTime
        "This room is a mess.":
            call Chap2_RoomMess
        "You’re a mess.":
            call Chap2_YouMess
    ############################################################
    "Letting out an irritated huff, you take another look at your phone."
    "Almost 1."
    "You had no idea how you were going to last another half hour with this man."
    "After all, just a few minutes with him had already made you want to punch him."
    "It’s then you catch a glimpse of the slightly mischievous grin which [sb] casts your way."
    ############################################################
    menu sbSendMichievous:
        "It’s then you catch a glimpse of the slightly mischievous grin which [sb] casts your way."
        "Say Something":
            call Chap2_SaySomething
        "Remain Quiet.":
            call Chap2_RemainQuietAgain
    ############################################################
    sb "Hey."
    sb "Kaito Sakuraba…was it?"
    sb "You know, for some reason, now that I actually think about it, that name sounds familiar."
    sb "You and that Mikael guy would always have lunch at the nearby park~"
    sb "The Anime-Themed Bento boxes were your favorite, were they not?"
    "Both you and Kaito stare confusedly at [sb]."
    ks "How did you…"
    "The sudden shift in attention almost causes [sb] to stumble."
    sb "Was that too forward??"
    sb "Forgive me~"
    # *A CG of what looks to be a younger Kaito getting an octopus-cut hot dog fed to him by Mikael pops up. Kaito is purposely positioned so that you can only see the back of his head. There are sakura petals littering the area around them. No one else is around them.*
    sb "I mean~ I just knew I recognized something about you two."
    ma "Do you like it?"
    ma "I made sure to pack your favorite~"
    ks "Your craftsmanship has most certainly improved since coming here."
    ks "Though, I am quite jealous to know how others are soon going to be able to taste your–"
    # *The CG gets disrupted by a rather displeased looking Kaito.*
    ks "Enough!"
    "You notice how Kaito’s fists are now clenched."
    ks "Is this how you plan to distract me?? By bringing up the insignificant moments of the past?!"
    ks "As far as I’m concerned, I don’t even know who you are."
    ks "At the very least I could verify [p]'s existence!"
    ks "Yet you. Bearing the falsities of someone who’s oh so innocent and nice."
    ks "Truly, you’re a greater thorn in my side than I initially thought."
    ############################################################
    menu greaterThorn:
        ks "Truly, you’re a greater thorn in my side than I initially thought."
        "Uh…":
            call Chap2_Uhh
        "Further push Kaito":
            call Chap2_FutherPush
    ############################################################

    return

