#*Depending on who the MC chooses here, this will lead into that respective character's Epilogue. If the MC has not built up enough affection with said character. They will fail to find said character, and they will end up deciding to return to the Sakura blossom tree in hopes of seeing SB there, where they will just be met with a single branch in front of it.* 

# For the demo, we will only include the scenario where the player successfully finds the player. Post-jam, we will add in the point conditional for the good end.

label epilogues:
    menu:
        "Sensing that this could be important, you decide the following:"
        "Look for [sb].":
            call sbLoveIncrease
            p "W-Where the Hell did they go!?"
            "Quickly scrambling to find where [sb] went, you check the spots which you knew were of interest to them."
            scene BG YYFront:
                pos (-18, -189) zoom 1.29 
            with dissolve
            p "Not here." #Food stand is shown
            scene BG YYFront:
                pos (-18, -270) zoom 1.29 xzoom -1.0
            with dissolve
            p "Nothing here either..." #The game stand is shown
            scene BG YYFront:
                xpos -531 ypos -270 zoom 1.29
            with dissolve
            p "What about here?" #*The Streets leading into the School Entrance are shown*
            "After what seems like an eternity of searching, the sun begins to set."
            "With only one place left in mind, you figure it'd be your last attempt for the day."
            p "If you aren't here...I don't know where you'd be."
            scene BG YYFront:
                zoom 1.0 pos (0,0)
            with dissolve
            #*The Sakura Tree where you first met SB is shown*
            "Making your way through the fields leading up to the campus Cherry Blossom Tree, your eyes widen."
            p "[sb]?"
            #*A CG of SB facing away from the MC is shown. Their head is turned slightly as if they just noticed you. A soft pink glow is enveloping them while blossoms flutter around them.*
            show sb oh at center with dissolve:
                alpha 0.87
                matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.12)*HueMatrix(0.0)
                parallel:
                    ease 0.8 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.15)*HueMatrix(0.0)
                    pause 0.5
                    ease 0.8  matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.04)*HueMatrix(0.0)
                    pause 0.5
                    repeat
            sb "I'm sorry…my friend."
            sb "I didn't want you to see me like this."
            "Your legs begin to move on their own."
            "Despite this, it felt like no matter how fast you ran, [sb] was still an eternity away from your reach."
            sb "I wish I'd realized sooner."
            sb "That our time together...was to be so short."
            sb "At first I didn't wanna believe it."
            sb "It's why I tried."
            sb "I really, really tried."
            sb "I wanted to be your friend."
            sb "With or without my memories…even if they were never around to begin with–"
            show sb annoyed
            p "[sb]!!!!!!" with vpunch
            "The glow around [sb] grows more intense."
            "So much so, you can see the sakura petals starting to pass through them with ease."
            "You never ran so fast in your life."
            "In fact, as you closed in on [sb], you completely disregard how your phone had long since fallen from your pocket."
            "Deciding to take a leap of faith, you lunge to pull [sb] into your embrace."
            "You're glad to hear them wince as you both tumble to the ground below."
            sb "[p]."
            p "Don't \"[p]\" me!!!"
            p "Whatever the fuck is going on, I don't want to hear it."
            p "We {i}are{/i} friends. And I'll be damned if I let you go!"
            show sb oh
            sb "B-But–"
            p "I've finally got someone who even if they've got a few screws left loose, I can look forward to seeing them everyday!"
            p "I may not always act like it, but I grew attached, okay?!"
            p "You mean to tell me after all that, I won't get to even take you to the stupid Idol Concert!?!"
            p "Doesn't that sound like some sort of cruel joke?!?!?!"
            show sb excited
            "You watch as [sb]'s sonce solemn expression lights up beneath you."
            show sb blush
            "They sigh, lifting one of their free hands up to gently caress your cheek."
            "This time, you can't feel it."
            sb "You're telling me..."
            sb "I know this sounds rather cheesy, but, even if I go away…you still have the others, yeah?"
            sb "You gotta make sure they don't forget me, ahaha~"
            sb "I'm sure that as long as I'm in your memories, then I won't ever truly be gone."
            sb " At least…that's what I'm going to tell myself."
            #*A final CG of a nearly full transparent SB on the ground smiling can be seen. Sakura petals are surrounding them, and their hand appears to be gingerly wiping away at some of your tears. Lanterns seem to be floating in the sky around you both.*
            sb "I'm gonna tell myself, that this isn't how it ends."
            sb "So I'm going to need you to do that too."
            sb "As hard as that'll be…"
            sb "Wait for me, promise?"
            hide sb with Dissolve(1.5)
            "As you nod your head in response, you watch as [sb]'s form disappears in its entirety."
            "Leaving only their Sakura branch behind, you can't find the strength to keep yourself up right any longer, and instead flop pathetically to your side."
            "Letting the night take its course."

            $ quick_menu = False
            window auto hide
            scene black with Dissolve(2.0)
            show text "To be continued..." with dissolve
            pause 3.0
            hide text with Dissolve(1.0)
            stop music fadeout 3.0
            pause 4.0
            return
        "Look for Kaito.":
            p "W-Where the Hell did they go!?"
            scene BG YYFront:
                pos (-18, -270) zoom 1.29 xzoom -1.0
            with dissolve
            "Quickly scrambling to find where [sb] went, you check the spots you knew were of interest to them."
            "However, after what seemed like an eternity of searching with little to no results, you find yourself letting out a pathetic whine as you plop onto a nearby bench."
            p "This is absolutely not how I wanted to go about spending the rest of my day..."
            $ k_name = "???"
            ks "For once it seems like we can {i}agree{/i} on something."
            #A CG of Kaito sitting right next to you can be seen. You're both on some bench in the streets leading up to the Campus. It's nighttime, and lanterns are all floating in the dark sky around you. They're looking off ahead, their mask tossed aside and with a stoic look to them. Their lips also appear bruised.
            $ renpy.music.play("audio/Music/EndingKaito_FleetingBlossoms_Intro.ogg", fadein=1.0)
            $ renpy.music.queue("audio/Music/EndingKaito_FleetingBlossoms_Loop.ogg", clear_queue=False,loop=True)
            scene BG YYFront:
                zoom 1.0 pos (0,0)
            show ks neutral at center
            with dissolve
            p "Your mask..."
            $ k_name = "Kaito"
            ks "There's no longer a need for it."
            "While Kaito's jaw remained firmly clenched, his eyes seemed to glisten with a story untold."
            "Of all the people who could have joined you in your misery, you were comforted in the fact that Kaito wouldn't make dramatics from it."
            show ks bashful
            ks "This has been quite the week, wouldn't you agree?"
            ks "Going from some random wallflower to someone worth remembering."
            ks "Does it not make you feel like the Protagonist of some cheesy slice of life anime?"
            "You hang your head at Kaito's repeated reference."
            "Though, you'd be lying if it wasn't a welcome distraction at the moment."
            p "I guess."
            p "At least in those anime, the main character's companion doesn't disappear on the last day…"
            show ks neutral
            ks "Oh, on the contrary."
            ks "You see there are plenty of tales which end on the more bittersweet note."
            ks "Beating Angels, Titan Attack, Fairy Tale–"
            show ks happy
            ks "Ah… forgive me. Perhaps this is a conversation for another time."
            ks "Now that I think about it, this is the first time we have truly had the chance to speak one on one."
            ks "I almost don't know what else to say…"
            ks "I've no reason to chastise, nor ridicule you for the matter."
            ks "I suppose I can simply enjoy what time we have, embracing one another's presence."
            "You feel Kaito's weight shift so that the side of his face is resting on your shoulder."
            "The air around you feels so still that you can easily hear the man's light breaths."
            "He looks tired."
            p "I'm assuming this is the first time you've had a moment to rest in a hot minute, huh."
            p "What ever happened to Mikael's big \"stunt?\""
            p "I'm assuming those bangs earlier were from him."
            show ks angry
            ks "He was a fool, that's what."
            ks "Trying to carry over 80 kilograms worth of wooden crates. Unbelievable."
            ks "It wouldn't be the first time he's done something stupid."
            ks "Won't be the last either."
            #*A CG of the sky with hundreds of floating lanterns appears. You're watching from the perspective of Kaito and you sitting on the bench, with the addition of bustling city life going on around you all*
            show ks neutral
            "Kaito lets his eyes briefly flutter open."
            "Taking in the beauty of the night time lanterns, you see his face brighten like a child getting to see their favorite toy."
            show ks blush
            ks "Say...[p]."
            ks "I know this is rather forward, but Mikael had informed me of your need for a \"concert partner.\""
            ks "I understand with how I've acted towards you and [sb], that I would most likely not be your first choice."
            ks "However, if it means anything, I…would love to at the very least make amends in the form of my passion for the local Idol scenery."
            ks "Perhaps you, myself, and [sb] may attend together, even."
            "Your frown at the mention of your currently missing friend."
            "However, with how genuine Kaito was being, rather than remind them of their disappearance, you instead nod."
            "Taking Kaito's hand into your own, you give it a firm squeeze."
            p "Well all go then."
            p "Mikael and Amari, too."
            show ks happy
            ks "Fufufu~ It's a date, then."

            $ quick_menu = False
            window auto hide
            scene black with Dissolve(2.0)
            show text "To be continued..." with dissolve
            pause 3.0
            hide text with Dissolve(1.0)
            stop music fadeout 3.0
            pause 4.0
            return
        "Look for Mikael.":
            scene BG YYFront:
                pos (-18, -270) zoom 1.29 xzoom -1.0
            with dissolve
            "Quickly scrambling to find where [sb] went, you check the spots you knew were of interest to them."
            "However, after what seemed like an eternity of searching with little to no results, you find yourself letting out a pathetic whine while flopping face first into some grass."
            $ m_name = "???"
            ma "You and me both~"
            $ renpy.music.play("audio/Music/EndingMikael_FleetingBlossoms_Intro.ogg", fadein=1.0)
            $ renpy.music.queue("audio/Music/EndingMikael_FleetingBlossoms_Loop.ogg", clear_queue=False,loop=True)
            scene BG YYFront:
                zoom 1.0 pos (0,0)
            show ma neutral at center
            with dissolve
            #*A CG of Mikael lying right next to you on the grass can be seen. Their hair is a mess as they happily cast an almost unhinged grin your way. They have Sakura petals stuck in their hair, but their cheek appears slightly swollen.*
            $ m_name = "Mikael"
            p "Guessing your plan didn't work out?"
            show ma wink1
            ma "Oh no. It worked."
            ma "It really worked. If ya catch my drift~"
            "Mikael cackles while rolling themselves around some more in the grass."
            "You were about to question the manic, but were stopped by a firm grasp at your shoulders."
            show ma neutral2
            ma "Tell me, have you managed to find your concert partner yet?!"
            ma "Ya see, following the execution of my grand scheme, I went ahead and told anyone I saw of your woes!"
            show ma angry
            ma "...unfortunately there were no takers."
            ma "Well, Kaito, maybe."
            show ma wink1
            ma "But I doubt he'll be free any time soon with the magic I worked~"
            ma "Despite droppin' those crates, I'd call my plan a raging success!" 
            #*A CG of Mikael pulling you close as you both look up at the night sky is displayed. He's pointing out the many lanterns that are floating by with a manic look to his eye. The few that are visible in the background have a hand painted Kaito on it. Meanwhile the MC is still sweating at being touched so intimately.*
            show ma wink2
            ma "See that, [p]???"
            ma "That's all me!"
            ma "Hundreds of lanterns, each hand crafted with the Mikael Amoris touch~"
            ma "Honestly, wouldn't have been possible without you and Flower Boy~"
            show ma neutral
            ma "Say...where'd they go anyways?"
            ma "Didn't think I'd see ya without ‘em."
            "You frown at the mention of [sb]."
            "You can't help but think of their final words."
            "They were almost like a goodbye left unsaid."
            p "It's...a long story."
            p "I haven't been able to find [sb] since the sun was up..."
            p "Part of me wonders if they'll even come back."
            p "What if I never see them again?"
            p "How could someone just upright {i}abandon{/i} someone like that–??"
            ma "Hey."
            show ma blush
            ma "If it means somethin'. I ain't ever gonna abandon ya."
            ma "Trust me, I know that feelin' all too well."
            ma "Hurts like Hell."
            ma "Makes ya wanna scream, {i}punch{/i} somethin' even...!"
            ma "But…I don't feel like Flower Boy would just up ‘n leave without a good reason."
            ma "Guys' too soft for that sort'a stuff."
            "Mikael meets your gaze."
            "It's intense."
            "Too intense."
            "You could tell however that even if you tried looking away, that the man wasn't going to let you go."
            ma "I'll tell ya what."
            ma "Why don't {i}I{/i} be your concert partner?"
            ma "That way, when [sb] sees us all happy together, they're gonna just come runnin' back!!"
            ma "And if they don't~"
            show ma wink2
            ma "Then I, Mikael Amoris, President of YuraYura's Baking Club will personally make them!"
            ma "We're gonna do {i}great{/i} things together, [p]."
            ma "I just know we will."
            ma "Kyeheha!!!"

            $ quick_menu = False
            window auto hide
            scene black with Dissolve(2.0)
            show text "To be continued..." with dissolve
            pause 3.0
            hide text with Dissolve(1.0)
            stop music fadeout 3.0
            pause 4.0
            return
        "Look for Amari.":
            scene BG YYFront:
                pos (-18, -270) zoom 1.29 xzoom -1.0
            with dissolve
            "Quickly scrambling to find where [sb] went, you check the spots you knew were of interest to them."
            scene BG YYFront with dissolve:
                zoom 1.0 pos (0,0)
            "However, after what seemed like an eternity of searching with little to no results, you find yourself letting out a pathetic whine while slumping against some nearby wall."
            $ a_name = "???"
            ah "Oh my~ How uncomfortable you look~"
            $ renpy.music.play("audio/Music/EndingAmari_FleetingBlossoms_Intro.ogg", fadein=1.0)
            $ renpy.music.queue("audio/Music/EndingAmari_FleetingBlossoms_Loop.ogg", clear_queue=False,loop=True)
            #*A CG of Amari is shown. They've taken to sitting next to you, with Bushi nearby munching on what appears to be some Sakura petals. Amari is positioned so that they've a hand on their forehead in a rather dramatic fashion.*
            show ah happy at center with dissolve
            $ a_name = "Amari"
            ah "Allow us to join you!"
            "Bushi huffs. It seems they'd rather focus on their evening snack than her owner's antics."
            show ah dramatic with Dissolve(0.3)
            ah "That look of dread..."
            ah "The utter sense of sorrow...!"
            show ah neutral with Dissolve(0.3)
            ah "While I'd {i}love{/i} to see more of it, something tells me you need a bit more than that."
            ah "Tell me, my beloved [p], what has you so glum?"
            ah "Where is your knight clad in an armor of cherry blossoms when you need them most~!?!"
            p "I wish I could tell you."
            p "Though I'm starting to think they'll never come back."
            show ah angry
            "Amari laughs, however it seems your bluntness has them slightly off beat from their usual flair."
            ah "How depressing…"
            ah "I rather liked [sb], too."
            ah "The way which they stirred the pot in my beloved Kaito-Kun's world truly made their presence an unforgettable experience~"
            ah "Though, I digress."
            show ah happy
            ah "I've something far better to show you."
            #*A CG of Amari forcibly grabbing your chin to look up at the sky can be seen. Countless lanterns are making their way across it. The light is enough to illuminate even the dingy dark place which you decided to haul yourself away to. Bushi is still in the background too cause we love her.*
            show ah blush
            ah "Look~!"
            ah "How utterly vibant it all is."
            ah "Countless lanterns, each said to hold a piece of it's maker's dreams~"
            ah "A truly spectacular way to conclude this year's cherry blossom season, no?"
            ah "These moments truly are fleeting, after all~"
            ah "It'd be a shame to miss it in your moment of despair."
            p "But–"
            show ah happy
            ah "But how can you expect to enjoy it without your once companion, you may ask??"
            ah "Simple!"
            "You watch as a manic grin crosses Amari's face as they pull you up from your spot."
            #*A CG of Amari holding you Waltz style is shown. The MC looks nervous while Amari has that fire look in their eyes.*
            show ah dramatic with Dissolve(0.3)
            ah "{i}I{/i} shall play that part."
            ah "After all, I'm quite the actress~"
            ah "With my dear Kaito-Kun tying up his spare ends, I'm afraid I've quite a lot of time to spend with my newfound friend."
            ah "You've that concert to go to as well."
            show ah blush with Dissolve(0.3)
            ah "Ahhh~ The memories we shall make~!"
            ah "I'll even paint my nails for the occasion!!"
            ah "I'm sure, once [sb] sees how much more of a {i}wonderful{/i} companion I am, they'll come rushing back in no time~"
            ah "And if not, then I, Amari Haruka, shall be your new best friend!"

            $ quick_menu = False
            window auto hide
            scene black with Dissolve(2.0)
            show text "To be continued..." with dissolve
            pause 3.0
            hide text with Dissolve(1.0)
            stop music fadeout 3.0
            pause 4.0
            return