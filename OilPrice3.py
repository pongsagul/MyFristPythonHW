#import
from zeep import Client
from lxml import etree
import os

#กำหนดค่าต่างๆ
client = Client('http://www.pttor.com/OilPrice.asmx?WSDL')

result = client.service.CurrentOilPrice("en")

root = etree.fromstring(result)

GasProduct = []
GasPrice = []

space, high = os.get_terminal_size()
space -= 2



#ฟังชันกรอบ+ตัวหนังสือ
def page(strings, symbol="#"):
  s = len(strings) / 2
  if (int(s) != s):
    s1, s2 = s - 1, s
  else:
    s1, s2 = s, s
  print(symbol + (" " * int(space / 2 - s1)) + strings +
        (" " * int(space / 2 - s2)) + symbol)

#ฟังชันขอบกรอบ
def line(symbol):
  L = "#"*(int(space)+2)
  print(L)

#ฟังชันกรอบ
def frame(symbol):
  F = ("#"+" "*(space)+"#")
  print(F)
  #ใช้ for i in range(x): - เพื่อทำหลายแถว 

#ฟังชันลิตรเป็นเงินLitToMoney(LTM) K=ชนิดน้ำมัน , L=lit
def LTM(K,L):
	page(str(GasProduct[K])+" : "+" %2.f" %((GasPrice[K])*L)+" BATH")
	
#ฟังชันเงินเป็นลิตรMonetyToLits(MTL) K=ชนิดน้ำมัน , M=mone
def MTL(K,M):
	page(str(GasProduct[K])+" : "+" %2.f" %(M/(GasPrice[K])*M)+" LITS")

#กรอบแสดงน้ำมัน
line("#")
frame("#")
page("*Oil Price - TODAY!!!")
for i in range(2):
  frame("#")

number = 1

for r in root.xpath('FUEL'):
  product = r.xpath('PRODUCT/text()')[0]
  price = r.xpath('PRICE/text()') or [0]

  GasProduct.append(product)
  GasPrice.append(float(price[0]))

  page(str(number) + ". " + product + " %2.f" %
  (float(price[0])) + ' BAHT')

  number += 1

frame("#")
page("-Choose Kinds of oil (Number)-")
frame("#")
line("#")

#รับค่าชนิดน้ำมัน
kind = int(input("Oil's kind : >"))
K = (kind-1)

#หน้าเมนูเลือกคำสั่ง
line("#")
for i in range(5):
  frame("#")
page("*Choose Command")
frame("#")
frame("#")
page("(1) Lits To Money")
frame("#")
frame("#")
page("(2) Money To Lits")
frame("#")
frame("#")
page("-Choose Kinds of oil (Number)-")
for i in range(6):
  frame("#")
line("#")

#รับคำสั่ง

Com = str(input("Command : >"))

#ประมวลคำสั่ง

if "1" in Com:

  line("#")
  for i in range(9):
    frame("#")
  page("Lits Input")
  frame("#")
  for i in range(10):
    frame("#")
  line("#")
  
  L = float(input("Lits : "))
  
  line("#")
  for i in range(9):
    frame("#")
  page("Result - Lits To Bath")
  frame("#")
  LTM(K,L)
  for i in range(9):
    frame("#")
  line("#")

elif "2" in Com:

  line("#")
  for i in range(9):
    frame("#")
  page("Money Input")
  frame("#")
  for i in range(10):
    frame("#")
  line("#")
  
  M = float(input("Lits : "))
  
  line("#")
  for i in range(9):
    frame("#")
  page("Result - Bath To Lits")
  frame("#")
  MTL(K,M)
  for i in range(9):
    frame("#")
  line("#")


  
