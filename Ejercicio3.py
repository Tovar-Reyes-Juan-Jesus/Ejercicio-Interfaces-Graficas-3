from tkinter import *
from tkinter import ttk
import tkinter as ttk

raiz = Tk()

raiz.title("Ejercicio 3")
raiz.geometry("1450x750")
raiz.config(bg="white",borderwidth=0)

#Frames necesarios 

frame = Frame(raiz,background="black",width=2100,height=1800)
frame.grid()
frame.grid_propagate(False)
#frame.place(x=0,y=0)

frame2 = Frame(frame,background="#10747c",width=2100,height=50,borderwidth=0)
frame2.grid(column=0,row=0,columnspan=2,sticky=N)

frame3 = Frame(frame,height=1000,borderwidth=0,background="black",width=100)
frame3.grid(column=0,row=1)

frame4 = Frame(frame,background="#383434",width=210,height=350,padx=5,pady=5)
frame4.grid(column=1,row=0,rowspan=2)
frame4.place(x=50,y=50)
frame4.grid_propagate(False)

frame5 = Frame(frame,background="#383434",width=460,height=350,padx=1,pady=1)
frame5.grid(column=2,row=0,rowspan=2)
frame5.place(x=270,y=50)
frame5.grid_propagate(False)

frame6 = Frame(frame,background="#383434",width=600,height=450,padx=1,pady=1)
frame6.grid(column=3,row=0,rowspan=2,columnspan=4)
frame6.place(x=740,y=50)
frame6.grid_propagate(False)

frame7 = Frame(frame,height=300,borderwidth=0,background="#383434",width=360)
frame7.grid(column=1,row=0,columnspan=2)
frame7.place(x=50,y=410)
frame7.grid_propagate(False)

frame8 = Frame(frame,height=300,borderwidth=0,background="#383434",width=310)
frame8.grid(column=1,row=0,columnspan=2)
frame8.place(x=420,y=410)
frame8.grid_propagate(False)

#titulo Frame 2

imagen = PhotoImage(file="widget1.PNG") #cremos el objeto imagen
imagen_sub=imagen.subsample(2)
etiqueta=ttk.Label(image=imagen,borderwidth=0)
etiqueta.place(x=20, y=10)



titulo = Label(frame2,text="SPAI 4.0", fg="white",background="#10747c",font=("Arial",20))
titulo.grid(column=0,row=0)
titulo.place(x=60,y=10)

#buttons

indicador = Label(frame4,text="Indicadores Digitales",fg="#10747c",font=("Arial",12,"bold"),background="#383434",compound="center")
indicador.grid(column=0,row=1,columnspan=2)

espacio = Label(frame4,text="",fg="white",font=("Arial",12),background="#383434",compound="center")
espacio.grid(column=0,row=2)

Linea1 = Label(frame4,text="Linea 1:",fg="white",font=("Arial",12),background="#383434",compound="center")
Linea1.grid(column=0,row=3,sticky=W)
On1 = Label(frame4,text="On",fg="white",font=("Arial",12,"bold"),background="#383434",compound="center")
On1.grid(column=1,row=3,sticky=W)
circulo = PhotoImage(file="circulogreen.PNG") #cremos el objeto imagen
imagen_sub=circulo.subsample(2)
etiqueta1=ttk.Label(frame4,image=circulo,borderwidth=0)
etiqueta1.place(x=170, y=53)


espacio = Label(frame4,text="",fg="white",font=("Arial",12),background="#383434",compound="center")
espacio.grid(column=0,row=4)

Linea2 = Label(frame4,text="Linea 2:",fg="white",font=("Arial",12),background="#383434",compound="center")
Linea2.grid(column=0,row=5,sticky=W)
On2 = Label(frame4,text="On",fg="white",font=("Arial",12,"bold"),background="#383434",compound="center")
On2.grid(column=1,row=5,sticky=W)
circulo1 = PhotoImage(file="circulogreen.PNG") #cremos el objeto imagen
imagen_sub=circulo1.subsample(2)
etiqueta2=ttk.Label(frame4,image=circulo1,borderwidth=0)
etiqueta2.place(x=170, y=100)

