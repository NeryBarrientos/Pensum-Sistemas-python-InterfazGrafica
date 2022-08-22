#enconding: utf-8
from cProfile import label
from optparse import Values
from tkinter import *
from tkinter import ttk
import tkinter as tk

import time
#import random
import numpy 
from random import randint

optionSelect = 0
i = 0
devolver = ""
num1Alea = int(randint(0,35))
acumulador = ""
cantidadDePalabras = 0
palabrasMemorizar = ["Bachata","Auto","Tren","Avión","Isla","Perro","Gato","Soldado",
"Rusia","Celular","Copa","Mouse","Tv","Sega","Mesa","Asado","Lechuga",
"Palo","Estufa","Árbol","Piano","Pantalón","Mueble","Cortina","Luna","Misión",
"Resident Evil","Remera","Escopeta","Verde","Sol","Cable","Internet","Celular","Rig",
"Manzana","Lapicera","Pileta","Gorila","Cartucho","Tablet","Remera","Salchicha",
"Marte","Golf","Ventilador","Taladro","Fregona","Mochila","Cordón","Ropero",
"Plutón","Eclipse","Fiat","Banco","Servidor","Reino Unido","Computador","Pelota","Verde"]
""" print("|------------------------------|")
print("|   Bienvenido a Full Memory   |")
print("|------------------------------|") """
#print("Elija una opción por favor para comenzar a entrenar su memoria...")
#optionSelect = int(input("1-Nivel inicial | 2-Nivel medio | 3-Nivel avanzado: ")) 
#cantidadDePalabras = int(input("Cuantas palabras desea memorizar: "))
def arrancarEntrenamiento():
    global valorseleccionado,entrypalabra
    valorseleccionado = combo.get()
    cantidadDePalabras =  camponumpalabras.get()
    time.sleep(1)
    print("Muy bien, ya comenzamos...")
    time.sleep(1)
    if  valorseleccionado == "Nivel inicial":
        for palabra in range(int(cantidadDePalabras)):
            global acumulador
            time.sleep(2)
            print("")
            print("°---------------°")
            devolver = numpy.random.choice(palabrasMemorizar)
            entrypalabra.set(devolver)
            print(devolver , "Hola")
            print("°---------------°")
            acumulador =  acumulador + devolver + " | " 
            time.sleep(2)
    elif valorseleccionado == "Nivel medio":  
         for palabra in range(int(cantidadDePalabras)):
            acumulador
            time.sleep(10)
            print("")
            print("°---------------°")
            devolver = numpy.random.choice(palabrasMemorizar)
            print(devolver)
            print("°---------------°")
            acumulador =  acumulador + devolver + " | " 
    elif valorseleccionado == "Nivel avanzado":
         for palabra in range(int(cantidadDePalabras)):
            acumulador
            time.sleep(5)
            print("")
            print("°---------------°")
            devolver = numpy.random.choice(palabrasMemorizar)
            print(devolver)
            print("°---------------°")
            acumulador =  acumulador + devolver + " | "   
    else:
        print("Error, debe elegír una opción válida") 
""" arrancarEntrenamiento(valorseleccionado)
time.sleep(2)
print("Perfecto, vamos a comprobar lo memorizado...")
time.sleep(2)
def comprobar(acumulador):
     print(" --> ",acumulador)
comprobar(acumulador) """
raiz = Tk()
raiz.title("Memory full")
raiz.geometry("1000x700")
#raiz.iconbitmap("fullmemori.ico")
raiz.config(bg="black")
miLabel = Label(raiz,text="Memory Full",font=("Arial",24))
miLabel.pack()
miLabel.place(x=580,y=55)
miFrame = Frame()
miFrame.pack(fill="x",expand="True")
miFrame.config(bg="red")
miFrame.config(width="399",height="399")
miFrame.config(cursor="hand1")

opciones = ["Nivel inicial","Nivel medio","Nivel avanzado"]

combo = ttk.Combobox(miFrame,font=('Arial',10),state="readonly",values=opciones)
combo.place(x=190,y=100)
numNivel = Label(miFrame, text="Ingrese el nivel de dificultad: ",bg="red")
numNivel.place(x=10,y=100)
labelnumpalabras = Label(miFrame,text="Cuantas palabras desea memorizar: ",bg="red")
labelnumpalabras.place(x=10,y=150)
entrynumpalabras =tk.StringVar()
camponumpalabras = Entry(miFrame,textvariable=entrynumpalabras)
camponumpalabras.place(x=200,y=150)
boton = tk.Button(miFrame,text="Ejecutar programa",command=arrancarEntrenamiento)
boton.place(x=350,y=150)
entrypalabra = tk.StringVar()
campopalabra=Label(miFrame, textvariable=entrypalabra)
campopalabra.place(x=200,y=250,width=100,height=50)
""" valorseleccionado = combo.get()
print(valorseleccionado) """
raiz.mainloop()