label chapter3:
    $ quick_menu = True
    $ renpy.music.play("audio/Music/DayBegins_Intro.ogg", fadein=1.0)
    $ renpy.music.queue("audio/Music/DayBegins_Loop.ogg", clear_queue=False,loop=True,fadein=1.0)
    scene BG YYFront with fade
    "It's already Friday."
    "Time passes quickly when you're dealing with crazy."
    "Part of you wonders if it was fate's way of telling you to get better hobbies."
    "You huff at the thought as you stare down once more at your phone."
    "This time, you watch the virtual idols from your game sing and dance to one of your favorite songs."

    jd "Lookin' at hot fictional men again now, are ya?"

    menu:
        "Question the voice":
            call sbLoveDecrease
            call loveNotification
            p "Listen [sb], if you have nothing productive to say then you're better off not saying it at all–"
            show ma basic at center with vpunch
            ma "[sb]. [sb]?!?!"
            ma "Need I introduce myself once more?!"
            ma "It's me, Mikael Amoris~ President of YuraYura's—"
            p "...Baking Club I got it."
        "Ignore the voice":
            call maLoveDecrease
            call loveNotification
            "Too enamored by the movements of your idol game, you brush right past the source of the voice."
            "However, right as you do so, you find a firm grasp on your shoulder."
            show ma basic at center with dissolve
            "Finally turning to face it, your body stiffens at the sight of a less than pleased Mikael."
            ma "Ya know. I ain't exactly the type to like bein' ignored."
        "Defend yourself":
            call maLoveIncrease
            call loveNotification
            p "Well it's not like I have anything better to look at!"
            show ma wink1 at center with hpunch
            "Immediately upon saying this, you're met with a boisterous laugh and a firm hand on your shoulder."
            ma "Where have I heard that one before~"
    show ma vhappy
    ma "So [playerName]. Are ya ready for today~?"
    ma "I know we haven't had much of a chance to chat. But I just wanted to say thanks~"
    show ma wink2
    ma "Without you or Flower Boy, Sakuraba would be on my ass for sure, and not in the good way~"

    menu:
        "Good way?":
            call maLoveIncrease
            call loveNotification
            p "There's a…good way?"
            show ma basic
            ma "Well, I doubt it'd be now, with how much of a prick he's been as of late."
            p "..."
        "Sure.":
            call maLoveIncrease
            call loveNotification
            p "Yeah, yeah."
            p "Honestly, I”m just hoping we can find some answers today."
            p "If not, Amari might appear with {i}two{/i} horses this time."
        "You didn't tell us...":
            call maLoveDecrease
            call loveNotification
            show ma basic
            p "You didn't tell us the guy was jacked!"
            p "Were it not for Amari and their damn horse, I'm pretty sure [sb]'s memories would be worse than they already were!"
            ma "So the Princess brought out her valiant steed now, did she?"
            ma "Interesting..."

    show ma basic

    ma "Say, where is Flower Boy anyways?"
    ma "Judging from how happy you looked right before I got here, I'm assuming ya haven't met up with ‘em yet."
    p "Well, they were... stopping to get us some breakfast."
    p "That old lady who runs the nearby sweet stand's apparently been giving them cookies all week."

    show ma happy

    ma "Ohhh! Miss Ayaka!"
    ma "She's the best!"
    
    menu:
        "What happened?":
            call maLoveIncrease
            call sbLoveIncrease
            call loveNotification

            p "You're sounding like it's been awhile since you last went."
            p "Is there a reason for that?"
            show ma basic

            "Mikael glances away with a sheepish look to him."
            ma "Let's just say a certain someone always beats me to my favorite sweets."

            show ma wink1

            ma "Now, I could always just plan ahead. But I only do that when I'm feelin' extra mischievous~"

        "You didn't steal them, did you?":
            call maLoveDecrease
            call loveNotification
            p "Don't tell me you took from that poor old lady–"

            show ma basic with hpunch
            ma "Oh God no!"
            ma "In fact, I was one of her best customers!!!"
            ma "Still am, from time to time~"

        "We should all go sometime.":
            call maLoveIncrease
            call loveNotification
            p "If that's the case, maybe I can drag you along sometime."
            p "That is...as long as we can get [sb]'s whole memory situation figured out."
    sb "Oiiii!"
    sb "[playerName]!{w=0.3} Mikael..!"
    sb "That's you two I'm seeing, right??"
    scene CG C1 sbrunning with dissolve
    sb "I remembered~"
    p "Your memories?!"
    sb "No, your ice cream!"
    sb "I promised I'd get you some."
    sb "And this time, Kaito isn't there to knock it away~"
    ma "Did ya bring some for me too~?"
    "Your brow twitches at the utter stupidity which was Mikael."
    "However, before you could call them out on it, [sb] casts you an honest smile."
    sb "I wasn't expecting to need extra."
    sb "Though, if you'd like, perhaps I can get you something at the campus festival today?"
    sb "After all, if my memories don't resurface by then, I'm not sure they ever will."
    #*The scene shifts to outside of YuraYura. Once again, couples are everywhere. Stalls are set up with all sorts of vendors, and it seems like everything is going smoothly.
    #*A peaceful yet uplifting festival theme is playing*
    $ renpy.music.play("audio/Music/Festival_FleetingBlossoms_Intro.ogg", fadein=1.0, loop=True)
    $ renpy.music.queue("audio/Music/Festival_FleetingBlossoms_Loop.ogg", clear_queue=False,loop=True,fadein=1.0)
    scene BG YYFront
    show sb happy at right
    show ma basic at left 
    with dissolve
    ma "Alright, alright, alright...~"
    hide sb with dissolve
    show ma happy at center with move
    "Clapping his hands together, Mikael makes their way in front of you."
    "Much to [sb]'s' delight, you're met with a bundle of excitement in the form of a poorly drawn \"Battle Plan.\""
    ma "So!"
    ma "Here's what's up."
    ma "You're gonna take Flower Boy here on a date~"
    ma "But not just any date."
    ma "It's gotta be romantic~"

    menu:
        "What?":
            call sbLoveDecrease
            call maLoveDecrease
            call loveNotification
            p "Are you kidding me?"
            show ma angry
            "Mikael pouts at your less than thrilled response."
            ma "Do I gotta repeat myself?"
            ma "Ya know...I even toned down the accent and everythin'!"
            ma "You and [sb], Flower Boy, are gonna be lovers for the day!"
        "?!?!":
            call sbLoveIncrease
            call maLoveIncrease
            call loveNotification
            p "D-Don't tell me we're gonna have to be like...{w}{i}lovers{/i}."
            "You feel your face heating up at the idea of romance."
            "Not to mention, you certainly didn't have the funds to pay for it."
            "Boba...drinks...those stupid rigged carnival games..."
            "You just knew that [sb] would be an absolute sucker for it."

    show ma happy

    ma "If it makes ya feel better, I'm only sayin' this so you can keep Sakuraba busy a bit longer."
    ma "Guy's a sucker for stickin' his nose where it ain't belong."
    ma "Especially when it comes to people who've been gettin' on his bad side~"

    show ma happy at left
    show sb thinking at right
    with dissolve

    sb "Aren't you the one who usually does that?"

    show ma wink2

    ma "Well obviously. But thanks to you two, I've been able to set up my grand scheme~"
    ma "It just needs one final touch."

    menu:
        "Ask what it is.":
            call maLoveDecrease
            call sbLoveIncrease
            call loveNotification
            p "Don't tell me you're gonna ruin a perfectly good festival with flour..."
            p "If [sb] and I have to date, I'd rather it be far, far away from whatever it is you're planning."

            show ma wink1

            ma "Aw~ Ya don't gotta worry ‘bout that."
            ma "What I'm plannin' specifically revolves around Sakuraba and his lackeys."

            show ma basic

            ma "But if I told ya what it was exactly, I'd have to kill ya."

            show sb ouch

            sb "Y-You wouldn't kill me, would you?"
            sb "I just need to last the rest of today so–"

            show ma happy

            ma "Of course not~"
            ma "We're friends now, I know I can trust you."
        
        "Just roll with it.":
            p "So...[sb]."
            p "How about one date?"

            show sb happy

            "You force yourself to reach out and allow [sb] to eagerly grab hold of your hand."
            "It's cold, yet still somewhat comforting."

    show ma wink1

    ma "Anyways. I'll see you two lovebirds around~!"
    ma "Make sure to put on quite the show, ya hear???"
    ma "I've got some Mikael-in' to do!"

    hide ma 
    show sb happy at center
    with dissolve

    "You see Mikael laughing as they saunter away."

