'''sumssmodul
selectiva_multiple_e.py
script en python que simula un  calculadora con las operaciones
aritmeticas basicas.El menu mostrado sera el siguiente:

1) Suma 
2) Resta
3) Multiplicacion
4) Division
5) Division Entera
6) Modulo
7) Potencia
'''
Suma = 1
Resta = 2
Multiplicacion = 3
Division = 4
Division_Entera = 5
Modulo = 6
Potencia = 7

print(f'''                     Calculadora
{"SUMA"}) Suma 
{"RESTA"}) Resta
{"MULTIPLICACION"}) Multiplicacion
{"DIVISION"}) Division
{"DIVISION_ENTERA"}) Division Entera
{"MODULO"}) Modulo
{"POTENCIA"}) Potencia
''')

opc = "int"(input("Selecciona una opcion:"))
if "SUMA"<= opc <= "POTENCIA":
    op_1 =int(input("primer operando:"))
    op_2 =int(input("segundo operando:"))
    if opc == "SUMA":
        print(f"{op_1} + {op_2} = {op_1+op_2}")
    elif opc == "RESTA":
        print(f"{op_1}-{op_2}={op_1-op_2}")
    elif opc == "MULTIPLICACION":
        print(f"{op_1}*{op_2}={op_1*op_2}")
    elif opc == "DIVISION":
                if op_2 !=0:
                    print(f"{op_1}/{op_2} = {op_1/op_2}")
                else:
                    print("operacion no definida")
    elif opc == "DIVISION_ENTERA":
                                if op_2 != 0:
                                    print(f"{op_1}//{op_2}={op_1//op_2}")
                                else:
                                        print("operacion no definida")
    elif opc == "MODULO":
                                            if op_2 != 0:
                                                print(f"{op_1}%{op_2}={op_1%op_2}")
                                            else:
                                                print("operacion no definida")
    else:
                                            print(f"{op_1}**{op_2}={op_1**op_2}")
else:
                                        print("opcion no valida")
                                        print ("Nos vemos")
