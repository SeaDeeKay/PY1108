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

print('Bankjegyautomata')
print(' ')
print('A legkisebb címlet 1000 Ft, a maximálisan felvehető összeg 300 000 Ft.')
print(' ')

osszeg = int(input('Adja meg mekkora összeget kíván felvenni! '))

print(' ')
print('A kiadott bankjegyek:')
print(' ')

if (osszeg % 10000) == 0:
    print(f'{osszeg / 10000} * 10 000 = {osszeg}')
elif (osszeg % 10000) != 0 and ((osszeg % 10000) % 5000) == 0:
    print(f'{osszeg // 10000} * 10 000 = {(osszeg // 10000) * 10000}')
    print(f'{(osszeg % 10000) / 5000} * 5000 = {(osszeg % 10000)}')
elif (osszeg % 10000) != 0 and (osszeg % 5000) != 0 and (osszeg % 1000) == 0:
    print(f' {osszeg // 10000} * 10 000 = {(osszeg // 10000) * 10000}')
    print(f' {(osszeg % 10000) // 5000} * 5 000 = {((osszeg % 10000) // 5000) * 5000}')
    print(f' {round((osszeg % 5000) / 1000)} * 1 000 = {osszeg % 5000}')
elif (osszeg % 10000) != 0 and (osszeg % 5000) != 0 and (osszeg % 1000) != 0:
    print('A legkisebb felvehető összeg 1000 Ft!')

print(' ')
if (osszeg % 10000) == 0 or (osszeg % 5000) == 0 or (osszeg % 1000) == 0:
    print(f'Összeg: {osszeg} Ft')
elif (osszeg % 10000) != 0 and (osszeg % 5000) != 0 and (osszeg % 1000) != 0:
    print ('Összeg: 0 Ft')