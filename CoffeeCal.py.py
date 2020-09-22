W = 400
M = 540
B = 120
C = 9
m = 550

y = 1
while True:
    if y == 1:
        print("*" * 80)
        print("*" * 80)
        print("**", ' ' * 25, "The Coffee machine has:", ' ' * 24, "**")
        print('**', ' ' * 74, '**')
        print("**", ' ' * 29, (W), "ml of water", ' ' * 28, "**")
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print("**", ' ' * 29, (M), "ml of milk", ' ' * 29, "**")
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print("**", ' ' * 29, (B), "g of coffee beans", ' ' * 22, "**")
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print("**", ' ' * 29, (C), "of disposable cups", ' ' * 23, "**")
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print("**", ' ' * 29, (m), "$ of money", ' ' * 29, "**")
        print('**', ' ' * 74, '**')
        print('**', ' ' * 74, '**')
        print("*" * 80)
        print("*" * 80)

        p = input("choose one option - buy / fill/ take >")

        if "buy" in p or "Buy" in p or "BUY" in p:
            print("*" * 80)
            print("*" * 80)
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print("**", ' ' * 25, "Choose Kind Of Coffee", ' ' * 26, "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print("**", ' ' * 25, "( 1 ) Espresso", ' ' * 33, "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print("**", ' ' * 25, "( 2 ) Latte", ' ' * 36, "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print("**", ' ' * 25, "( 3 ) Cappuccino", ' ' * 31, "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print("*" * 80)
            print("*" * 80)
            c = str(input("tell me what number do you want ? >"))
            if 'espresso' in c or '1' in c:
                print("*" * 80)
                print("*" * 80)
                print("**", ' ' * 30, "Espresso", ' ' * 34, "**")
                print("**", ' ' * 27, "you must pay 4 $", ' ' * 29, "**")
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    "*The Coffee machine has:",
                    ' ' * 23,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    (int(W) - 250),
                    "ml of water",
                    ' ' * 32,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print("**", ' ' * 25, (M), "ml of milk", ' ' * 33, "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    (int(B) - 16),
                    "g of coffee beans",
                    ' ' * 26,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    (int(C) - 1),
                    "of disposable cups",
                    ' ' * 27,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    (int(m) + 4),
                    "$ of money",
                    ' ' * 33,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print("*" * 80)
                print("*" * 80)
            elif 'latte' in c or '2' in c:
                print("*" * 80)
                print("*" * 80)
                print('**', ' ' * 74, '**')
                print("**", ' ' * 30, "Latte", ' ' * 37, "**")
                print("**", ' ' * 27, "you must pay 7 $", ' ' * 29, "**")
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    "The Coffee machine has:",
                    ' ' * 24,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    (int(W) - 350),
                    "ml of water",
                    ' ' * 33,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    (int(M) - 75),
                    "ml of milk",
                    ' ' * 33,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    (int(B) - 20),
                    "g of coffee beans",
                    ' ' * 26,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    (int(C) - 1),
                    "of disposable cups",
                    ' ' * 27,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    (int(m) + 7),
                    "$ of money",
                    ' ' * 33,
                    "**")
                print('**', ' ' * 74, '**')
                print("*" * 80)
                print("*" * 80)
            elif 'cappuccino' in c or '3' in c:
                print("*" * 80)
                print("*" * 80)
                print('**', ' ' * 74, '**')
                print("**", ' ' * 30, "Cappuccino", ' ' * 32, "**")
                print("**", ' ' * 27, "*you must pay 6 $", ' ' * 28, "**")
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    "The Coffee machine has:",
                    ' ' * 24,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    (int(W) - 200),
                    "ml of water",
                    ' ' * 32,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    (int(M) - 100),
                    "ml of milk",
                    ' ' * 33,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    (int(B) - 12),
                    "g of coffee beans",
                    ' ' * 26,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    (int(C) - 1),
                    "of disposable cups",
                    ' ' * 27,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print(
                    "**",
                    ' ' * 25,
                    (int(m) + 6),
                    "$ of money",
                    ' ' * 33,
                    "**")
                print('**', ' ' * 74, '**')
                print('**', ' ' * 74, '**')
                print("*" * 80)
                print("*" * 80)
            else:
                print("Error")

        elif "fill" in p or "Fill" in p or "FILL" in p:
            wf = int(input("write how many ml of water do you want to add:\n>"))
            Mf = int(input("write how many ml of milk do you want to add:\n>"))
            Bf = int(
                input("write how many grams of coffee beans do you want to add:\n>"))
            mf = int(
                input("write how many disposable cups do you want to add:\n>"))

            print("*" * 80)
            print("*" * 80)
            print("**", ' ' * 30, "**Result", ' ' * 34, "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print("**", ' ' * 25, "*The Coffee machine has:", ' ' * 23, "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print(
                "**",
                ' ' * 25,
                (int(W) + (wf)),
                "ml of water",
                ' ' * 32,
                "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print(
                "**",
                ' ' * 25,
                (int(M) + (Mf)),
                "ml of milk",
                ' ' * 33,
                "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print(
                "**",
                ' ' * 25,
                (int(B) + (Bf)),
                "g of coffee beans",
                ' ' * 26,
                "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print(
                "**",
                ' ' * 25,
                (int(C) + (mf)),
                "of disposable cups",
                ' ' * 26,
                "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print("**", ' ' * 25, (int(m)), "$ of money", ' ' * 33, "**")
            print('**', ' ' * 74, '**')
            print("*" * 80)
            print("*" * 80)
        elif "take" in p or "Take" in p or "TAKE" in p:
            print("*" * 80)
            print("*" * 80)
            print('**', ' ' * 74, '**')
            print(
                "**",
                ' ' * 25,
                "< I gave you ",
                (m),
                " $ > ",
                ' ' * 24,
                "**")
            print('**', ' ' * 74, '**')
            print("**", ' ' * 33, "Result", ' ' * 33, "**")
            print("**", ' ' * 25, " *The Coffee machine has:", ' ' * 22, "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print("**", ' ' * 25, (int(W)), "ml of water", ' ' * 32, "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print("**", ' ' * 25, (int(M)), "ml of milk", ' ' * 33, "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print(
                "**",
                ' ' * 25,
                (int(B)),
                "g of coffee beans",
                ' ' * 26,
                "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print(
                "**",
                ' ' * 25,
                (int(C)),
                "of disposable cups",
                ' ' * 27,
                "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print("**", ' ' * 25, (int(m) - m), "$ of money", ' ' * 35, "**")
            print('**', ' ' * 74, '**')
            print('**', ' ' * 74, '**')
            print("*" * 80)
            print("*" * 80)
        else:
            print("Error")

        x = input("Exit/Restart : >")
        if "Exit" in x or "exit" in x or "x" in x or "X" in x:
            y = 0
        elif "Restart" in x or "restart" in x or "R" in x or "r" in x:
            y = 1
        else:
            print("Error")
    elif y == 0:
        break
