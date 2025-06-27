NUKES:
    L1:
        Symbols: 1234567890 [10]
        Guess: XXXXX (18256)
        Rules: No repeat; Double if place+num; Single if num
        Possible guess: 13845 (18256) -> 11, 3, 5
        Gives: 1 Part
    L2:
        Symbols: 1234567890 [10]
        Guess: XXXXX (18286)
        Rules: Repeat; Sungle if num or if num+place
        Possible guess: 13845 (18286) -> 1, 3
        Gives: 2 Parts
    L3:
        Symbols: 1234567890ABCDEFGHIJKLMNO [25]
        Guess: XXXXXXXX (2G65F3AB)
        Rules: No repeat; More Less
        Possible guess: 345HB7KI (2G65F3AB) -> Less
        Gives: 2-3 Parts
    L5:
        Symbols: 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ [36]
        Guess: XXXXXXXXXX (HB097V28)
        Rules: No repeat; More Less
        Possible guess: W3O947V6 (HB097V28) -> Less
        Gives: 4 Parts
    L4:
        Symbols: 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ [36]
        Guess: XXXXXXXX (HB097V28)
        Rules: Repeat; Single if sym exists and in place
        Possible guess: W3O947V6 (HB097V28) -> 1/8
        Gives: 3 Parts


Commands:
    !Nuke {lv} {guess}