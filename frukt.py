import random

frukter =("Apelsin", "Banan", "Melon", "Kiwi", "citron")
looping = True


def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + frukter[fnr-1] + " kommer här!\n")

print("\n-:FruktMaskin:-\n")

while looping:
    
    i = 1
    for frukt in frukter:
        print(str(i) + ": " + frukt)
        i += 1

        fruktnr = input("\nMata in nr på frukt du vill ha: ")
        print_fruit(fruktnr)
        go = input("\nVill du ha en frukt")

        if (go == "n"):
            break


print("--------------------------------------------------------")

print("\nFöresten, du får en frukt till för du är snäll!\n")
slumpfrukt = random.randint(1, 5)
print_fruit(slumpfrukt)