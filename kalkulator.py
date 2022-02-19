a = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
b = int(input("Podaj składnik 1"))
c = int(input("Podaj składnik 2"))
operacja = input("+,-,*,/")
print(operacja)
if (operacja == "+"):
    print("Wynik to", b+c)
if (operacja == "-"):
    print("Wynik to", b-c)
if (operacja == "*"):
    print("Wynik to", b*c)
if (operacja == "/"):
    print("Wynik to", b/c)

