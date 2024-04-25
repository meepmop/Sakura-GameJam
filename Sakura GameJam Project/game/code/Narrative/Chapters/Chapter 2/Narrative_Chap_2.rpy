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
    "Deciding to put an end to this conversation, you gesture towards the room 
    marked ‘Student Council Office’." 
    "Unlike the rest of the Campus, this particular part of it was lacking any sort of 
    festive flair." 
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
    # *The Background changes to the student council office. It has papers scattered everywhere 
    # and looks rather messy.*
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
    # *A CG of what looks to be a younger Kaito getting an octopus-cut hot dog fed to him by
    # Mikael pops up. Kaito is purposely positioned so that you can only see the back of his head. There are sakura petals littering the area around them. No one else is around them.*
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
    sb "Oh dear."
    "Judging from the ominous tone of Kaito’s voice, you quickly reached to grab at [sb]'s arm."
    "Now turning to make a run for it, you could only imagine what would have become of you two 
    if you hadn’t."
    "After all, just from a mere glance, you could see the sheer difference in mass between 
    yours and Kaito’s arms."
    "It almost reminded you of one of your favorite idols."
    "Not that you had the time to be thinking about this sort of stuff anyways with said 
    man now actively chasing you through the hallway."
    p "H-He’s fast!"
    sb "I think we’ve done a bit too well, don’t ya think~"
    ks "Get back here and reap what you’ve both sewn!!"
    ks "Once I get my hands on you, you are going to wish that you let me keep to my 
    regularly scheduled activities!!"
    ks "I’ve even taken the liberty of calling the school’s infirmary to reserve both your seats!"
    sb "Oh, how kind~"
    sb "Did you hear that? That must mean he cares~"
    p "No, that means he’s going to kick our ass!"
    "With your chest pounding from the sudden need to run, you find your head scrambling at the 
    sight of a forked path."
    sb "I’m thinking we go left."
    sb "After all, there are more beautiful decorations leading that way."
    sb "Perhaps the Cherry Blossoms shall serve as our guide towards escape~"
    ############################################################
    menu cherryBlossomEscape:
        sb "Perhaps the Cherry Blossoms shall serve as our guide towards escape~"
        "Listen to [sb]":
            call Chap2_ListenToSakura
        "Ignore them":
            call Chap2_Ignore
    ############################################################
    ah "Make way, make way~!"
    ah "Your beloved Amari is here, dawning a chariot befitting that of a 
    princess, nonetheless!"
    "Turning your attention towards the source of the dramatics, your eyes widen 
    at the sight before you."
    # *Insert CG of Amari on horseback extending their hand out towards you. 
    # Don’t ask how they got an entire horse both on Campus and inside the building, 
    # just roll with it.*
    ah "Care for a lift~?"
    ah "Well. Not that you’ve much of a choice."
    ah "Not unless you wish to suffer at the hands of my one and only best friend~"
    ############################################################
    menu sufferHands:
        ah "Not unless you wish to suffer at the hands of my one and only best friend~"
        "Take Amari’s hand":
            call Chap2_TakeAmariHand
        "Stand still":
            call Chap2_StandStill
        "Accept your fate":
            jump Chap2_AcceptFate
    ############################################################
    ah "Ahahaha! How absolutely wonderful~!"
    ah "One could even classify such as amazing~ Don’t you think?"
    ks "I’ve found you–!"
    sb "Uh oh."
    "Quickly snapping at the reins of their stallion, Amari continues to cackle as the 
    horse bucks beneath you all."
    "Both you and [sb] hold on for dear life while the animal charges through the 
    passing by students and straight for Kaito."
    ks "A-Amari!?"
    ah "‘Tis nothing personal, Kaito-Kun~"
    ah "Consider this just part of the show~!"
    ############################################################
    menu partOfShow:
        ah "Consider this just part of the show~!"
        "Warn Kaito":
            call Chap2_WarnKaito
        "Taunt Kaito":
            call Chap2_TauntKaito
    ############################################################
    "Fortunately enough for Kaito, it seemed as though luck was on his side."
    "Having taken a leap of faith, Kaito had just barely in the knick of time 
    dodged the impending doom which was Amari."
    "Though, judging from how excited the eccentric was despite nearly trampling his 
    supposed ‘best friend’, something told you that this wasn’t too out of the norm for them."
    # *The scene shifts to the Campus’ Cherry Blossom tree. It’s the same spot where you first 
    # met [SB].*
    ah "Ahh~ What joy that always brings me."
    ah "I’m quite certain Kaito-Kun should have been kept more than busy with that stunt."
    "Hopping off their steed, Amari runs his fingers through their mane, cooing out a few words 
    of praise in the process."
    "Deciding to join them on the comfort which was the ground, you notice that [sb] appears 
    to be struggling."
    ############################################################
    menu strugglingSakura:
        "Deciding to join them on the comfort which was the ground, you notice that [sb] appears 
        to be struggling."
        "Help them":
            call Chap2_HelpThem
        "They can handle it":
            call Chap2_HandleIt
    ############################################################
    ah "You know, dramatics aside, I am beyond happy to finally have you both to myself~"
    ah "I simply must know. Just what have you done to cause my best friend to ‘start swinging’ 
    as the youth say~"
    ############################################################
    menu startSwinging:
        ah "I simply must know. Just what have you done to cause my best friend to ‘start swinging’ 
        as the youth say~"
        "We bullied him.":
            call Chap2_WeBully
        "[sb] bullied him":
            call Chap2_SakuraBully
    ############################################################
    ah "I see…"
    "Clapping their hands together, with a spark of burning passion, Amari takes [sb]’s 
    hands into their own."
    ah "Oh, flower of dawn, won’t you relay to me your wisdom?!"
    ah "Show me what you’ve done to spark the fire within Kaito-Kun’s heart!"
    sb "?!?!"
    ############################################################
    menu sparkTheFire:
        sb "?!?!"
        "Nudge [sb]":
            call Chap2_NudgeSB
        "Stand there awkwardly":
            call Chap2_StandAwkward
    ############################################################
    sb "Alright, alright!"
    sb "You just have to promise. No trying to hurt me or [p]. Don’t shoot the messenger!"
    ah "You have my word– My heart, even~! Now, speak..!"
    ah "Speak to me the words which set Kaito-Kun’s heart ablaze~!"
    "With a huff, [sb] manages to pry themselves away from Amari."
    "They press their fingers together, and glance towards you."
    "It was as if they were silently asking for your support."
    sb "When I look at you, it’s almost like I see someone that’s constantly changing."
    sb "Judging from how dramatic you are…I’m assuming that’s in character."
    sb "But, it’s kind of funny. That this spot you took us to, also once served as 
    the beginning for said character in the first place."
    # *A CG of a younger Amari seemingly praying at this tree is shown. They have 
    # longer hair, decorated with a sakura blossom, and are wearing a high school 
    # male uniform which appears slightly too big on them. Nearby, a kimono can be 
    # seen along with a pair of scissors as well as their backpack.*
    ############################################################
    menu beginningForCharacter:
        sb "But, it’s kind of funny. That this spot you took us to, also once served as 
        the beginning for said character in the first place."
        "Stay Quiet":
            call Chap2_StayQuiet
        "Speak up":
            call Chap2_SpeakUp
    ############################################################
    ah "Tell me more~"
    sb "W-Wouldn’t you already know all this stuff anyways??"
    sb "I-I’m only saying what comes to mind– it’s only when sakura petals fall, 
    that I can truly gain a sense of who someone really is."
    sb "It’s not like I can learn your whole life story…"
    ah "Oho~"
    ah "Ohohoho~"
    ah "I see."
    ah "A shame, really."
    ah "I’d of loved to hear what happened next~"
    ah "After all, each retelling of tragedy has its own unique touch."
    "With a wink, Amari twirls their body to end up right behind you."
    "Placing their hands on your shoulders, you instantly become stiff as a board."
    ah "Wouldn’t you agree, [p]?"
    ############################################################
    menu wouldntAgree:
        ah "Wouldn’t you agree, [p]?"
        "T-Touching…":
            call Chap2_Touching
        "The only thing that’s ‘tragic’ is…":
            call Chap2_OnlyTragic
    ############################################################
    "Humming out a small tune, Amari releases their hold on you."
    "Rather than pay mind to your feelings on the matter, they instead focus 
    their attention towards the Sakura tree once more."
    ah "The Cherry Blossom season is nearing its conclusion."
    ah "That means soon enough, there won’t be any ‘petals’ for [sb] to latch on to."
    ah "As someone that never truly viewed themself as ‘in the norm’, I can tell that you and I, 
    [sb], are the same~"
    ah "Though, that should be a talk for another day."
    ah "I’d love to see what you’re able to accomplish come Friday~"
    ############################################################    
    menu accomplishFriday:
        ah "I’d love to see what you’re able to accomplish come Friday~"
        "Mention Mikael":
            call Chap2_MentionMikael
        "Mention Kaito":
            call Chap2_MentionKaito
        "Mention your Idol Tickets":
            call Chap2_MentionIdol
    ############################################################
    ah "Everything shall fall in place soon enough~!"
    ah "Just trust in the blossom of fate, and she shall deliver!"
    ah "You have my word!"

    return

