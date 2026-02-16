<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Calculadora de Funciones</title>
    <link rel="stylesheet" href="https://pyscript.net/releases/2024.1.1/core.css" />
    <script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>
</head>
<body style="background-color: #f0f2f5; font-family: sans-serif; padding: 20px;">

    <h2>Calculadora de Funciones</h2>
    <p>El código se ejecutará aquí abajo (espera a que cargue):</p>
    
    <hr>

    <script type="py">
import math

# --- TU CÓDIGO EMPIEZA AQUÍ ---
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
# --- TU CÓDIGO TERMINA AQUÍ ---
    </script>

</body>
</html>
