label LoveNotifyTest:
    "Select a love"
    menu SelectLove:
        "Select a Love"
        "[sb], [ks], [ah], [ma] Love":
            call sbLoveIncrease
            call ksLoveIncrease
            call ahLoveIncrease
            call maLoveIncrease
            call loveNotification
        "[sb], [ks], [ah], [ma] Hate":
            call sbLoveDecrease
            call ksLoveDecrease
            call ahLoveDecrease
            call maLoveDecrease
            call loveNotification
        "[sb] and [ks] Hate, [ah] and [ma] Love ":
            call sbLoveDecrease
            call ksLoveDecrease
            call ahLoveIncrease
            call maLoveIncrease
            call loveNotification
    "Did it work?"
    "Did it work again?"
    menu LoveAgain:
        "Did it work again?"
        "[sb] Love":
            call sbLoveIncrease
            call loveNotification
        "[ks] Hate and [sb] Love":
            call sbLoveIncrease
            call ksLoveDecrease
            call loveNotification
    "God I hope so"
    return