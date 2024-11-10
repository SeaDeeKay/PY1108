# --- feladatok 01 / 1 (lakcím) ---------
# print("Add meg a következő adatokat:")

# iranyito = input("Irányítószám: ")
# varos = input("Város: ")
# utca = input("Közterület neve: ")
# hazszam = input("Házszám: ")

# print(f"az ön lakcíme: {iranyito} {' '} {varos} {' '} {utca} {' '} {hazszam} {' '}")

# --- feladatok 01 / 2 (nevek) ---------

# vn = input("Vezetéknév:")
# vn2 = input("Vezetéknév2:")
# kn = input("Keresztnév: ")
# kn2 = input("Keresztnév2: ")

# print('képezhető nevek: ')
# print(f'{vn} {kn}')
# print(f'{vn} {kn2}')
# print(f'{vn2} {kn}')
# print(f'{vn2} {kn2}')

# --- feladatok 01 / 3 (fizetes) ---------

# havi = int(input("Írd be a havi fizetésed:"))

# print(f"A te éves fizetésed: {12 * havi} HUF")

# --- feladatok 01 / 4 (euro) ---------

# eu_arf = int(input('Hány forint egy dollár? '))
# eu_menny = int(input('Hány dollárt szeretnél átváltani? '))

# print(f'Az általad átváltani kívánt euró mennyiségének értéke: {eu_arf * eu_menny}$')

# --- feladatok 01 / 5 (teglalap_ker_ter) ---------

# print('Írd be a téglalp oldalainak hosszát!')

# a = int(input('A téglalap "a" oldala: '))
# b = int(input('A téglalap "b" oldala: '))

# print(f'A téglalap területe: {a * b} cm2')
# print(f'A téglalap kerülete: {2 * (a + b)} cm')

# --- feladatok 01 / 6 (kor_ker_ter) ---------

# from math import pi

# print('Írd be a kör sugarának hosszát!')
# r = float(input('r = '))
# print(f'kör területe: {2 * r * pi:.2f} cm2')
# print(f'kör kerülete: {round(r ** 2 * pi, 4)} cm')

# ts = float(input('testsúly (kg): '))
# mag = int(input('magasság (cm): ')) / 100

# tti = ts / mag ** 2

# print('a testsúlyosztályod:', end='')
# if tti < 16: print('súlyosan sovány vagy')
# elif tti < 17: print('mérsékelten sovány vagy')
# elif tti < 18.5: print('enyhén sovány vagy')
# elif tti < 25: print('normál testsúly')
# elif tti < 30: print('túlsúlyos')
# elif tti < 35: print('elsőfokú elhízás')
# elif tti < 40: print('másodfokú elhízás')
# else: print('súlyos elhízás')

# --- feladatok 01 / 11 (zoldseges) ---------

# print('Alma ára (/kg): 350 HUF')
# print('Szőlő ára (/kg): 550 HUF')
# print('Szilva ára (/kg): 450 HUF')

# alma_ar = 350
# szilva_ar = 450
# szolo_ar = 550

# termek = str(input('Mit szeretnél vásárolni? '))
# menny = float(input('Mennyit szeretnél vásárolni (kg)? '))

# if termek == 'szőlőt':
#     print(f'ár: {round(menny * szolo_ar, 0)} HUF')
# elif termek == 'szilvát':
#     print(f'ár: {round(menny * szilva_ar, 0)}')
# elif termek == 'almát':
#     print(f'ár: {round(menny * alma_ar, 0)}')
# else:
#     print('Ilyen termékünk sajnos nincs az üzletben.')

# --- feladatok 01 / 12 (hordo) ---------

# hordo_V = int(input('Mennyi egy hordó térfogata (l)?: '))
# kancso_V = int(input('Mennyi egy kancsó térfogata (l)?: '))

# print(f'A hordóból kimérhető teli kancsók száma: {round(hordo_V / kancso_V, 0)} ')
# print(f'A hordóban maradt folyadék mennyisége: {hordo_V % kancso_V}')
# print(f'A hordó és a kancsó hányadosa: {hordo_V / kancso_V:.2f}')

# --- feladatok 01 / 13 (bankjegy) ---------

