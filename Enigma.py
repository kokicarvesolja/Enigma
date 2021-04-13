abeceda = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25
}

r1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9] 
r2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
r3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
r4 = [4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1]
r5 = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]

reflektor = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

vnos_uporabnika = 1
# začetne nastavitve 

# vrstni red rotorjev

def vrstni_red_rotorjev(vnos, rotor1, rotor2, rotor3, rotor4, rotor5):
    mesto = rotor1
    if vnos == "r1":
        mesto = rotor1
    elif vnos == "r2":
        mesto = rotor2
    elif vnos == "r3":
        mesto = rotor3
    elif vnos == "r4":
        mesto = rotor4
    elif vnos == "r5":
        mesto = rotor5
    return mesto

prvo_mesto = r1
drugo_mesto = r1
tretje_mesto = r1

izbira = ["r1", "r2", "r3", "r4", "r5"]


while prvo_mesto == drugo_mesto or prvo_mesto == tretje_mesto or drugo_mesto == tretje_mesto: 
    print("Kateri rotor naj bo na prvem mestu: ", izbira, "?")
    vnos_uporabnika1 = input()
    prvo_mesto = vrstni_red_rotorjev(vnos_uporabnika1, r1, r2, r3, r4, r5)
    izbira.pop(izbira.index(vnos_uporabnika1))
    print("Kateri rotor naj bo na drugem mestu: ", izbira, "?")
    vnos_uporabnika2 = input()
    drugo_mesto = vrstni_red_rotorjev(vnos_uporabnika2, r1, r2, r3, r4, r5)
    izbira.pop(izbira.index(vnos_uporabnika2))
    print("Kateri rotor naj bo na tretjem mestu: ", izbira, "?")
    vnos_uporabnika3 = input()
    tretje_mesto = vrstni_red_rotorjev(vnos_uporabnika3, r1, r2, r3, r4, r5)

# za obračanje obročev

def zasuk_rotorja_stevilo(izbran_rotor, prvi_rotor, drugi_rotor, tretji_rotor, cetrti_rotor, peti_rotor):
    if izbran_rotor == prvi_rotor:
        zasuk_pri = 17
    elif izbran_rotor == drugi_rotor:
        zasuk_pri = 5
    elif izbran_rotor == tretji_rotor:
        zasuk_pri = 22
    elif izbran_rotor == cetrti_rotor:
        zasuk_pri = 10
    elif izbran_rotor == peti_rotor:
        zasuk_pri = 0
    return zasuk_pri

zasuk_rotorja_1 = zasuk_rotorja_stevilo(prvo_mesto, r1, r2, r3, r4, r5)

zasuk_rotorja_2 = zasuk_rotorja_stevilo(drugo_mesto, r1, r2, r3, r4, r5)

print(zasuk_rotorja_1, zasuk_rotorja_2)

# položaj obročev 

def zasuk_obroca(rotor):
    print("Za koliko naj se zasuka obroč", rotor, "od 0 do 25?")
    zasuk = int(input())
    rotor = [x + zasuk for x in rotor]
    for _ in range(zasuk):
        rotor.insert(0, rotor.pop(25))
    if zasuk == 0:
        return rotor
    else:
        for i in range(len(rotor)):
            if rotor[i] >= 26:
                rotor[i] = rotor[i] - 26
        return rotor

#prvo_mesto = zasuk_obroca(prvo_mesto)
#drugo_mesto = zasuk_obroca(drugo_mesto)
#tretje_mesto = zasuk_obroca(tretje_mesto)

# menjava črk 

menjava_crk = {}

def fun_menjava_crk(slovar):
    kljuc = input("Katero črko želiš zamenjati? ")
    vrednost = input("S katero črko pa? ")
    slovar[kljuc] = vrednost

#for i in range(10):
    fun_menjava_crk(menjava_crk)
    print(menjava_crk)

# začetno stanje rotorjev

def obracanje_rotorja(vnos, rotor):
    if vnos == 0:
        return rotor
    else:
        for _ in range(vnos):
            rotor.append(rotor.pop(0))
        return rotor

print("Katero naj bo začetno mesto obračanja prvega rotorja?")
x = int(input(""))
prvo_mesto = obracanje_rotorja(x, prvo_mesto)

print("Katero naj bo začetno mesto obračanja drugega rotorja?")
y = int(input())
drugo_mesto = obracanje_rotorja(y, drugo_mesto)

print("Katero naj bo začetno mesto obračanja tretjega rotorja?")
z = int(input())
tretje_mesto = obracanje_rotorja(z, tretje_mesto)

# delovanje enigme - zasuk rotorjev (preden je črka pritisnjena)

def zasuk_rotorja(rotor):
    rotor.append(rotor.pop(0))
    return rotor


# delovanje enigme - črka

# skozi rotorje 

def pogled_v_slovar(rotor, crka): 
    return rotor[abeceda[crka]] # pogleda vrednost ključa crke v slovarju in ga kot indeks r1 vrne

def signal_skozi_rotor(rotor, indeks):
    return rotor[indeks]

def dolocitev_pravega_indeksa(zamik,indeks):
    pravi_indeks = indeks - zamik
    if pravi_indeks < 0:
        pravi_indeks += 26
    return pravi_indeks

def signal_skozi_rotorje(vnos, zamik1, zamik2, zamik3, prvi_rotor, drugi_rotor, tretji_rotor):
    indeks_prvega_rotorja = pogled_v_slovar(prvi_rotor,vnos)
    indeks_za_drugi_rotor = dolocitev_pravega_indeksa (zamik1, indeks_prvega_rotorja)
    indeks_drugega_rotorja = signal_skozi_rotor(drugi_rotor, indeks_za_drugi_rotor)
    indeks_za_tretji_rotor = dolocitev_pravega_indeksa (zamik2, indeks_drugega_rotorja)
    indeks_tretjega_rotorja = signal_skozi_rotor (tretji_rotor, indeks_za_tretji_rotor)
    indeks_za_reflektor = dolocitev_pravega_indeksa(zamik3, indeks_tretjega_rotorja)
    return indeks_za_reflektor

