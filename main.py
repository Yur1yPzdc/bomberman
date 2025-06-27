import json
from sys import exit


# Through Console
class bebra:
    def __init__(self, nuke_lv, guess):
        with open('nukes.json', 'r') as f:
            self.w = json.load(f)
        self.difficulty = nuke_lv
        self.guess = guess

    def do_smth(self):
        match self.difficulty:
            case 1:
                print(self.l1(self.guess))
            case 2:
                print(self.l2(self.guess))
            case 3:
                print(self.l3(self.guess))
            case 4:
                print(self.l4(self.guess))
            case 5:
                print(self.l5(self.guess))
            case _:
                print(0)


    def l1(self, guess):
        a = []
        if guess == self.w['L1'][0]:
            self.w['L1'].pop(0)
            return 'Correct!'
        for i in range(5):
            if self.w['L1'][0][i] == guess[i]:
                a.append(f'{i + 1}{i + 1}')
            elif guess[i] in self.w['L1'][0]:
                a.append(f'{i + 1}')
        return ' '.join(a)



    def l2(self):
        a = []
        if self.guess == self.w['L2'][0]:
            self.w['L2'].pop(0)
            return 'Correct!'
        for i in range(5):
            if self.guess[i] in self.w['L2'][0]:
                a.append(f'{i}')
        return ' '.join(a)


    def l3(self):
        if self.guess == self.w['L3'][0]:
            self.w['L3'].pop(0)
            return 'Correct!'
        return 'Less' if int(self.guess.lower(), base=25) < int(self.w['L3'][0], base=25) else 'More'


    def l4(self):
        if self.guess == self.w['L4'][0]:
            self.w['L4'].pop(0)
            return 'Correct!'
        return 'Less' if int(self.guess.lower(), base=36) < int(self.w['L4'][0], base=36) else 'More'


    def l5(self):
        if self.guess == self.w['L5'][0]:
            self.w['L5'].pop(0)
            return 'Correct!'
        return f'{len([i for i in self.guess if i in self.w["L5"][0]])}/8'


while True:
    q = input()
    if q.startswith('idi'):
        exit()
    if q.startswith('!nuke'):
        lv = int(q[1:].split()[1])
        guess = q[1:].split()[-1]
        huy = bebra(lv, guess)
        huy.do_smth()