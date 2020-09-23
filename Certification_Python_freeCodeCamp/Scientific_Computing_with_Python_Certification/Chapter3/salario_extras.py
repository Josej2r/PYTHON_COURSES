horas = input("Introduzca las horas: ")
tarifa = input("Introduzca la Tarifa por hora: ")

try:
    horas = float(horas)
    tarifa = float(tarifa)
    if horas > 40.0:
        extra = horas - 40
        salario = (40.0*tarifa) + (extra*1.5*tarifa)
    else:
        salario = horas * tarifa

    print(f"Salario: {salario}")

except:
    print("Error, por favor introduzca un número ")
