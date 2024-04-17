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
    return





    return