gria = {
    "IC": 6,
    "ProI": 6,
    "Álgebra": 6,
    "Cálculo": 6,
    "MD": 6,
    "XO": 6,
    "APS": 6,
    "Lógica": 6,
    "PRO II": 6,
    "Estadística": 6
}

for i, asignatura in gria.items():
    print(i, "-", asignatura, "ECTS.")
fin = False
suma = 0
creditos = 0

while fin == False:
    asig = input("Introduzca las asignaturass en las que se quiere matricular(fin para terminar): ")
    if asig == 'fin':
        fin = True
    else:
        suma += 1
        creditos += 6

print(f"Ha escogido {suma} asignaturas y la matrícula contiene {creditos} creditos.")