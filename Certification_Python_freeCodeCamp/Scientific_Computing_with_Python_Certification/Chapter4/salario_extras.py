def calculo_salario(horas, tarifa):
    try:
        horas = float(horas)
        tarifa = float(tarifa)
        if horas > 40.0:
            extra = horas - 40
            salario = (40.0 * tarifa) + (extra * 1.5 * tarifa)
            return salario
        else:
            salario = horas * tarifa
            return salario

    except:
        print("Error, por favor introduzca un número ")


horas_trabajadas = input("Introduzca las horas: ")
tarifa_por_hora = input("Introduzca la Tarifa por hora: ")
salario = calculo_salario(horas_trabajadas, tarifa_por_hora)
print(f"Salario: {salario}")
