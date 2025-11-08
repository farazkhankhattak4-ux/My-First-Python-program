score = input("Enter Score: ")
s = float(score)
if 0.9<= s <1.0:
    print("A")
elif 0.8<= s <0.9:
    print("B")
elif 0.7<= s <0.8:
    print("C")
elif 0.6<= s <0.7:
    print("D")
elif s <0.6:
    print("F")
else :
    print("Incorrect data")