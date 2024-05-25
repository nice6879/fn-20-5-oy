import random

def togrilikni_tekshirish(funksiya):
    def tekshiruv_funksiyasi(*args, **kwargs):
        savol, togrisini_tanlash = funksiya(*args, **kwargs)
        javob = int(input(savol))
        if javob == togrisini_tanlash:
            print("To'g'ri!")
        else:
            print("Noto'g'ri!")
    return tekshiruv_funksiyasi

@togrilikni_tekshirish
def matematik_savol():
    
    savol1 = random.randint(1, 10)
    savol2 = random.randint(1, 10)
    oper = random.choice(('+', '-', '*'))
    if oper == '+':
        togrisini_tanlash = savol1 + savol2
    elif oper == '-':
        togrisini_tanlash = savol1 - savol2
    else:
        togrisini_tanlash = savol1 * savol2
    return f"{savol1} {oper} {savol2} = ?", togrisini_tanlash


matematik_savol()