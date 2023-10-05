salario = float(input("¿Cuanto cobras? "))
hipoteca = float(input("¿Cuanta hipoteca te queda por pagar? "))
interes = float(input("A cuantos interses "))
plazos = float(input("En cuantas cuotas "))

resultado = ((hipoteca*(interes/100))+hipoteca)/plazos
print("Al mes tienes que pagar:", resultado)
if salario>=resultado:
    print("Lo cual para lo qu ganas es asequible, dentro de lo que cabe")
else:
    print("Pero deberias replantearte esta opcion ya qy lo que gannas no s sufucuente para cubrirlo")
