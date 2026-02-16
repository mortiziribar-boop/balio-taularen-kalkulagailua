
funtzioa=input("zartu zure funtzioa,adb:(3*x-5):")
pkopurua=int(input("idatzi zenbat puntu nahi dituzun:"))
puntuak=[]
for y in range(pkopurua):
    balioak=float(input("Eman x-eri balio bat:"))
    puntuak.append(balioak)
    
print("\nZuk ataratako puntuak:")
for x in puntuak:
    try:
        y=eval(funtzioa)
        print(f"puntua:({x},{y})")
    except:
        print("x",x,"denean, errore matematiko bat dago.")
