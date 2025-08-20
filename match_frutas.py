import os
os.system("clear")
frutas=(input("seleccione una fruta: ")).lower()
match frutas:
    case "manzana":
     print("\nusted escogio manzana y tiene un precio de 2000")
    case "pera" :
      print("\nUsted escogio pera y tiene un precio de 3500")
    case "mango" :
      print("\nUsted escogio mango y tiene un valor de 4000")
    case _:
      print("\nopcion de fruta invalida")