espacio = Label(frame4,text="",fg="white",font=("Arial",12),background="#383434",compound="center")
espacio.grid(column=0,row=6,sticky=W)

Linea11 = Label(frame4,text="Linea 1:",fg="white",font=("Arial",12),background="#383434",compound="center")
Linea11.grid(column=0,row=7,sticky=W)
On3 = Label(frame4,text="On",fg="white",font=("Arial",12,"bold"),background="#383434",compound="center")
On3.grid(column=1,row=7,sticky=W)
circulo2 = PhotoImage(file="circulogreen.PNG") #cremos el objeto imagen
imagen_sub=circulo2.subsample(2)
etiqueta2=ttk.Label(frame4,image=circulo2,borderwidth=0)
etiqueta2.place(x=170, y=150)

espacio = Label(frame4,text="",fg="white",font=("Arial",12),background="#383434",compound="center")
espacio.grid(column=0,row=8,sticky=W)

Gabinete = Label(frame4,text="Gabinete:",fg="white",font=("Arial",12),background="#383434",compound="center")
Gabinete.grid(column=0,row=9,sticky=W)
On4 = Label(frame4,text="Abierto",fg="white",font=("Arial",12,"bold"),background="#383434",compound="left")
On4.grid(column=0,row=9,sticky=W)
On4.place(x=80,y=197)
circulo3 = PhotoImage(file="circulorojo.PNG") #cremos el objeto imagen
imagen_sub=circulo3.subsample(2)
etiqueta2=ttk.Label(frame4,image=circulo3,borderwidth=0)
etiqueta2.place(x=170, y=201)

espacio = Label(frame4,text="",fg="white",font=("Arial",12),background="#383434",compound="center")
espacio.grid(column=0,row=10,sticky=W)

Alarma = Label(frame4,text="Alarma:",fg="white",font=("Arial",12),background="#383434",compound="center")
Alarma.grid(column=0,row=11,sticky=W)
On5 = Label(frame4,text="On",fg="white",font=("Arial",12,"bold"),background="#383434",compound="center")
On5.grid(column=1,row=11,sticky=W)
circulo4 = PhotoImage(file="circulorojo.PNG") #cremos el objeto imagen
imagen_sub=circulo4.subsample(2)
etiqueta2=ttk.Label(frame4,image=circulo4,borderwidth=0)
etiqueta2.place(x=170, y=247)

espacio = Label(frame4,text="",fg="white",font=("Arial",12),background="#383434",compound="center")
espacio.grid(column=0,row=12,sticky=W)

Alarma2 = Label(frame4,text="Alarma 2:",fg="white",font=("Arial",12),background="#383434",compound="center")
Alarma2.grid(column=0,row=13,sticky=W)
On6 = Label(frame4,text="Off",fg="white",font=("Arial",12,"bold"),background="#383434",compound="center")
On6.grid(column=1,row=13,sticky=W)
circulo5 = PhotoImage(file="circulogreen.PNG") #cremos el objeto imagen
imagen_sub=circulo5.subsample(2)
etiqueta2=ttk.Label(frame4,image=circulo5,borderwidth=0)
etiqueta2.place(x=170, y=296)

#grafica temperaturas

temperatura = Label(frame5,text="Temperaturas",fg="#10747c",font=("Arial",12,"bold"),background="#383434",compound="center",pady=5)
temperatura.grid(column=0,row=1)

espacio = Label(frame5,text="",fg="white",font=("Arial",12),background="#383434",compound="center")
espacio.grid(column=0,row=2,sticky=W,columnspan=2)
espacio = Label(frame5,text="",fg="white",font=("Arial",12),background="#383434",compound="center")
espacio.grid(column=0,row=3,sticky=W,columnspan=2)

