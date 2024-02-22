import random

print("Teumakan Kelinci Berikut '🐇' ")

position = random.randint(0, 4)

print ("MASUKAN OPSI PILIHAN \n 🕳️  🕳️  🕳️  🕳️"  )

inputan = int(input("Temukan Kelincinya Ada Di Goa Mana?: 1/2/3/4 = "))

 
while True:
    if inputan == position:
        print(f"🐇 Anda Benar Tempat Berada Di {inputan}" )
        break 
    else:
        print("Inputan Anda Salah")
        inputan = int(input("Temukan Kelincinya Ada Di Goa Mana?: 1/2/3/4 = " ))  
        