def menu1():
    print('********************************************************************************')
    print('********************************************************************************')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                           WELCOME TO DreamOilStar                          **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('********************************************************************************')
    print('********************************************************************************')


def menu2():

    print('********************************************************************************')
    print('********************************************************************************')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                     Serect                                 **')
    print('**                                                                            **')
    print('**                             Oil type and price                             **')
    print('**                                                                            **')
    print('**                   *==   1.GASOLINE 95 price  29.15  BATH ==*               **')
    print('**                   *==   2.GASOLINE 91 price  25.30  BATH ==*               **')
    print('**                   *==   3.GASOHOL 91  price  21.68  BATH ==*               **')
    print('**                   *==   4.Gasohol E20 price  20.2   BATH ==*               **')
    print('**                   *==   5.GASOHOL 95  price  21.2   BATH ==*               **')
    print('**                   *==   6.DIESEL      price  21.1   BATH ==*               **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('********************************************************************************')
    print('********************************************************************************')


def menu3():
    print('********************************************************************************')
    print('********************************************************************************')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                   Serect                                   **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                             1.Money To Liter                               **')
    print('**                             2.Liter To Money                               **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('**                                                                            **')
    print('********************************************************************************')
    print('********************************************************************************')


menu1()
y = 1
while True:
    if y == 1:
        menu2()
        tp = 0
        status = True
        i = 0
        while not(tp in ['1', '2', '3', '4', '5', '6']):
            if tp in ['1', '2', '3', '4', '5', '6'] and status:
                status = True
            else:
                status = False
                if i > 0:
                    menu2()
                    print('You entered the wrong information Please enter again')
            i += 1
            tp = (input('Serect Oil Number 1-6 : '))
            b = tp

        menu3()
        tp1 = 0
        status = True
        i = 0
        while not(tp1 in ['1', '2']):
            if tp1 in ['1', '2'] and status:
                status = True
            else:
                status = False
                if i > 0:
                    menu3()
                    print('You entered the wrong information Please enter again')
            i += 1
            tp1 = (input('Serect Means Number 1-2 : '))
            c = tp1
        if '1' in c:
            g1 = input('Enter money :  ')
            m1 = int(g1)
        elif '2' in c:
            g2 = input('Enter Liter : ')
            m2 = float(g2)
        else:
            print('Serect not found')
        k = 0
        if '1' in c:
            if '1' in b:
                k = k + (m1 / 29.15)
                print('Ans', '%.2f' % k, 'Liter')
            elif '2' in b:
                k = k + (m1 / 25.30)
                print('Ans', '%.2f' % k, 'Liter')
            elif '3' in b:
                k = k + (m1 / 21.68)
                print('Ans', '%.2f' % k, 'Liter')
            elif '4' in b:
                k = k + (m1 / 20.2)
                print('Ans', '%.2f' % k, 'Liter')
            elif '5' in b:
                k = k + (m1 / 21.2)
                print('Ans', '%.2f' % k, 'Liter')
            elif '6' in b:
                k = k + (m1 / 21.1)
                print('Ans', '%.2f' % k, 'Liter')
            else:
                print('Invalid information, please Enter again.')
        elif '2' in c:
            if '1' in c:
                k = k + (m2 * 29.15)
                print('Price Oil =', k, 'BATH')
            elif '2' in c:
                k = k + (m2 * 25.30)
                print('Price Oil =', k, 'BATH')
            elif '3' in c:
                k = k + (m2 * 21.68)
                print('Price Oil =', k, 'BATH')
            elif '4' in c:
                k = k + (m2 * 20.2)
                print('Price Oil =', k, 'BATH')
            elif '5' in c:
                k = k + (m2 * 21.2)
                print('Price Oil =', k, 'BATH')
            elif '6' in c:
                k = k + (m2 * 21.1)
                print('Price Oil =', k, 'BATH')
            else:
                print('Invalid information, please Enter again.')

        x = int(input("*=1.Enter 1 Continue calculation *=2.Enter 0 to Exit :"))
        y = x
    elif y == 0:
        print('********************************************************************************')
        print('********************************************************************************')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                           THANK YOU FOR BUY OIL                            **')
        print('**                                                                            **')
        print('**                               DreamOilStar                                 **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('**                                                                            **')
        print('********************************************************************************')
        print('********************************************************************************')

        break
