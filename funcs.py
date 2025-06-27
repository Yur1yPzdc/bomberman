def l1(w, guess):
    assert len(w['L1']), 'Больше нет'
    a = []
    if guess == w['L1'][0]:
        w['L1'].pop(0)
        return 'Correct!'
    for i in range(5):
        if w['L1'][0][i] == guess[i]:
            a.append(f'{i + 1}{i + 1}')
        elif guess[i] in w['L1'][0]:
            a.append(f'{i + 1}')
    return ' '.join(a)


def l2(w, guess):
    assert len(w['L2']), 'Больше нет'
    a = []
    if guess == w['L2'][0]:
        w['L2'].pop(0)
        return 'Correct!'
    for i in range(5):
        if guess[i] in w['L2'][0]:
            a.append(f'{i}')
    return ' '.join(a)


def l3(w, guess):
    assert len(w['L3']), 'Больше нет'
    if guess == w['L3'][0]:
        w['L3'].pop(0)
        return 'Correct!'
    return 'Less' if int(guess.lower(), base=25) < int(w['L3'][0], base=25) else 'More'


def l5(w, guess):
    assert len(w['L4']), 'Больше нет'
    if guess == w['L4'][0]:
        w['L4'].pop(0)
        return 'Correct!'
    return 'Less' if int(guess.lower(), base=36) < int(w['L4'][0], base=36) else 'More'


def l4(w, guess):
    assert len(w['L5']), 'Больше нет'
    if guess == w['L5'][0]:
        w['L5'].pop(0)
        return 'Correct!'
    return f'{len([i for i in guess if i in w["L5"][0]])}/8'
