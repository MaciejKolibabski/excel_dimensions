napis = "ATHLONE BEIGE PULIDO 59X119 G1 AL"
hash_table = {}
ilosc=0
for i in napis:
    i = i.lower()
    if i in "x":
        ilosc += 1
    else:
        ilosc = 1
print('ssss', ilosc)

# iloścx = hash_table['x']
# print("Ilość x =", iloścx)
# print('Location: ', napis.index("X"))
# print(napis[iloścx])