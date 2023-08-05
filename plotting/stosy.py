x = {"nr_przeyslki": ["123asdas", "123addqwe", "123sdsfaf", "234sdada", "234wdsad", "2113dasd"]}

print(x["nr_przeyslki"][8:10])

lista = ["123asdas", "123addqwe", "123sasfaf", "234sbada", "234wzsad", "2113dasd"]


def middle_char(s):
    return s[4]


lista.sort(key=middle_char)

print(lista)