def vypocetNaKg(user_weight):
    result = user_weight / 1000
    print(result, "kg")


def vypocetNaG(user_weight):
    result = user_weight * 1000
    print(result, "g")


user_weight = input("Koľko vážiš? ")

if user_weight.replace('.', '', 1).isdigit():
    user_weight = float(user_weight)
    user_unit = input("Kilograms (kg) or Grams (g): ").lower()

    if user_unit == "kg":
        vypocetNaG(user_weight)
    elif user_unit == "g":
        vypocetNaKg(user_weight)
    else:
        print("Error: Nezadali ste jednotku na prepočet.")
else:
    print("Zadali ste nesprávne hodnoty.")