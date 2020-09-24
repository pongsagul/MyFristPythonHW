# import
from zeep import Client
from lxml import etree
import os

y = 1
while True:
    if y == 1:
        # กำหนดค่าต่างๆ
        client = Client('http://www.pttor.com/OilPrice.asmx?WSDL')

        result = client.service.CurrentOilPrice("en")

        root = etree.fromstring(result)

        GasProduct = []
        GasPrice = []

        space, high = os.get_terminal_size()
        space -= 2

        # ฟังชันกรอบ+ตัวหนังสือ

        def Window(strings, symbol="*"):
            s = len(strings) / 2
            if (int(s) != s):
                s1, s2 = s - 1, s
            else:
                s1, s2 = s, s
            print(symbol + (" " * int(space / 2 - s1)) + strings +
                  (" " * int(space / 2 - s2)) + symbol)

        # ฟังชันขอบกรอบ

        def line(symbol):
            L = "*"*(int(space)+2)
            print(L)

        # ฟังชันกรอบ

        def frame(symbol):
            F = ("*"+" "*(space)+"*")
            print(F)
            # ใช้ for i in range(x): - เพื่อทำหลายแถว

        # ฟังชันลิตรเป็นเงินLitToMoney(LTM) K=ชนิดน้ำมัน , L=lit

        def LTM(K, L):
            Window(str(GasProduct[K])+" : "+" %2.f" %
                   ((GasPrice[K])*L)+" BATH")

        # ฟังชันเงินเป็นลิตรMonetyToLits(MTL) K=ชนิดน้ำมัน , M=mone

        def MTL(K, M):
            Window(str(GasProduct[K])+" : "+" %2.f" %
                   (M/(GasPrice[K])*M)+" LITS")

        #Fream or Oilprice
        line("*")
        line("*")
        frame("*")
        Window("*Oil Price - TODAY!!!")
        for i in range(0):
            frame("*")

        number = 1

        for r in root.xpath('FUEL'):
            product = r.xpath('PRODUCT/text()')[0]
            price = r.xpath('PRICE/text()') or [0]

            GasProduct.append(product)
            GasPrice.append(float(price[0]))

            Window(str(number) + ". " + product + " %2.f" %
                   (float(price[0])) + ' BAHT')

            number += 1

        frame("*")
        Window("-Choose Type of oil (Number)-")
        frame("*")
        line("*")
        line("*")

        # รับค่าชนิดน้ำมัน
        Type = int(input("Oil's Type : "))
        T = (Type-1)

        # หน้าเมนูเลือกคำสั่ง
        line("*")
        line("*")
        for i in range(3):
            frame("*")
        Window("*Choose Calculate Method")
        frame("*")
        frame("*")
        Window("(1) Lits To Money")
        frame("*")
        frame("*")
        Window("(2) Money To Lits")
        frame("*")
        frame("*")
        Window("-Choose Type of oil (Number)-")
        for i in range(6):
            frame("*")
        line("*")
        line("*")

        # รับคำสั่ง

        Com = str(input("Calculate Method: "))

        # ประมวลคำสั่ง

        if "1" in Com:

            line("*")
            line("*")
            for i in range(9):
                frame("*")
            Window("LITS Input")
            frame("*")
            for i in range(8):
                frame("*")
            line("*")
            line("*")

            L = float(input("Lits : "))

            line("*")
            line("*")
            for i in range(7):
                frame("*")
            Window("Result - LITS To BATH")
            frame("*")
            LTM(T, L)
            for i in range(9):
                frame("*")
            line("*")
            line("*")
            end = input("Enter (1) or Exit / Enter (2) or Restart :  ")

        elif "2" in Com:

            line("*")
            line("*")
            for i in range(7):
                frame("*")
            Window("Money Input")
            frame("*")
            for i in range(10):
                frame("*")
            line("*")
            line("*")

            M = float(input("LITS : "))

            line("*")
            line("*")
            for i in range(7):
                frame("*")
            Window("Result - BATH To LITS")
            frame("*")
            MTL(T, M)
            for i in range(9):
                frame("*")
            line("*")
            line("*")
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
        line("*")
        line("*")
        for i in range(6):
            frame("*")
        Window("**THANK YOU SO MUCH**")
        frame("*")
        Window("**THANK YOU SO MUCH**")
        frame("*")
        Window("**THANK YOU SO MUCH**")
        for i in range(8):
            frame("*")
        line("*")
        line("*")
        break
