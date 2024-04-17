############################################################
# familiarSakura
############################################################
label Chap1_Familiar:
    call sbLoveIncrease
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
    call sbLoveDecrease
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
    call sbLoveIncrease
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
# Our classes?
############################################################
label Chap1_SearchChoice:
    menu whereTheyGo:
        "Knowing there’s only so many places they could be, you decide the following:"
        "Check the Nearby Classrooms.":
            jump Chapter1_Cont_NearbyClass
        "Check the Supply Closet":
            jump Chap1_SuppyCloset
        "Cut your losses and just leave.":
            jump Chap1_JustLeave
    return
label Chap1_SuppyCloset:
    "Figuring that perhaps there would be some spare decorations inside, you make your way to the Supply Closet located at the end of the hall."
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
    "It wasn’t your problem anyways."
    return