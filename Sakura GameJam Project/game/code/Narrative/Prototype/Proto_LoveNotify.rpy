label LoveNotifyTest:
    "Select a love"
    menu SelectLove:
        "Select a Love"
        "[sb], [ks], [ah], [ma] Love":
            call sbLoveIncrease from _call_sbLoveIncrease_22
            call ksLoveIncrease from _call_ksLoveIncrease_12
            call ahLoveIncrease from _call_ahLoveIncrease_16
            call maLoveIncrease from _call_maLoveIncrease_13
            call loveNotification from _call_loveNotification_59
        "[sb], [ks], [ah], [ma] Hate":
            call sbLoveDecrease from _call_sbLoveDecrease_14
            call ksLoveDecrease from _call_ksLoveDecrease_6
            call ahLoveDecrease from _call_ahLoveDecrease_10
            call maLoveDecrease from _call_maLoveDecrease_6
            call loveNotification from _call_loveNotification_60
        "[sb] and [ks] Hate, [ah] and [ma] Love ":
            call sbLoveDecrease from _call_sbLoveDecrease_15
            call ksLoveDecrease from _call_ksLoveDecrease_7
            call ahLoveIncrease from _call_ahLoveIncrease_17
            call maLoveIncrease from _call_maLoveIncrease_14
            call loveNotification from _call_loveNotification_61
    "Did it work?"
    "Did it work again?"
    menu LoveAgain:
        "Did it work again?"
        "[sb] Love":
            call sbLoveIncrease from _call_sbLoveIncrease_23
            call loveNotification from _call_loveNotification_62
        "[ks] Hate and [sb] Love":
            call sbLoveIncrease from _call_sbLoveIncrease_24
            call ksLoveDecrease from _call_ksLoveDecrease_8
            call loveNotification from _call_loveNotification_63
    "God I hope so"
    return