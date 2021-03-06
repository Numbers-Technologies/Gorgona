def rus2eng(text: str) -> str:
    """
    Russian alphabet to english alphabet
    :gets text: = 'п': str
    :returns text = 'p': str
    """
    slovar = {"а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e",
              "ё": "yo", "ж": "j", "з": "z", "и": "i", "й": "yi", "к": "k",
              "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
              "с": "s", "т": "t", "у": "y", "ф": "f", "х": "x", "ц": "c",
              "ч": "ce", "ш": "sh", "щ": "shi", "ъ": "none", "ы": "none",
              "ь": "none", "э": "e", "ю": "u", "я": "ya"}
    return slovar[text]


def text2num(number: str) -> int:
    """
    Text to num
    :gets number = "два": str
    :returns slovar[number]: int
    """
    slovar = {"один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5,
              "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "десять": 10,
              "одинадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14,
              "пятнадцать": 15, "шестнадцать": 16, "семьнадцать": 17, "восемьнадцать": 18,
              "девятнадцать": 19, "двадцать": 20, "двадцать один": 21, "двадцать два": 22,
              "двадцать три": 23, "двадцать четыре": 24, "двадцать пять": 25,
              "двадцать шесть": 26, "двадцать семь": 27, "двадцать восемь": 28,
              "двадцать девять": 29, "тридцать": 30, "тридцать один": 31, "тридцать два": 32, "тридцать три": 33,
              "тридцать четыре": 34, "тридцать пять": 35, "тридцать шесть": 36, "тридцать семь": 37,
              "тридцать восемь": 38, "тридцать девять": 39,
              "сорок": 40, "сорок один": 41, "сорок два": 42, "сорок три": 43, "сорок четыре": 44,
              "сорок пять": 45, "сорок шесть": 46, "сорок семь": 47, "сорок восемь": 48, "сорок девять": 49,
              "пятьдесят": 50, "пятьдесят один": 51,
              "пятьдесят два": 52, "пятьдесят три": 53, "пятьдесят четыре": 54, "пятьдесят пять": 55,
              "пятьдесят шесть": 56,
              "пятьдесят семь": 57, "пятьдесят восемь": 58, "пятьдесят девять": 59}

    return slovar[number]
