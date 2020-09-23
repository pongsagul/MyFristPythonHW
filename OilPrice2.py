
from zeep import Client
from lxml import etree
import os
# LOOP Exit or Restart
y = 1
while True:
    if y == 1:
        client = Client('http://www.pttor.com/OilPrice.asmx?WSDL')

        result = client.service.CurrentOilPrice("en")

        root = etree.fromstring(result)

        GasProduct = []
        GasPrice = []

        space, high = os.get_terminal_size()
        space -= 2

        def Window(strings, symbol="*"):
            s = len(strings) / 2
            if (int(s) != s):
                s1, s2 = s - 1, s
            else:
                s1, s2 = s, s
            print(symbol + (" " * int(space / 2 - s1)) + strings +
                  (" " * int(space / 2 - s2)) + symbol)
        print("*" * (space + 2))
        print("*" * (space + 2))
        print("*" + " " * (space) + "*")
        Window("*Oil Price")
        for i in range(0):
            print("*" + " " * (space) + "*")

        number = 1

        for r in root.xpath('FUEL'):
            product = r.xpath('PRODUCT/text()')[0]
            price = r.xpath('PRICE/text()') or [0]

            GasProduct.append(product)
            GasPrice.append(float(price[0]))

            Window(str(number) + ". " + product + " %2.f" %
                   (float(price[0])) + ' BAHT')

            number += 1
# Select Oil Type
        print("*" + " " * (space) + "*")
        Window("Choose Type oils (list's ordinal)")
        print("*" + " " * (space) + "*")
        print("*" * (space + 2))
        print("*" * (space + 2))
        Type = int(input("Oil Type :  "))

        n = (Type - 1)
# Select Calculate Method (1):Lit to BATH or (2):Bath to LITS
        print("*" * (space + 2))
        print("*" * (space + 2))
        print("*" + " " * (space) + "*")
        print("*" + " " * (space) + "*")
        Window("*Choose Calculate Method")
        for i in range(4):
            print("*" + " " * (space) + "*")
        Window("(1):Lit to BATH")
        print("*" + " " * (space) + "*")
        Window("(2):Bath to LITS")
        for i in range(9):
            print("*" + " " * (space) + "*")
        print("*" * (space + 2))
        print("*" * (space + 2))
        c = str(input("Choose Calculate Method :  "))
# Input LITS in Calculate Method : Lit_to_Bath
        if "1" in c or "Lit_to_Bath" in c:
            print("*" * (space + 2))
            print("*" * (space + 2))
            for i in range(8):
                print("*" + " " * (space) + "*")
            Window("**Input LITS**")
            for i in range(10):
                print("*" + " " * (space) + "*")
            print("*" * (space + 2))
            print("*" * (space + 2))
            lits = float(input("LITS input: > "))
# Result - Lit_To_Bath
            print("*" * (space + 2))
            print("*" * (space + 2))
            for i in range(7):
                print("*" + " " * (space) + "*")
            Window("**Result - Lit_To_Bath**")
            print("*" + " " * (space) + "*")
            Window("Money: " +
                   str(GasProduct[n]) +
                   " %2.f" %
                   ((GasPrice[n]) *
                    lits) +
                   " BATH")
            for i in range(9):
                print("*" + " " * (space) + "*")
            print("*" * (space + 2))
            print("*" * (space + 2))
            end = input("Enter (1) or Exit / Enter (2) or Restart :  ")
# Input BATH in Calculate Method : Bath_to_Lit
        elif "2" in c or "Bath_to_Lit" in c:
            print("*" * (space + 2))
            for i in range(10):
                print("*" + " " * (space) + "*")
            Window("Input Money(BATH)")
            for i in range(10):
                print("*" + " " * (space) + "*")
            print("*" * (space + 2))
            money = float(input("Money input(BATH): "))
# Result - Lit_To_Bath
            print("#" * (space + 2))
            for i in range(9):
                print("*" + " " * (space) + "*")
            Window("**Result - Bath_To_Lits**")
            print("*" + " " * (space) + "*")
            Window("Lits: " +
                   str(GasProduct[n]) +
                   " %2.f" %
                   (money /
                    float(GasPrice[n])) +
                   " Lits")
            for i in range(9):
                print("*" + " " * (space) + "*")
            print("*" * (space + 2))
            end = input("Enter (1) or Exit / Enter (2) or Restart :  ")
        else:
            print("Error")

        if "Restart" in end or "2" in end or "restart" in end or "0" in end:
            y = 1
        elif "Exit" in end or "1" in end or "exit" in end:
            y = 0
        else:
            print("Error")
    elif y == 0:
# Exit and Print THANK YOU SO MUCH
        print("*" * (space + 2))
        print("*" * (space + 2))
        for i in range(6):
            print("*" + " " * (space) + "*")
        Window("**THANK YOU SO MUCH**")
        print("*" + " " * (space) + "*")
        Window("**THANK YOU SO MUCH**")
        print("*" + " " * (space) + "*")
        Window("**THANK YOU SO MUCH**")
        for i in range(8):
            print("*" + " " * (space) + "*")
        print("*" * (space + 2))
        print("*" * (space + 2))
        break
