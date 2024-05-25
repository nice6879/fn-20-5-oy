import time

def vaqtni_hisoblash(funksiya):
    def qurilmagan_funksiya(*args, **kwargs):
        boshlangich_vaqt = time.time()
        natija = funksiya(*args, **kwargs)
        tugash_vaqt = time.time()
        ish_vaqti = tugash_vaqt - boshlangich_vaqt
        print(f"{funksiya.__name__} ish vaqti: {ish_vaqti} soniya")
        return natija
    return qurilmagan_funksiya

@vaqtni_hisoblash
def masalan_funksiya():
    for i in range(1000000):
        pass

masalan_funksiya()
