def f(matn):
    sozlar = matn.split()  
    teskari_matn = ' '.join(sozlar[::-1])  
    return teskari_matn


matn = input("matn kiriting: ")
teskari = f(matn)
print(teskari)