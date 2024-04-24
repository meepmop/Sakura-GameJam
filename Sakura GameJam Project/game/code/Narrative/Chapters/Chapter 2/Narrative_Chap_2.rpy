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

    return