# reflektor 

def skozi_reflektor(reflektor, indeks):
    return reflektor[indeks] # pogleda, katera vrednost je shranjena v reflektorju pod določenim indeksom 

# nazaj od reflektorja 

def nazaj_skozi_rotor(rotor, vrednost): # funkcija za to, ko se signal vrača nazaj od reflektorja
    return rotor.index(vrednost)

def dolocitev_pravega_indeksa_vracanje(zamik, indeks):
    pravi_indeks = indeks + zamik
    if pravi_indeks > 25:
        pravi_indeks -= 26
    return pravi_indeks

def nazaj_skozi_rotorje(indeks_reflektorja, zamik1, zamik2, zamik3, prvi_rotor, drugi_rotor, tretji_rotor): # signal se vrača nazaj iz reflektorja do abecede
    indeks_za_tretji_rotor = dolocitev_pravega_indeksa_vracanje (zamik3, indeks_reflektorja)
    indeks_tretjega_rotorja = nazaj_skozi_rotor (tretji_rotor, indeks_za_tretji_rotor)
    indeks_za_drugi_rotor = dolocitev_pravega_indeksa_vracanje (zamik2, indeks_tretjega_rotorja)
    indeks_drugega_rotorja = nazaj_skozi_rotor (drugi_rotor, indeks_za_drugi_rotor)
    indeks_za_prvi_rotor = dolocitev_pravega_indeksa_vracanje (zamik1, indeks_drugega_rotorja)
    indeks_prvega_rotorja = nazaj_skozi_rotor (prvi_rotor,indeks_za_prvi_rotor)
    return indeks_prvega_rotorja

def izpisovanje_crke (slovar, iskana_crka):
    kljuci = list(slovar.keys())
    vrednosti = list(slovar.values())
    crka = kljuci[vrednosti.index(iskana_crka)]
    return crka

def fun_sprememba_crke(crka, slovar):
    if crka in slovar:
        sprememba_crke = slovar[crka]
    elif crka in slovar.values():
        sprememba_crke = izpisovanje_crke(slovar,crka)
    else:
        sprememba_crke=crka
    return sprememba_crke

def drugi_rotor_se_zasuka(rotor, zasuk_pri, zamik1, zamik2):
    if zamik1 == zasuk_pri:
        zasuk_rotorja(rotor)
        zamik2 += 1
        return zamik2, rotor
    else:
        return zamik2, rotor

def tretji_rotor_se_zasuka(rotor, zasuk_r1, zasuk_r2, zamik, zamik1, zamik2):
    zasuk_r1 += 1
    zasuk_r1 %= 25
    if zamik == zasuk_r1 and zamik1 == zasuk_r2:
        zasuk_rotorja(rotor)
        zamik2 += 1
        return zamik2, rotor
    else:
        return zamik2, rotor

def nastavitev_zamika(zamik):
    zamik += 1
    if zamik >= 26:
        zamik = 0
    return zamik

def zasuk_za_drugi(zasuk):
    zasuk -= 1
    if zasuk < 0:
        zasuk = 25
    return zasuk


stevilo_vnosov = 0

zamik_r1 = x
zamik_r2 = y
zamik_r3 = z

print("1: ", tretje_mesto)

if zamik_r2 == zasuk_za_drugi(zasuk_rotorja_2) :
    zasuk_rotorja(tretje_mesto)
    zamik_r3 += 1

print("2: ", tretje_mesto)

while vnos_uporabnika != 0:
    zasuk_rotorja(prvo_mesto)
    zamik_r1 = nastavitev_zamika(zamik_r1)
    if zamik_r2 == zasuk_za_drugi(zasuk_rotorja_2):
        zasuk_rotorja(drugo_mesto)
        zamik_r2 = nastavitev_zamika(zamik_r2)
    print("Zamik_r2 = ", zamik_r2)
    #print("zasuk 1: ", zasuk_rotorja_1, "zasuk 2: ", zasuk_rotorja_2 )
    zamik_r2, drugo_mesto = drugi_rotor_se_zasuka(drugo_mesto, zasuk_rotorja_1, zamik_r1, zamik_r2)
    zamik_r3, tretje_mesto = tretji_rotor_se_zasuka(tretje_mesto, zasuk_rotorja_1, zasuk_rotorja_2, zamik_r1, zamik_r2, zamik_r3)
    print("Zamik_r1 = ", zamik_r1,"Zamik_r2 =", zamik_r2, "Zamik_r3 = ",zamik_r3)
    vnos_uporabnika = input("Vnesi malo tiskano črko za šifriranje: ")
    stevilo_vnosov += 1
    prva_sprememba_crke = fun_sprememba_crke(vnos_uporabnika, menjava_crk)
    r_indeks = signal_skozi_rotorje(prva_sprememba_crke, zamik_r1, zamik_r2, zamik_r3, prvo_mesto, drugo_mesto, tretje_mesto) # indeks za reflektor
    n_indeks = skozi_reflektor(reflektor, r_indeks) # vrednost, ki je shranjena pod indeksom reflektorja
    a_vrednost = nazaj_skozi_rotorje (n_indeks, zamik_r1, zamik_r2, zamik_r3, prvo_mesto, drugo_mesto, tretje_mesto)
    zadnja_sprememba = izpisovanje_crke(abeceda, a_vrednost)
    print(fun_sprememba_crke(zadnja_sprememba, menjava_crk))