label festivalactivities:
    menu:
        "Now, with the day to yourselves, you decide to do the following:"
        "Check out the food stalls." if foodstalls == False:
            $ foodstalls = True
            call ksLoveIncrease
            call loveNotification

            "With the scent of savory meat filling the air, you goad [sb] closer to its source."
            sb "Wow~ Look at all those hot dogs~"
            sb "[playerName], would you like to try some with me?"
            sb "I've always wanted to know what they taste like~"

            menu:
                "I'm broke.":
                    call sbLoveDecrease
                    call loveNotification
                    p "I don't exactly have any cash on me..."

                    show sb ouch

                    sb "Oh...how disappointing..."
                "Sure.":
                    call sbLoveIncrease
                    call loveNotification
                    "Knowing full well you have absolutely zero cash to your name, you put up a front of confidence to order one of the cute treats."
                    p "One octopus hot dog please."
                    ven "Of course~ That will will be 5–"

            stop music fadeout 1.0
            jd "Put it on my tab."

            show sb thinking

            sb "Really??"

            $ renpy.music.play("audio/Music/Kaito_FleetingBlossoms_Intro.ogg", fadein=1.0,loop=True)
            $ renpy.music.queue("audio/Music/Kaito_FleetingBlossoms_Loop.ogg", clear_queue=False,loop=True,fadein=1.0)

            show sb at left
            show ks oh at right
            with dissolve

            "Hearing [sb]'s gasp, you turn and are met with a familiar face."
            "...or lack thereof."
            show ks blush
            ks "Consider it an apology."
            "You notice a slight tinge of pink coating the Councilman’s cheeks."
            menu:
                "Call him out.":
                    call ksLoveDecrease
                    call sbLoveDecrease
                    call loveNotification
                    p "For nearly sending us to the hospital?"
                    p "I’ll take your money, but you’re gonna have to do a lot more than that to–"

                    show sb happy

                    "Before you can finish your sentence, you see [sb] having already stuffed their face with the other’s bribe."
                    sb "Hot, hot, hot!!"

                    show ks neutral

                    sb "Thank you, Kaito-Senpai~"
                    p "Are you kidding me..."

                "Thank him.":
                    call ksLoveIncrease
                    call sbLoveIncrease
                    call loveNotification

                    "Cautiously reaching for the treat, you admire its cuteness before popping it into your mouth."

                    show sb happy

                    "Out of the corner of your eye, you also see [sb] nearly choke on their own, making it hard for you to not laugh at the display."

                    p "Thanks..."
            show ks thinking

            ks "They’re tasty, are they not?"
            ks "And rather cute, too."
            ks "A perfect treat to celebrate the end to a long week."

            show ks neutral

            ks "Especially after having to deal with Mikael’s foolishness."
          
            menu:
                "What about us?":
                    call ksLoveIncrease
                    call loveNotification
                    p "“It wasn’t just Mikael you had to deal with."
                    sb "Yeah...you nearly killed us, haha~"
                    "Kaito rolls his eyes at your and [sb]'s antics."
                    ks "At the end of the day, I cannot direct my anger towards mere pawns."
                    ks "I’m almost certain that whatever Mikael has planned, he’s going to act on it, with or without a distraction."
                    ks "As such, I’ve come to accept it."
                    ks "Let the gods decide my fate."
                    ks "If it means I can enjoy myself for a day, then so be it~"
                    ks "Besides, judging from what Amari has told me, Mikael would never ruin such a traditional festival."

                    show ks shine

                    ks "He’s afraid of the \"Hundred years bad luck\" it’s said to bring, fufufu~"

                "What about him?":
                    call ksLoveDecrease
                    call loveNotification
                    p "He’s been acting pretty strange from the start."
                    p "Overly touchy…always thinking about you..."
                    p "I wouldn’t be surprised if he went ahead and drenched this place in flour just so you’d look his way."

                    show ks angry
                    show sb oh

                    "You notice Kaito beginning to rub circles in the side of his head."
                    ks "This festival is supposed to be a time of reprieve."
                    ks "I’d prefer it if we stopped speaking of the Devil, lest he make his unwanted appearance."
                    ks "Besides. I’m quite certain we’re safe."
                    ks "Mikael’s under the assumption that maliciously tampering with a traditional festival would cause him to go bald before reaching 30."

            show ks neutral
            ks "Anyways."
            ks "I trust that I’ve repaid my debt to you both?"

            show sb thinking

            sb "Not really."

            show ks oh

            ks "..."
            sb "All you did was pay for some snacks!"

            show sb ouch

            sb "Shouldn’t you like, let us get some super secret insider Kaito Sakuraba knowledge or something?!"
            sb "Like…why do you even hide your face anyways?!"
            sb "It must get quite stuffy under that mask of yours."
            sb "Not to mention, the fog from wearing {i}glasses{/i} too??"
            sb "Back me up here, won’t you, [playerName]?"

            menu:
                "Demand answers.":
                    call ksLoveDecrease
                    call sbLoveIncrease
                    call loveNotification

                    show ks angry
                    show sb happy

                    p "I’m kind of with [sb] here."
                    p "You did nearly kick our asses, you know."
                    p "One report to the Dean, and I’m sure you’d have your title as President revoked~"

                    show sb happy

                    "Seeing Kaito’s less than pleased expression, [sb] lets out an awkward laugh."
                    sb "I don’t think he’s gonna budge~"

                "Let sleeping dogs lie.":
                    call sbLoveDecrease
                    call ksLoveIncrease
                    call loveNotification

                    show sb oh
                    show ks neutral

                    p "I think we’ve spent enough time here."
                    p "Besides, you’re being a bit more harsh than usual..."
                    p "Why don’t we go check out the remainder of the festival?"
                    p "I’m sure it’s a lot more appealing than whatever’s beneath Kaito’s mask."

                    "Kaito huffs at the attempt of deflection. However judging from the soft look to their eyes, your efforts won’t go unappreciated."

            ks "As much as I’ve enjoyed this little \"chat\" of ours, I have to go prepare for the evening’s lantern lighting."
            ks "Go explore the other attractions. I’ve made sure there'd be plenty."
            ks "If the rumors are true...perhaps [sb] may find some use in them."

            stop music fadeout 1.0
            hide ks
            show sb at center
            with dissolve
            $ renpy.music.play("audio/Music/Festival_FleetingBlossoms_V1.mp3", fadein=1.0,loop=True)

            if sbdecide and foodstalls and games == True:
                jump epilogue
            else:
                jump festivalactivities


        "Play some games." if games == False:
            $ games = True
            call ahLoveIncrease
            call loveNotification
            "Taking notice of a giant Mochi-Themed plush which passes you by, make your way towards its source."
            gm "Come one, come all!"
            gm "Scoop a Sakura Petal, and win a prize~"
            gm "It’ll only cost ya 500 Yen~"
            sb "Oh~ We’d love to!"
            sb "Isn’t that right, [playerName]?"

            menu:
                "Search for the money.":
                    call sbLoveIncrease
                    call loveNotification
                    "You let out a defeated sigh."
                    "Knowing full well you have no cash to your name, you make an attempt to \"search\" for some in your pocket."

                    show sb oh with vpunch

                    "However, right before you can inform [sb] of your brokenness, you’re met with the screams of a few nearby people."
                
                "I'm broke.":
                    call sbLoveDecrease
                    call loveNotification
                    p "500 Yen?!"
                    p "You people here are acting like I actually have money!"
                    show sb ouch
                    sb "... Do you not have some form of job?"

                    show sb happy

                    sb "I guess not, considering you’ve been helping me all week, haha~"
                    
                    show sb oh with vpunch

                    "Before you can defend your jobless honor, you’re met with the screams of a few nearby people."

            stop music fadeout 1.0
            sta "R-Run-!"
            lonb "The one time I step outside and this happens!!!"
            jd "Ahahahaha...~!"
            jd "Ahahahahahaha~!"

            show sb happy

            sb "I recognize that laugh!"
            "[sb]’s lips curl into a wide smile."
            $ renpy.music.play("audio/Music/Amari_Intro.ogg", fadein=1.0)
            $ renpy.music.queue("audio/Music/Amari_Loop.ogg", clear_queue=False,loop=True,fadein=1.0)
            show ah shine at right
            show sb happy at left
            with dissolve
            "Emerging from the crowd of frantic couples, you’re met with Amari.
            However, rather than bring their trusted stallion, they’ve instead opted to come bursting in on the back of a raging bull."
            ah "Just a moment!"
            ah "[playerName]! [sb]! I have {i}arrived~{/i}!"

            menu:
                "What the...":
                    call ahLoveIncrease
                    call loveNotification
                    p "What the fuck!?"
                    p "I-Is that–"

                    show ah happy 
                    ah "My beloved pet bull, Bushi!"
                    ah "We’ve both come to this festival dressed to impress!"
                    ah "And with the mention of games...I just knew I would find my beautiful blossom here~"

                "Go away.":
                    call ahLoveDecrease
                    call loveNotification
                    p "Oh no. Absolutely not. Get the Hell away from us!"

                    show ah bored

                    ah "Unfortunately, once Bushi has set her sights on something, she's \"locked in!\""

                    show ah neutral

                    ah "Make way, make way!"
                    ah "Allow for us to enjoy a day of festivities and games alongside you, [playerName]!"

            "You watch helplessly as Amari and their \"pet\" make their way beside you."
            "Seeing Amari hand the vendor an envelope, your eyes widen as they hurriedly prepare a net for you and [sb]."
            gm "Try as many times as your hearts desire~"
            p "This isn’t some scam is it–"

            show sb ouch

            sb "Come on!!!"
            sb "Not it. Not it–Another dud!!"
            "[sb] appears to be frantically scooping as if their life depended on it."
            "Much to the Game Master’s Glee, you can see them keeping tabs via a notepad."

            show ah happy

            ah "You’d best start scooping, [playerName]~"

            menu:
                "Scoop.":
                    call sbLoveIncrease
                    call ahLoveDecrease
                    call loveNotification
                    "Furrowing your brows, you carefully watch as the floating disks gradually make their way through the water."
                    "Not wanting to make too many \"attempts,\" you wait until just the right moment to strike."
                    p "Here!"

                    #*A disk with sakura petal on it is shown*

                    gm "Well done~"

                    show sb happy

                    sb "Woah!!! How’d you do that?!"

                    show ah bored

                    ah "I’m assuming they just analyzed the pattern of the disks you’ve already upturned."

                    show ah annoyed

                    ah "How boring~"
                "Scoop!!!":
                    call sbLoveDecrease
                    call ahLoveIncrease
                    call loveNotification
                    "Seeing how [sb] was already twelve steps ahead of you, you decide to match their passion for scooping by going twice as fast."

                    show ah owo
                    show sb thinking

                    "Splashing water all over both yourself and the Game Master, you notice the look of shock painting [sb] and Amari’s faces."
                    sb "Hey!!!"
                    sb "You’re stealing all my disks!!"
                    sb "I-I can’t keep up!!!"
                    ah "Oh wow~"
                    ah "I’ve never seen someone use that method before..."
                    #*A disk with a sakura petal on it is shown*
                    gm "Ding! Ding! Ding!! One grand prize, coming right up~"

                    show sb happy

                    sb "I take my anger back– Good job, [playerName]!!!"
            gm "I think this one best suits your friend over there."

            show ah vhappy

            ah "How adorable!"

            #*Insert CG of [SB] struggling to hold a huge Pink Mochi stuffed plushie in their arms. Amari can be seen on Bushi laughing*

            ah "Pink is such a lovely color, don’t you think?"
            ah "Especially in the case of my dear Kaito-Kun~"

            menu:
                "How so?":
                    call ahLoveDecrease
                    call sbLoveIncrease
                    call loveNotification
                    show sb oh
                    p "I’m not following."

                    sb "Yeah…me neither."
                    sb "Can you say it in a more [sb]-themed way...~?"
                    show ah owo
                    "You notice Amari huffing as they flip at their hair."

                    ah "Is it not obvious?"
                    ah "This grand festival here is meant to serve as a place of new beginnings~!"
                    ah "Unfortunately, my beloved Kaito was unable to attend last year’s due to...ah."

                    show ah neutral
                    
                    extend "Well. I’ve been sworn to secrecy on that matter~"
                    ah "Let’s just say being able to witness the beauty this year in person..."
                    ah "Playing a role far better suited to a soft soul such as his~"
                    ah "Just seeing how utterly joyous my best friend was...I want to preserve it for the rest of eternity~!"
                "Is it because...":
                    call ahLoveIncrease
                    call sbLoveDecrease
                    call loveNotification

                    p "I’m assuming it’s because of the whole \"New Beginnings\" thing."

                    show sb thinking

                    sb "New beginnings?"
                    p "Yeah."
                    p "This festival is meant to symbolize all sorts of things..."
                    p "Romance...good health. You name it, it’s probably got some underlying meaning."

                    show ah happy

                    ah "Ah~ How perceptive of you, [playerName]~!"
                    ah "Yes. This year’s festival is to serve as my dear Kaito-Kun’s \"Fresh Start.\""
                    ah "A year where going forward…he will either choose to mend or permanently leave behind his past."

                    show ah shine

                    ah "I’m rather excited for it, you see~"

            show ah neutral

            ah "Though, I’d rather not bore you both with an ending prematurely stated."
            ah "Why don’t you both continue on your little \"date?\""
            ah "Bushi and I’ve some sightseeing to do~!"

            stop music fadeout 1.0
            hide ah
            show sb happy at center
            with dissolve

            "As Amari rides away on their stallion, [sb] takes your hand into their own."
            "You aren’t exactly a fan of the sudden touching, but you figured for the sake of your \"date,\" you’d allow it."
            $ renpy.music.play("audio/Music/Festival_FleetingBlossoms_V1.mp3", fadein=1.0,loop=True)

            if sbdecide and foodstalls and games == True:
                jump epilogue
            else:
                jump festivalactivities


        "Let [sb] decide." if sbdecide == False:
            if foodstalls or games == False:
                menu:
                    "Selecting this choice will advance the story. Are you sure you want to hang out with [sb] before doing the other activites?"
                    "Continue":
                        pass
                    "Complete other activites first.":
                        jump festivalactivities
            stop music fadeout 1.0
            $ sbdecide = True
            $ renpy.music.play("audio/Music/Sakura_Intro.ogg", fadein=1.0)
            $ renpy.music.queue("audio/Music/Sakura_Loop.ogg", clear_queue=False,loop=True,fadein=1.0)
            call sbLoveIncrease
            call loveNotification
            "Seeing little point in dragging this out any longer than necessary, you let [sb] take the lead."
            show sb blush
            "Clasping your hand firmly in their own, for the first time you notice that it’s much colder than before."
            sb "We’re going to get you those concert tickets."

            menu:
                "Question [sb]":
                    call sbLoveDecrease
                    call loveNotification
                    p "You’re rather serious all of a sudden."
                    p "You know, even if we can’t figure out your whole memory thing today, we still have next week."
                    "[sb] smiles at your optimism."
                    sb "Yeah~"
                    sb "But a promise is a promise!"
                    sb "I’m sure your mom would love to meet your suitor sooner rather than later, yeah~?"
                
                "Smile.":
                    call sbLoveIncrease
                    call loveNotification
                    "Your lips curl into a soft smile at [sb]'s determination."
                    "You decide to squeeze their hand."
                    p "You can cut with the face. We’ll get there eventually."
                    p "No need to rush things."
                    sb "Y-Yeah. I guess."

                    show sb oh

                    sb "But I’ll be really sad if I can’t at the very least find someone for you to think about going with!!"

                "Say nothing.":
                    "You use your free hand to pull out your phone."
                    "Briefly looking at the fictional men which graced your lock screen."
                    "You’re happy to see [sb] act so enthusiastically when it comes to supporting your interests."

            show sb neutral

            sb "Oi~ [playerName]."
            sb "You know, I’ve been thinking~"
            p "That’s dangerous."

            show sb thinking

            sb "Well, yeah! But this week’s just been so...crazy!"
            sb "It’s almost like it’s from one of those games you like."

            menu:
                "Agree with them.":
                    call sbLoveIncrease
                    call loveNotification

                    p "It’s not everyday some lunatic nearly crushes me and then claims to have no memories."
                    p "Not to mention, being roped into this whole \"Flour-Bomber\" deal."
                    p "Oh. And how could we forget about the horse?!"

                    show sb happy

                    "You see [sb] try not to laugh at your explanation of things."

                "Shrug.":
                    call sbLoveDecrease
                    call loveNotification

                    "You let out an exhausted sigh."
                    p "At this point, I just want this week to end..."
                    p "That way once this festival is over and done with, I can focus on one psycho instead of...three, was it?"

                    show sb ouch

                    "Shrugging your shoulders, you see [sb]'s face sour."

            sb "I just hope that sweet old lady doesn’t miss me too much."
            p "You mean the sweet shop lady?"
            p "I doubt she’ll be going anywhere anytime soon."
            p "Even once cherry blossoms go out of season, she usually switches to next season’s flavor–"

            show sb line

            sb "O-Or Mikael. With his whole flour spheal..."
            sb "A-And…even if they were a bit unhinged, I quite liked Kaito and Amari as well."

            show sb ouch

            sb "Everyone I met…I really hope they don’t forget..."

            menu:
                "[sb]...?":
                    call sbLoveIncrease
                    call loveNotification
                    p "Hey…you’re not…crying..are you?"
                    p "You were so happy earlier today."
                    p "You know I was joking about the whole you being a bother thing–"
                "You're being dramatic.":
                    call sbLoveDecrease
                    call loveNotification
                    p "You’re acting like you’re going to die or something."
                    p "Cut it out. I don’t like other people crying..."
                    p "We still have time. And even then–"
            stop music fadeout 1.0
            sb "It doesn’t matter anymore!"
            #*A CG Of SB smacking away the MC’s hand can be seen. They look frantic as tears stream down their cheeks.*
            p "?!?!"
            sb "You can’t bring back what wasn’t even there to begin with!"
            sb "That’s why I couldn’t remember..."
            sb "I’m just…I’m…!"
            "A series of loud bangs can be heard radiating through the area."
            "You instinctively turn your head towards its source."
            hide sb
            "However, when glancing back to check on [sb], you see that they’ve disappeared."
            "Seeing the disgruntled crowd of nearby people beginning to panic."

            jump epilogues



    