temperatura1 = Label(frame5,text="Temperatura 1:",fg="white",font=("Arial",12,"bold"),background="#383434",compound="center",padx=50)
temperatura1.grid(column=0,row=4)

temperatura2 = Label(frame5,text="Temperatura 2:",fg="white",font=("Arial",12,"bold"),background="#383434",compound="center")
temperatura2.grid(column=1,row=4)
temperatura2.place(x=250,y=74)

medidor = PhotoImage(file="medidores.PNG") #cremos el objeto imagen
imagen_zoom=medidor.zoom(10)
etiqueta2=ttk.Label(frame5,image=medidor,borderwidth=0)
etiqueta2.place(x=50, y=129)

tempAgua = Label(frame5,text="Temp. Agua:",fg="white",font=("Arial",12),background="#383434",compound="center")
tempAgua.grid(column=1,row=5)
tempAgua.place(x=150,y=250)
temp = Label(frame5,text="58 °C",fg="white",font=("Arial",12,"bold"),background="#383434",compound="center")
temp.grid(column=2,row=5)
temp.place(x=250,y=250)

tempAmbiente = Label(frame5,text="Temp. Ambiente:",fg="white",font=("Arial",12),background="#383434",compound="center")
tempAmbiente.grid(column=1,row=6)
tempAmbiente.place(x=130,y=300)
temp1 = Label(frame5,text="32 °C",fg="white",font=("Arial",12,"bold"),background="#383434",compound="center")
temp1.grid(column=2,row=6)
temp1.place(x=260,y=300)

#Produccion
temperatura = Label(frame6,text="Producción",fg="#10747c",font=("Arial",12,"bold"),background="#383434",compound="center",pady=5,padx=10)
temperatura.grid(column=0,row=1)
grafica = PhotoImage(file="grafica.PNG") #cremos el objeto imagen
imagen_sub=grafica.subsample(x=0,y=0)
etiqueta2=ttk.Label(frame6,image=grafica,borderwidth=0)
etiqueta2.place(x=8, y=47)

pzs = Label(frame6,text="Piezas producidas:",fg="white",font=("Arial",12,"bold"),background="#383434",compound="center")
pzs.grid(column=0,row=2)
pzs.place(x=200,y=350)

pzs1 = Label(frame6,text="Piezas defectuosas:",fg="white",font=("Arial",12,"bold"),background="#383434",compound="center")
pzs1.grid(column=0,row=3)
pzs1.place(x=190,y=400)

num = Label(frame6,text="50",fg="white",font=("Arial",12,"bold"),background="#383434",compound="center")
num.grid(column=1,row=2)
num.place(x=360,y=350)

num1 = Label(frame6,text="12",fg="white",font=("Arial",12,"bold"),background="#383434",compound="center")
num1.grid(column=1,row=3)
num1.place(x=360,y=400)

#velicidad
velocidad = Label(frame7,text="Velocidad bomba:",fg="white",font=("Arial",15,"bold"),background="#383434",compound="center")
velocidad.grid(column=0,row=0)
velocidad.place(x=90,y=50)
medidor2 = PhotoImage(file="medidor2.PNG") #cremos el objeto imagen
imagen_sub=medidor2.subsample(x=0,y=0)
etiqueta2=ttk.Label(frame7,image=medidor2,borderwidth=0)
etiqueta2.place(x=50, y=99)

#tanque
tanque = Label(frame8,text="Nivel del Tanque",fg="#10747c",font=("Arial",15,"bold"),background="#383434",compound="center",padx=10,pady=4)
tanque.grid(column=0,row=0)
burbuja = PhotoImage(file="burbuja.PNG") #cremos el objeto imagen
burbuja.zoom(2)
etiqueta2=ttk.Label(frame8,image=burbuja,borderwidth=0)
etiqueta2.place(x=50, y=70)

#scrillroll

barra = Scrollbar(frame)
barra.place(relx=0.64,y=51,relheight=0.4)














raiz.mainloop()