# print('Bankjegyautomata')
# print(' ')
# print('A legkisebb címlet 1000 Ft, a maximálisan felvehető összeg 300 000 Ft.')
# print(' ')

# osszeg = int(input('Adja meg mekkora összeget kíván felvenni! '))

# print(' ')
# print('A kiadott bankjegyek:')
# print(' ')

# if (osszeg % 10000) == 0:
#     print(f'{osszeg / 10000} * 10 000 = {osszeg}')
# elif (osszeg % 10000) != 0 and ((osszeg % 10000) % 5000) == 0:
#     print(f'{osszeg // 10000} * 10 000 = {(osszeg // 10000) * 10000}')
#     print(f'{(osszeg % 10000) / 5000} * 5000 = {(osszeg % 10000)}')
# elif (osszeg % 10000) != 0 and (osszeg % 5000) != 0 and (osszeg % 1000) == 0:
#     print(f' {osszeg // 10000} * 10 000 = {(osszeg // 10000) * 10000}')
#     print(f' {(osszeg % 10000) // 5000} * 5 000 = {((osszeg % 10000) // 5000) * 5000}')
#     print(f' {round((osszeg % 5000) / 1000)} * 1 000 = {osszeg % 5000}')
# elif (osszeg % 10000) != 0 and (osszeg % 5000) != 0 and (osszeg % 1000) != 0:
#     print('A legkisebb felvehető összeg 1000 Ft!')

# print(' ')
# if (osszeg % 10000) == 0 or (osszeg % 5000) == 0 or (osszeg % 1000) == 0:
#     print(f'Összeg: {osszeg} Ft')
# elif (osszeg % 10000) != 0 and (osszeg % 5000) != 0 and (osszeg % 1000) != 0:
#     print ('Összeg: 0 Ft')

# --- feladatok 01 / 14 (utazasikoltseg) ---------

# print('Utazási költségtérítés')
# print()

# ut = float(input('Add meg a megtett utat km-ben! '))
# fogyasztas = float(input('Add meg az autó fogyasztását 100 km-re literben! '))
# ar = float(input('Add meg az üzemanyagárat ft-ban! '))
# kt = (ut * fogyasztas * ar) / 100

# if ut > 100:
#     print(f'Költségtérítés: {kt + ut * 25} ft')
# else:
#     print(f'Költségtérítés: {(ut * fogyasztas * ar) / 100} ft.')

# --- feladatok 01 / 18 (paritas) ---------

# szam = int(input('Adj meg egy egész számot! '))

# if szam % 2 == 0:
#     print('A szám páros.')
# else:
#     print('A szám páratlan.')

# --- feladatok 01 / 20 (elojel) ---------

# szam = int(input('Adj meg egy egész számot! '))

# if szam < 0:
#     print('A szám negatív.')
# elif szam > 0:
#     print('A szám pozitív.')
# else:
#     print('A szám 0.')

# --- feladatok 01 / 23 ---------

# pontszam = int(input('Írd be a pontszámodat! '))

# if 100 > pontszam > 88:
#     print('jeles')
# elif pontszam > 73:
#     print('jó')
# elif pontszam > 58:
#     print('közepes')
# elif pontszam > 43:
#     print('elégséges')
# elif pontszam > 0:
#     print('elégtelen')
# else:
#     print('Ilyen pontszámod biztosan nem volt!')

# --- feladatok 01 / 28 (honapok) ---------

# honap = int(input('Add meg a hónap sorszámát! '))

# if honap == 1:
#     print('Január')
# elif honap == 2:
#     print('Február')
# elif honap == 3:
#     print('Március')
# elif honap == 4:
#     print('Április')
# elif honap == 5:
#     print('Május')
# elif honap == 6:
#     print('Június')
# elif honap == 7:
#     print('Július')
# elif honap == 8:
#     print('Augusztus')
# elif honap == 9:
#     print('Szeptember')
# elif honap == 10:
#     print('Október')
# elif honap == 11:
#     print('November')
# elif honap == 12:
#     print('December')
# else:
#     print('Hibás adat!')

# --- feladatok 01 / 30 (szokoev) ---------

# ev = int(input('Adj meg egy évet! '))

# if ev % 400 == 0 or ev % 4 == 0 and ev % 100 != 0:
#     print('szökőév')
# else:
#     print('nem szökőév')