




weight = float(input("enter weight "))
unit = input("(K)g (L)bs ")


if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in pounds is  " + str(converted))
else:
    converted = weight * 0.45
    print("weight in Kgs " + str(converted))
