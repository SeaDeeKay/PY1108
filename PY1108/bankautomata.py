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