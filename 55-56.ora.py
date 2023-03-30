# Emőd időjárás előrejelzése: 2023. március 22 - 2023. április 20.

# A program globális változói
datum = ["március 22", "március 23", "március 24", "március 25", "március 26",
        "március 27", "március 28", "március 29", "március 30", 
        "április 1", "április 2", "április 3", "április 4", "április 5", "április 6",
        "április 7", "április 8", "április 9", "április 10", "április 11", "április 12",
        "április 13", "április 14", "április 15", "április 16", "április 17", 
        "április 18", "április 19", "április 20",]
napi_maximum = [14,17,21,15,16,13,8,11,12,14,16,16,14,15,13,14,16,16,14,12,12,10,
            11,13,15,17,19,17,19,20] # Celsius-fok
napi_minumum = [8,8,9,6,7,1,0,2,3,5,4,4,3,5,4,6,8,6,4,2,1,-1,-1,1,3,5,7,5,7,9] # Celsius-fok
napi_minumum_darab = None # mért minimum hőmérséklet napok száma -> 30 nap
napi_maximum_darab = None # mért maximum hőmérséklet napok száma -> 30 nap
harmincnapos_napi_atlag = []

# ------------------------------------------------------------------------------------

# 1. Feladat
# Számold meg, hány nap adatait tartalmazza a napi_maximum lista!

print("1. Feladat")
print("Számold meg, hány nap adatait tartalmazza a napi_maximum lista!")

def megszamlalas_max(napi_max):
darab = 0
for szam in napi_max:
    darab +=  1 # darab = darab + 1
    napi_maximum_darab = darab # A globális változónak értéket adtam
return darab

print(f"A napi_maximum lista elemszáma: {megszamlalas_max(napi_maximum)} ")

# 2. Feladat
# Számold meg, hány nap adatait tartalmazza a napi_minumum lista!

print("2. Feladat")
print("Számold meg, hány nap adatait tartalmazza a napi_minumum lista!")

def megszamlalas_min(napi_min):
darab = 0
for szam in napi_min:
    darab +=  1 # darab = darab + 1
    napi_minumum_darab = darab # A globális változónak értéket adtam
return darab

print(f"A napi_minumum lista elemszáma: {megszamlalas_max(napi_minumum)} ")

# ------------------------------------------------------------------------------------

# 3. Feldat
# Számold ki a 30 napos előrejelzés napi maximum értékeinek átlagát!

print("3. Feldat")
print("Számold ki a 30 napos előrejelzés napi maximum értékeinek átlagát!")

def atlag_max(napi_max):
lista_eleminek_osszege = 0
for szam in napi_max:
    lista_eleminek_osszege = lista_eleminek_osszege + szam
atlag = lista_eleminek_osszege / len(napi_max)    
return atlag


print(f"A 30 napos előrejelzés napi maximum értékeinek átlaga: {atlag_max(napi_maximum):.2f} Celsius-fok")

# ------------------------------------------------------------------------------------

def atlag_min(napi_min):
lista_eleminek_osszege = 0
for szam in napi_min:
    lista_eleminek_osszege = lista_eleminek_osszege + szam
atlag = lista_eleminek_osszege / len(napi_min)    
return atlag


print(f"Minimium hőmésékletek átlaga: {atlag_min(napi_minumum):.2f} ")
