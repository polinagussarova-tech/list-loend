#töö 5.1
#1
from binascii import a2b_qp


def float_kontroll(sisend:str)->float:
    """Kontrollib, kas sisestatud andmed on teisendatavad float arvuks
    :param str sisend: kasutaja sisestatud andmed
    :return/rtype: teisendatud float arv
    """
    while True:
        try:
            arv=float(sisend)
            return arv
        except ValueError:
            sisend=input("Palun sisesta ainult arv: ")

#2

def int_kontroll(sisend:str)->int:
    """Kontrollib, kas sisestatud andmed on teisendatavad int arvuks
    :param str sisend: kasutaja sisestatud andmed
    :return/rtype: teisendatud float arv
    """
    while True:
        try:
            arv=int(sisend)
            return arv
        except ValueError:
            sisend=input("Palun sisesta arv: ")

#1

def arithmetic(a:float, b:float, tehe:str)->any:
    """Lihtne kalkulaator:
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    Muul juhul tagastab "Tundmatu tehe"
    :param float a: esimene arv
    :param float b: teine arv
    :param str tehe: tehe, mis tuleb teha
    :return/rtype: tehte tulemus float või str
    """
    if tehe in ["+", "-", "*", "/"]:
        if tehe=="/" and b==0:
            vastus= "Nulliga jagamine pole lubatud."
        else:
            vastus=eval(f"{a}{tehe}{b}")
    else:
        vastus="Tundmatu tehe"
    return vastus

#2
def is_year_leap(aasta:int)->bool:
    """Kontrollib, kas aasta on liigaasta
    :param int aasta: aasta arvuna
    :return/rtype: True kui liigaasta, False kui tavaline aasta
    """
    if (aasta % 4 == 0 and aasta % 100 != 0):
        return True
    else:
        return False

#3
def square(külg:float)->any:
    """Arvutab ruudu ümbermõõdu, pindala ja diagonaali
    :param float külg: ruudu külje pikkus
    :return/rtype: ümbermõõt, pindala, diagonaal
    """
    ümbermõõt=4*külg
    pindala=külg**2 #või külg*külg
    diagonaal=külg**0.5*2
    return (ümbermõõt, pindala, diagonaal)


#4

def season(kuu:int)->str:
    """tagastab aastaaja kuu numbri põhjal
    :param int kuu: kuu arvuna (1-12)
    :return/rtype: hooaja aastaja nimetus str
    """
    if kuu in [12, 1, 2]:
        return "talv"
    elif kuu in [3, 4, 5]:
        return "kevad"
    elif kuu in [6, 7, 8]:
        return "suvi"
    elif kuu in [9, 10, 11]:
        return "sügis"
    else:
        return "vigane kuu number"

#5

def bank(a: float, years:int)->float:
    """Arvutab lõppsumma koos intressiga
    :param float a: algsumma
    :param int years: aastate arv
    :return/rtype: lõppsumma float
    """
    intress=0.1 #10% intress
    for i in range(years):
        a+=a*intress
    return a




#6

def is_prime(n: int) -> bool:
    """
    Tagastab True, kui arv n on algarv.
    Kui arv on kordarv, kuvab selle jagajad ja tagastab False.
    """

    if n < 2:
        print("Arv ei ole algarv ega kordarv.")
        return False
    jagajad = []

    for i in range(2, n):
        if n % i == 0:
            jagajad.append(i)

    if len(jagajad) == 0:
        return True

    print(f"{n} on kordarv. Selle jagajad on: {jagajad}")
    return False


#7
def date(day: int, month: int, year: int) -> bool:
    """Tagastab True, kui kuupäev eksisteerib, vastasel juhul False."""

    if year < 1 or month < 1 or month > 12:
        return False

    kuud = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        kuud[1] = 29

    if day < 1 or day > kuud[month - 1]:
        return False

    return True

#8
def XOR_cipher(text: str, key: int) -> str:
    """
    Krüpteerib sõne, rakendades iga märgi ja võtme vahel XOR-tehet.
    Tagastab krüpteeritud sõne.
    """
    encrypted = ""

    for ch in text:
        encrypted += chr(ord(ch) ^ key)

    return encrypted


def XOR_uncipher(encrypted_text: str, key: int) -> str:
    """
    Dekrüpteerib sõne, rakendades krüpteeritud tekstile ja võtmele XOR-tehet.
    Tagastab algse sõne.
    """
    decrypted = ""

    for ch in encrypted_text:
        decrypted += chr(ord(ch) ^ key)

    return decrypted

#9
def average(numbers: list) -> float | None:
    """
    Tagastab järjendis olevate arvude aritmeetilise keskmise.
    Kui järjend on tühi, tagastab None.
    """
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

#10
def min_max(numbers: list) -> tuple | None:
    """
    Tagastab järjendi väikseima ja suurima arvu kujul (väiksem, suurem).
    Kui järjend on tühi, tagastab None.
    """
    if len(numbers) == 0:
        return None

    return (min(numbers), max(numbers))

#11
def unique_elements(lst: list) -> list:
    """
    Tagastab uue järjendi, millest on eemaldatud korduvad elemendid,
    säilitades esialgse järjekorra.
    """
    seen = set()
    result = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result
