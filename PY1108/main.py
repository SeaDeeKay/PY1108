# változók:
#'duc type'

# nev = 'Dávid'
# print(nev)

# típusok:

# egész (integer) int
# lebegőpontos számok (floating point number) float

# 4 alap művelet: + ; - ; / ; *
# további matematikai műveletek: ** (hatvány) ; // (egész osztás) ; ** n (gyökvonás) ; % (ha elosztom a számot a másikkal, mennyi lesz a maradék)

# logika (bool) bool

# and ; or ; not
# and -> akkor igaz, ha mindkét állítás igaz
# or -> akkor igaz, ha legalább az egyik állítás igaz
# not -> "not True" == "False" ; "not False" == "True" (az ellenkezője)

# karakterláncok (sting) str
# str + str -> konkatenáció
# str * int -> többszörös konkatenáció
# print("kutya" + "ház")
# print("kutya" * 3)

# compare aka. 'összehasonlító operátorok':
# < ; > ; <= ; >= ; == ; !=
x:int = 10
5 + 5 == 10

# --------------

# input -> "bevitel", vagy "bekérés" (amit én írok a programnak) -> input()
# output -> "kimenet" -> print()

# print("Hogy hívnak?")
# nev = input()
# print(f"Szia {nev}")
# evszam:int = 2024
# kor = int(input('Hány éves vagy? '))

# print(f"Akkor te {evszam - kor}-ban születtél ") 
# if kor < 40:
#     print( "és még pofátlanul fiatal vagy!")

# print(10 < 2 or 44 / 2 > 21)

# minden algoritmus leírható
# - szekvencia (egymás után történnek a dolgok, nem egyszerre)
# - szelekció 'elágazás'
# - interáció 'ciklus' (ezekről később)

# if <condition>:
#   [indent] <- kódrészlet, ami akkor fut le, ha a <condition> True
# else:
#   [indent] <- kódrészlet, ami akkor fut le, ha a <condition> False
# 
# az 'else' rész opcionális, vagyis nem kötelező
#   "feltétel" <- ha ezt kiértékelem, akkor a vége bool (vagy igaz, vagy hamis)

# valasz:str = input('elmegyek este berúgni? ')

# if (valasz == 'igen'):
#     print('akkor készülj!')
#     print('sor, ha igaz')
# else:
#     print('akkor folytasd az órát!')
#     print('sor, ha hamis')

# print('sor, ha vége az elágazásnak')

