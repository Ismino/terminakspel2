import random

def gissa_numret():
    print("välkommen Till 'Gissa numret!")
    print("jag tänker på ett tal mellan 1 och 100.")
    print("kan du lista ut vilket det är? Du har 10 försök på dig")

    hemligt_tal = random.randint(1, 100)
    försök_kvar = 10

    while försök_kvar > 0:
        try:
            gissning = int(input(f"du har {försök_kvar} försök kvar. Din gissnig: "))
            if gissning < 1 or gissning > 100:
                print("Talet måste vara mellan 1 och 100. Försök igen")
                continue
        except ValueError:
            print("Du måste skriva ett giltigt tal! Försök igen.")
            continue
        if gissning == hemligt_tal:
            print(f"Grattis du gissade rätt. Talet var {hemligt_tal}")
            break
        elif gissning < hemligt_tal:
            print("För lågt")
        else:
            print("För högt!")

        försök_kvar -= 1

    if försök_kvar == 0:
        print(f"Tyvärr, du är slut på försök. Talet var {hemligt_tal}. Bättre lycka nästa gång")

if __name__ == "__main__":
    gissa_numret()            