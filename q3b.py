def add_binary(a, b):

    a = a[2:]
    b = b[2:]

    if len(a) < len(b):
        a = "0" * (len(b) - len(a)) + a
    else:
        b = "0" * (len(a) - len(b)) + b

    elde = 0
    sonuc = ""

    i = len(a) - 1

    while i >= 0:
        toplam = elde + (a[i] == "1") + (b[i] == "1")
        sonuc = str(toplam % 2) + sonuc
        elde = toplam // 2
        i -= 1

    if elde:
        sonuc = "1" + sonuc

    while len(sonuc) > 1 and sonuc[0] == "0":
        sonuc = sonuc[1:]

    return "0b" + sonuc

    
    
    


