#ord()
#A ord()függvény egy megadott karakter unicode kódját képviselő számot adja vissza.
x = ord("A")
y = ord("a")
print(f"A nagy a betű kódja:{x}") # 65
print(f"A kis a betű kódja:{y}") # 97
#chr()
#A chr()függvény a megadott unicode-ot képviselő karaktert adja vissza.
x = chr(97)
print(x)




#min()
#A min()függvény a legalacsonyabb értékű elemet, vagy a legalacsonyabb értékű elemet adja vissza az iterációban.
#Ha az értékek karakterláncok, akkor ábécé szerinti összehasonlítás történik.
x = min(5, 10)
print(x)



#max()
#A max()függvény a legmagasabb értékű elemet, vagy a legmagasabb értékű elemet adja vissza az iterálható elemben.
#Ha az értékek karakterláncok, akkor ábécé szerinti összehasonlítás történik.
x = max(5, 10)
print(x)




#index()
#A index()metódus a megadott érték első előfordulásakor adja vissza a pozíciót.
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)




#list()
#A listák több elem tárolására szolgálnak egyetlen változóban.
#A listák a Pythonban az adatgyűjtemények tárolására használt 4 beépített adattípus egyike, a másik 3 a Tuple , a Set és a Dictionary , amelyek mindegyike eltérő minőségű és felhasználású.
#A listák szögletes zárójelekkel jönnek létre:
thislist = ["apple", "banana", "cherry"]
print(thislist)
