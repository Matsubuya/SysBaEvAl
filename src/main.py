import os
from time import sleep

def limpiarTerm():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # UNIX
        os.system("clear")


def menuInicio():
    limpiarTerm()
    respuesta = 0
    while respuesta == 0:
        print("+============= MENU PRINCIPAL ==========+")
        print("||                                      ||")
        print("|| 1.- Registrar Alumno                 ||")
        print("|| 2.- Consultar Alumno                 ||")
        print("|| 3.- Consultar Reportes de Evaluación ||")
        print("|| 0.- Salir                            ||")
        print("||                                      ||")
        print("+=======================================+")

        try:
            respuesta = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Intenta de nuevo")

        match respuesta:
            case 1:
                print("Registrar Alumno")
            case 2:
                print("Consultar Alumno")
            case 3:
                print("Consultar Reportes de Evaluación")
            case 0:
                print("Salir")
                limpiarTerm()
                break
            case _:
                print("Opcion no valida")

        if respuesta != 0:
            sleep(1)
            limpiarTerm()

def logon(usr: str, psswd: str):
    # verificar que:
    #   no sea nulo
    #   contrasenia no menor o mayor de 8 a 64 caracteres
    #   usuario no menor o mayor de 5 a 20 caracteres
    #   la contrasenia son caracteres y numeros
    #   El usuario solo puede ser numero
    # falta comparar una contrasenia real

    respuesta = False

    if usr != "" and psswd != "":
        if (len(usr) >= 5 and len(usr) <= 20) and ( len(psswd) >= 8 and len(psswd) <= 64):
            if usr.isdigit():
                si_letras = any(c.isalpha()  for c in psswd)
                si_numeros = any(c.isalpha() for c in psswd)

                if si_letras and si_numeros:
                    respuesta = True
        else:
            respuesta = False
    else:
        respuesta = False

    return respuesta


def main():
    intentos = 3
    while intentos > 0:
        limpiarTerm()
        usuario = input("Usuario (De 5 a 20 Caracteres): ").strip()
        contrasenia = input("Contrasenia (De 8 a 64 Caracteres): ").strip()
        if logon(usuario, contrasenia) == True:
            print("Inicio de sesión exitoso")
            sleep(1)
            menuInicio()
            break
        else:
            print("Usuario o contraseña incorrectos")
            sleep(2)

if __name__ == "__main__":
    main()
    print("Saliendo del programa")
