# Music
################################################################################
label Music_ahTheme:
    play music "audio/Music/Amari_FleetingBlossoms_V1.mp3" volume 0.5 if_changed
    return
label Music_dayBegin:
    play music "audio/Music/DayBegins_FleetingBlossoms_V1.mp3" volume 0.5 if_changed
    return
label Music_pTheme:
    play music "audio/Music/MCTheme_FleetingBlossoms_V1.mp3" volume 0.5 if_changed
    return
label Music_maTheme:
    play music "audio/Music/Mikeal_FleetingBlossoms_V1.mp3" volume 0.5 if_changed
    return
label Music_sbTheme:
    play music "audio/Music/Sakura_FleetingBlossoms_V2.2.mp3" volume 0.5 if_changed
    return
label Music_ksTheme:
    play music "audio/Music/Kaito_FleetingBlossoms_V1.mp3" volume 0.5 if_changed
    return
label Music_cryTheme:
    play music "audio/Music/FleetingBlossoms_Sad.mp3" volume 0.5 if_changed
    return
label Music_kill:
    stop music fadeout 1.0
    return