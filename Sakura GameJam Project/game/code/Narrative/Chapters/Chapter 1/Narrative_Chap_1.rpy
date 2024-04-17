label Chapter1:
    "Day: Monday
    \nSetting: Streets of Tokyo leading towards YuraYura Academy
    \nTime: Morning"

    # *There would be casual/’lighthearted’ musical beats happening here.*
    "The weekend passes by just as quickly as it came."
    "As Cherry Blossoms continue to litter the streets with their 
    iconic Sakura Pink hue, you can’t help but admire their beauty."
    ############################################################
    menu familiarSakura:
        "As Cherry Blossoms continue to litter the streets with their 
        iconic Sakura Pink hue, you can’t help but admire their beauty."
        "The petals remind me of…":
            call Chap1_Familiar
        "Focus your attention back to your phone.":
            call Chap1_FocusPhone
    ############################################################
    sb "Oiii~ [p]!"
    sb "Oi, Oiiiii! Over here~!"
    "You quickly shift your gaze towards the direction which the voice is coming from.
    However, you can’t help but feel your brow twitch at the display."
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
    # There seems to be signs of the upcoming cherry blossom festival everywhere, 
    # ranging from posters in the background to decorative flowers hung up all 
    # around the hall.*
    p "Here we are."
    p "This is where we’ll start, I guess."
    sb "Woooow~! How pretty..~!"
    sb "It’s as though nature itself has reflected itself in this very hallway..!"
    sb "I simply must see more of it!!"
    p "We can but–"
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
    # It holds hints of the upcoming festival within it.*
    jd "Unbelievable!!"
    p "Huh–"
    jd "When I get my hands on him..!"
    jd "Oho~ Kaito-Kun~ I can practically see your hair graying by the second! Please, calm yourself~"
    ks "You’re not helping."
    jd "Ah~ Would you rather me join in your rage?"
    ah "Ahem. I, Haruka Amari, shall swear vengeance on the one foolish 
    enough to oppose YuraYura’s student council!"
    "Before you’ve the chance to leave, you find yourself cornered by the louder of the two people."
    "Their eyes glisten with a manic fire as they firmly take your hands into their own."
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
    ks "Enough."
    # *A CG of both Amari and Kaito standing side by side appears. Kaito looks less than impressed while Amari is seen striking a pose.*
    # *Kaito’s theme will now play.*
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
    "Running his fingers across the powdered white substance which coats the 
    desk in front of him, you notice the glint of sorrow which lingers behind his mask."
    ks "There’s no doubt about it. This is his work."
    ah "Gone just as quickly as they came too, no?"
    ah "A true master of stealth~"
    ks "You mean a true pain in the ass."
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
    "Suddenly, before another word can be spoken, a loud scream can be 
    heard coming from outside of the classroom."
    sta "HELP ME! PRESIDENT-SAMA!! IT’S EVERYWHERE!!!!"
    stb "The flour bomber is back again! Run!!"
    stc "My eyes!! They’re so dry!!!!"
    ks "..!"
    ks "Mikael!!!"
    "Without skipping a beat, Kaito can be seen bolting out of the area."
    ks "Out of my way!"
    # *Some clattering sound effects could be heard*
    ks "I said MOVE!"
    ah "Oh dear…there he goes again~"
    ah "I shouldn’t leave poor Kaito-Kun alone too long."
    ah "May we cross paths once more in the near future! My beloved [p]~!"
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
    "[sb]’s lips curl into a warm smile." 
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
    return