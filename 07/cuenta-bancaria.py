"""
Primero vas a crear una clase llamada Persona, y Persona va a tener solo dos atributos: 
nombre y apellido. 

Luego, vas a crear una segunda clase llamada Cliente, y Cliente va a 
heredar de Persona, pero también va a tener atributos propios:
número de cuenta y balance.

Pero eso no es todo: Cliente también va a tener tres métodos. 

a. El primero va a ser uno de los métodos especiales y es el que permite que podamos imprimir a nuestro cliente. Este método 
va a permitir que cuando el código pida imprimir Cliente, se muestren todos sus datos, 
incluyendo el balance de su cuenta. 
b. Luego, un método llamado Depositar, que le va a permitir decidir cuánto dinero quiere agregar a su cuenta. 
c. Un tercer método llamado Retirar, que le permita decidir cuánto dinero quiere sacar de su cuenta. 

Una vez que hayas creado estas dos clases, tienes que crear el código para que tu programa se 
desarrolle, pidiéndole al usuario que elija si quiere hacer depósitos o retiros. El usuario puede 
hacer tantas operaciones como quiera hasta que decida salir del programa

"""

import os
import random


def clear():
    os.system('clear')


class Persona:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Cliente(Persona):
    def __init__(self, name, surname, account_number, credit):
        super().__init__(name, surname)
        self.account_number = account_number
        self.credit = credit

    def __str__(self):
        return f'Name: {self.surname}, {self.name}. \nCredit: {self.credit} $\naccount: {self.account_number}'

    def deposit(self, cash):
        self.credit += cash

    def withdraw(self, cash):
        if self.credit >= cash:
            self.credit -= cash


def register():
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    name = input("Ingrese su nombre: ")
    surname = input("Ingrese su apellido: ")
    credit = int(input("Ingrese el monto inicial: "))
    account_number = "ES"+"".join(random.choices(numbers, k=16))
    new_client = Cliente(name, surname, account_number, credit)
    return new_client


def atm_start():
    clear()
    print("Binevenido al ATM Python(?)\n")
    new_client = register()
    while True:
        clear()
        print("""
        [1] - Mirar datos / Balance
        [2] - Ingresar dinero
        [3] - Retirar dinero
        [4] - Salir del programa
        """)
        option = input("Elija una opcion: ")
        if not option.isnumeric() or int(option) not in range(1, 5):
            clear()
            print("\tPOR FAVOR\n\tIngrese un NÚMERO del 1 al 4")
            input("Precione ENTER para continuar")
        if option == "4":
            clear()
            break
        if option == "1":
            clear()
            print(new_client)
            input("Precione ENTER para continuar")
        if option == "2":
            clear()
            cash = int(input("Ingrese el monto a depositar: "))
            new_client.deposit(cash)
        if option == "3":
            clear()
            can_withdraw = False
            cash = int(input("Ingrese el monto a retirar: "))
            while not can_withdraw:
                if cash > new_client.credit:
                    clear()
                    print("El monto que intenta retirar es superior a su saldo")
                    print(f'Su saldo: {new_client.credit} $')
                    cash = int(input("Ingrese el monto a retirar: "))
                else:
                    can_withdraw = True
            new_client.withdraw(cash)


atm_start()
