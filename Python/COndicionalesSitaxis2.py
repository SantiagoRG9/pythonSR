salarioPresidente = int(input("Digite el salario del presidente: "))
print("El salario del presidente es: " + str(salarioPresidente))

salarioDirector = int(input("Digite el salario del director: "))
print("El salario del Director es: " + str(salarioDirector))

salarioJefeArea = int(input("Digite el salario del jefe de area: "))
print("El salario del jefe de area es: " + str(salarioJefeArea))

salarioAdministrativo = int(input("Digite el salario del administrativo: "))
print("El salario del administrativo es: " + str(salarioAdministrativo))

if salarioPresidente > salarioDirector > salarioJefeArea > salarioAdministrativo:
    print("Esta todo en orden")
else:
    print("Algo anda mal")

