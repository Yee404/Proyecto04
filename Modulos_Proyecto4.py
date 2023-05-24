def Read():
    with open("excel.csv","r", encoding = "ISO-8859-1") as info_m:
        Texto = info_m.read()
        info_m.close()
        registros = []
        lineas = Texto.split("\n")
        lineas.pop()
        for i in lineas:
            linea = i.split(",")
            registros.append(linea)
        return(registros)
    
def NuevoUsuario(x):
    new_line = ",".join(x)
    new_line += "\n"
    with open("excel.csv","a", encoding = "ISO-8859-1") as info_m:
        Texto = info_m.write(new_line)
    info_m.close()

def SignIn():
    UserCreated = str(user.get())
    PasswordCreated = str(password.get())
    Exist = False
    for i in range(1,len(registros)):
        if (registros[i][0] == UserCreated and registros[i][1] == PasswordCreated):
            Exist = True
            window.destroy()
            APP = Tk()
            APP.title('Sign In')
            APP.geometry('1000x600+250+100')
            APP.configure(bg="red")
            APP.resizable(False, False)
            # 
            APP.mainloop()
    if Exist == False:
        messagebox.showinfo(title = "Error", message = "Incorrect username or password")

#def DIAGNOSTIC():
def DIAGNOSTIC():
    import tkinter as tk
    from tkinter import ttk


    DIAG = tk.Tk()
    DIAG.title('Diagnostic')
    DIAG.geometry('1000x600+250+100')
    DIAG.configure(bg="#FFFFFF")
    #DIAG.resizable(False, False)

    frame1 = tk.Frame(DIAG,width=40, height=580, bg='#429351')
    frame1.place(x=5,y=10)
    frame2 = tk.Frame(DIAG,width=940, height=580, bg='#B7E18E')
    frame2.place(x=50,y=10)

    def diagnostico():
        class ScrollableFrame(ttk.Frame):
            def __init__(self, container, *args, **kwargs):
                super().__init__(container, *args, **kwargs)
                canvas = tk.Canvas(self)
                scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
                self.scrollable_frame = ttk.Frame(canvas)

                self.scrollable_frame.bind(
                    "<Configure>",
                    lambda e: canvas.configure(
                        scrollregion=canvas.bbox("all")))

                canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

                canvas.configure(yscrollcommand=scrollbar.set)

                canvas.pack(side="left", fill="both", expand=True)
                scrollbar.pack(side="right", fill="y")


        diag = tk.Tk()
        diag.geometry('1000x600+250+100')
        frame = ScrollableFrame(diag,width=100, height=80)
        # TEXTO\n
        hora0 = tk.Label(frame2,width=140, height=20, bg='red')

        hora1 = tk.Frame(frame2,width=140, height=20, bg='red')

        hora2 = tk.Frame(frame2,width=140, height=20, bg='red')

        hora3 = tk.Frame(frame2,width=140, height=20, bg='red')

        hora4 = tk.Frame(frame2,width=140, height=20, bg='red')

        hora5 = tk.Frame(frame2,width=140, height=20, bg='red')

        hora6 = tk.Frame(frame2,width=140, height=20, bg='red')

        hora7 = tk.Frame(frame2,width=140, height=20, bg='red')

        hora8 = tk.Frame(frame2,width=140, height=20, bg='red')

        hora9 = tk.Frame(frame2,width=140, height=20, bg='red')

        hora10 = tk.Frame(frame2,width=140, height=20, bg='red')

        hora11 = tk.Frame(frame2,width=140, height=20, bg='red')

        hora12 = tk.Frame(frame2,width=140, height=20, bg='red')

        hora13 = tk.Frame(frame2,width=140, height=20, bg='red')

        hora14 = tk.Frame(frame2,width=140, height=20, bg='red')

        hora15 = tk.Frame(frame2,width=140, height=20, bg='red')

        frame.pack()
        diag.mainloop()


    # HORARIO
    fond = tk.Frame(frame2,width=920, height=550, bg='#F5F5F5')
    fond.place(x=10,y=25)

    horas = tk.Frame(frame2,width=50, height=535, bg='light gray')
    horas.place(x=20,y=35)

    clun = tk.Label(frame2,width=19, height=2, fg="white",bg='#429351', text='LUNES', font=('Roboto',10))
    clun.place(x=80,y=35)

    cmart = tk.Label(frame2,width=19, height=2, fg="white", bg='#429351', text='MARTES', font=('Roboto',10))
    cmart.place(x=250,y=35)

    cmier = tk.Label(frame2,width=19, height=2, fg="white", bg='#429351', text='MIERCOLES', font=('Roboto',10))
    cmier.place(x=420,y=35)

    cjuev = tk.Label(frame2,width=19, height=2, fg="white", bg='#429351', text='JUEVES', font=('Roboto',10))
    cjuev.place(x=590,y=35)

    cvier = tk.Label(frame2,width=19, height=2, fg="white", bg='#429351', text='VIERNES', font=('Roboto',10))
    cvier.place(x=760,y=35)

    lun = tk.Frame(frame2,width=160, height=490, bg='#EEEEEE')
    lun.place(x=80,y=80)

    mart = tk.Frame(frame2,width=160, height=490, bg='#EEEEEE')
    mart.place(x=250,y=80)

    mier = tk.Frame(frame2,width=160, height=490, bg='#EEEEEE')
    mier.place(x=420,y=80)

    juev = tk.Frame(frame2,width=160, height=490, bg='#EEEEEE')
    juev.place(x=590,y=80)

    vier = tk.Frame(frame2,width=160, height=490, bg='#EEEEEE')
    vier.place(x=760,y=80)

    #n6 = input("Ingrese la actividad: ")

    n6 = ""
    n7 = ""
    n8 = ""
    n9 = ""
    n10 = ""
    n11 = ""
    n12 = ""
    n13 = ""
    n14 = ""
    n15 = ""
    n16 = ""
    n17 = ""
    n18 = ""
    n19 = ""
    n20 = ""
    n21 = ""

    hora6 = tk.Entry(frame2, bg='light gray', text= n6, font=('Arial',10))
    hora6.place(x=90,y=90)

    hora7 = tk.Entry(frame2, bg='light gray', text= n7, font=('Arial',10))
    hora7.place(x=90,y=120)

    hora8 = tk.Entry(frame2, bg='light gray', text= n8, font=('Arial',10))
    hora8.place(x=90,y=150)

    hora9 = tk.Entry(frame2, bg='light gray', text= n9, font=('Arial',10))
    hora9.place(x=90,y=180)

    hora10 = tk.Entry(frame2, bg='light gray', text= n10, font=('Arial',10))
    hora10.place(x=90,y=210)

    hora11 = tk.Entry(frame2, bg='light gray', text= n11, font=('Arial',10))
    hora11.place(x=90,y=240)

    hora12 = tk.Entry(frame2, bg='light gray', text= n12, font=('Arial',10))
    hora12.place(x=90,y=270)

    hora13 = tk.Entry(frame2, bg='light gray', text= n13, font=('Arial',10))
    hora13.place(x=90,y=300)

    hora14 = tk.Entry(frame2, bg='light gray', text= n14, font=('Arial',10))
    hora14.place(x=90,y=330)

    hora15 = tk.Entry(frame2, bg='light gray', text= n15, font=('Arial',10))
    hora15.place(x=90,y=360)

    hora16 = tk.Entry(frame2, bg='light gray', text= n16, font=('Arial',10))
    hora16.place(x=90,y=390)

    hora17 = tk.Entry(frame2, bg='light gray', text= n17, font=('Arial',10))
    hora17.place(x=90,y=420)

    hora18 = tk.Entry(frame2, bg='light gray', text= n18, font=('Arial',10))
    hora18.place(x=90,y=450)

    hora19 = tk.Entry(frame2, bg='light gray', text= n19, font=('Arial',10))
    hora19.place(x=90,y=480)

    hora20 = tk.Entry(frame2, bg='light gray', text= n20, font=('Arial',10))
    hora20.place(x=90,y=510)

    hora21 = tk.Entry(frame2, bg='light gray', text= n21, font=('Arial',10))
    hora21.place(x=90,y=540)

    #_________________________________________________________________________________________________________

    hora62 = tk.Entry(frame2, bg='light gray', text= n6, font=('Arial',10))
    hora62.place(x=260,y=90)

    hora72 = tk.Entry(frame2, bg='light gray', text= n7, font=('Arial',10))
    hora72.place(x=260,y=120)

    hora82 = tk.Entry(frame2, bg='light gray', text= n8, font=('Arial',10))
    hora82.place(x=260,y=150)

    hora92 = tk.Entry(frame2, bg='light gray', text= n9, font=('Arial',10))
    hora92.place(x=260,y=180)

    hora102 = tk.Entry(frame2, bg='light gray', text= n10, font=('Arial',10))
    hora102.place(x=260,y=210)

    hora112 = tk.Entry(frame2, bg='light gray', text= n11, font=('Arial',10))
    hora112.place(x=260,y=240)

    hora122 = tk.Entry(frame2, bg='light gray', text= n12, font=('Arial',10))
    hora122.place(x=260,y=270)

    hora132 = tk.Entry(frame2, bg='light gray', text= n13, font=('Arial',10))
    hora132.place(x=260,y=300)

    hora142 = tk.Entry(frame2, bg='light gray', text= n14, font=('Arial',10))
    hora142.place(x=260,y=330)

    hora152 = tk.Entry(frame2, bg='light gray', text= n15, font=('Arial',10))
    hora152.place(x=260,y=360)

    hora162 = tk.Entry(frame2, bg='light gray', text= n16, font=('Arial',10))
    hora162.place(x=260,y=390)

    hora172 = tk.Entry(frame2, bg='light gray', text= n17, font=('Arial',10))
    hora172.place(x=260,y=420)

    hora182 = tk.Entry(frame2, bg='light gray', text= n18, font=('Arial',10))
    hora182.place(x=260,y=450)

    hora192 = tk.Entry(frame2, bg='light gray', text= n19, font=('Arial',10))
    hora192.place(x=260,y=480)

    hora202 = tk.Entry(frame2, bg='light gray', text= n20, font=('Arial',10))
    hora202.place(x=260,y=510)

    hora212 = tk.Entry(frame2, bg='light gray', text= n21, font=('Arial',10))
    hora212.place(x=260,y=540)

    #_______________________________________________________________________________________________________

    hora63 = tk.Entry(frame2, bg='light gray', text= n6, font=('Arial',10))
    hora63.place(x=430,y=90)

    hora73 = tk.Entry(frame2, bg='light gray', text= n7, font=('Arial',10))
    hora73.place(x=430,y=120)

    hora83 = tk.Entry(frame2, bg='light gray', text= n8, font=('Arial',10))
    hora83.place(x=430,y=150)

    hora93 = tk.Entry(frame2, bg='light gray', text= n9, font=('Arial',10))
    hora93.place(x=430,y=180)

    hora103 = tk.Entry(frame2, bg='light gray', text= n10, font=('Arial',10))
    hora103.place(x=430,y=210)

    hora113 = tk.Entry(frame2, bg='light gray', text= n11, font=('Arial',10))
    hora113.place(x=430,y=240)

    hora123 = tk.Entry(frame2, bg='light gray', text= n12, font=('Arial',10))
    hora123.place(x=430,y=270)

    hora133 = tk.Entry(frame2, bg='light gray', text= n13, font=('Arial',10))
    hora133.place(x=430,y=300)

    hora143 = tk.Entry(frame2, bg='light gray', text= n14, font=('Arial',10))
    hora143.place(x=430,y=330)

    hora153 = tk.Entry(frame2, bg='light gray', text= n15, font=('Arial',10))
    hora153.place(x=430,y=360)

    hora163 = tk.Entry(frame2, bg='light gray', text= n16, font=('Arial',10))
    hora163.place(x=430,y=390)

    hora173 = tk.Entry(frame2, bg='light gray', text= n17, font=('Arial',10))
    hora173.place(x=430,y=420)

    hora183 = tk.Entry(frame2, bg='light gray', text= n18, font=('Arial',10))
    hora183.place(x=430,y=450)

    hora193 = tk.Entry(frame2, bg='light gray', text= n19, font=('Arial',10))
    hora193.place(x=430,y=480)

    hora203 = tk.Entry(frame2, bg='light gray', text= n20, font=('Arial',10))
    hora203.place(x=430,y=510)

    hora213 = tk.Entry(frame2, bg='light gray', text= n21, font=('Arial',10))
    hora213.place(x=430,y=540)

    #_________________________________________________________________________________________________________
    hora64 = tk.Entry(frame2, bg='light gray', text= n6, font=('Arial',10))
    hora64.place(x=600,y=90)

    hora74 = tk.Entry(frame2, bg='light gray', text= n7, font=('Arial',10))
    hora74.place(x=600,y=120)

    hora84 = tk.Entry(frame2, bg='light gray', text= n8, font=('Arial',10))
    hora84.place(x=600,y=150)

    hora94 = tk.Entry(frame2, bg='light gray', text= n9, font=('Arial',10))
    hora94.place(x=600,y=180)

    hora104 = tk.Entry(frame2, bg='light gray', text= n10, font=('Arial',10))
    hora104.place(x=600,y=210)

    hora114 = tk.Entry(frame2, bg='light gray', text= n11, font=('Arial',10))
    hora114.place(x=600,y=240)

    hora124 = tk.Entry(frame2, bg='light gray', text= n12, font=('Arial',10))
    hora124.place(x=600,y=270)

    hora134 = tk.Entry(frame2, bg='light gray', text= n13, font=('Arial',10))
    hora134.place(x=600,y=300)

    hora144 = tk.Entry(frame2, bg='light gray', text= n14, font=('Arial',10))
    hora144.place(x=600,y=330)

    hora154 = tk.Entry(frame2, bg='light gray', text= n15, font=('Arial',10))
    hora154.place(x=600,y=360)

    hora164 = tk.Entry(frame2, bg='light gray', text= n16, font=('Arial',10))
    hora164.place(x=600,y=390)

    hora174 = tk.Entry(frame2, bg='light gray', text= n17, font=('Arial',10))
    hora174.place(x=600,y=420)

    hora184 = tk.Entry(frame2, bg='light gray', text= n18, font=('Arial',10))
    hora184.place(x=600,y=450)

    hora194 = tk.Entry(frame2, bg='light gray', text= n19, font=('Arial',10))
    hora194.place(x=600,y=480)

    hora204 = tk.Entry(frame2, bg='light gray', text= n20, font=('Arial',10))
    hora204.place(x=600,y=510)

    hora214 = tk.Entry(frame2, bg='light gray', text= n21, font=('Arial',10))
    hora214.place(x=600,y=540)

    #______________________________________________________________________________________________________

    hora65 = tk.Entry(frame2, bg='light gray', text= n6, font=('Arial',10))
    hora65.place(x=770,y=90)

    hora75 = tk.Entry(frame2, bg='light gray', text= n7, font=('Arial',10))
    hora75.place(x=770,y=120)

    hora85 = tk.Entry(frame2, bg='light gray', text= n8, font=('Arial',10))
    hora85.place(x=770,y=150)

    hora95 = tk.Entry(frame2, bg='light gray', text= n9, font=('Arial',10))
    hora95.place(x=770,y=180)

    hora105 = tk.Entry(frame2, bg='light gray', text= n10, font=('Arial',10))
    hora105.place(x=770,y=210)

    hora115 = tk.Entry(frame2, bg='light gray', text= n11, font=('Arial',10))
    hora115.place(x=770,y=240)

    hora125 = tk.Entry(frame2, bg='light gray', text= n12, font=('Arial',10))
    hora125.place(x=770,y=270)

    hora135 = tk.Entry(frame2, bg='light gray', text= n13, font=('Arial',10))
    hora135.place(x=770,y=300)

    hora145 = tk.Entry(frame2, bg='light gray', text= n14, font=('Arial',10))
    hora145.place(x=770,y=330)

    hora155 = tk.Entry(frame2, bg='light gray', text= n15, font=('Arial',10))
    hora155.place(x=770,y=360)

    hora165 = tk.Entry(frame2, bg='light gray', text= n16, font=('Arial',10))
    hora165.place(x=770,y=390)

    hora175 = tk.Entry(frame2, bg='light gray', text= n17, font=('Arial',10))
    hora175.place(x=770,y=420)

    hora185 = tk.Entry(frame2, bg='light gray', text= n18, font=('Arial',10))
    hora185.place(x=770,y=450)

    hora195 = tk.Entry(frame2, bg='light gray', text= n19, font=('Arial',10))
    hora195.place(x=770,y=480)

    hora205 = tk.Entry(frame2, bg='light gray', text= n20, font=('Arial',10))
    hora205.place(x=770,y=510)

    hora215 = tk.Entry(frame2, bg='light gray', text= n21, font=('Arial',10))
    hora215.place(x=770,y=540)

    #______________________________________________________________________________________________________
    # HORAS

    hora60 = tk.Label(frame2, width=4, height=1, bg='#EEEEEE', text='6:00', font=('Arial',10))
    hora60.place(x=25,y=90)

    hora70 = tk.Label(frame2, width=4, height=1,bg='#EEEEEE', text= '7:00', font=('Arial',10))
    hora70.place(x=25,y=120)

    hora80 = tk.Label(frame2, width=4, height=1,bg='#EEEEEE', text= '8:00', font=('Arial',10))
    hora80.place(x=25,y=150)

    hora90 = tk.Label(frame2, width=4, height=1,bg='#EEEEEE', text= '9:00', font=('Arial',10))
    hora90.place(x=25,y=180)

    hora100 = tk.Label(frame2, width=4, height=1,bg='#EEEEEE', text= '10:00', font=('Arial',10))
    hora100.place(x=25,y=210)

    hora110 = tk.Label(frame2, width=4, height=1,bg='#EEEEEE', text= '11:00', font=('Arial',10))
    hora110.place(x=25,y=240)

    hora120 = tk.Label(frame2, width=4, height=1,bg='#EEEEEE', text= '12:00', font=('Arial',10))
    hora120.place(x=25,y=270)

    hora130 = tk.Label(frame2, width=4, height=1,bg='#EEEEEE', text= '13:00', font=('Arial',10))
    hora130.place(x=25,y=300)

    hora140 = tk.Label(frame2, width=4, height=1,bg='#EEEEEE', text= '14:00', font=('Arial',10))
    hora140.place(x=25,y=330)

    hora150 = tk.Label(frame2, width=4, height=1,bg='#EEEEEE', text= '15:00', font=('Arial',10))
    hora150.place(x=25,y=360)

    hora160 = tk.Label(frame2, width=4, height=1,bg='#EEEEEE', text= '16:00', font=('Arial',10))
    hora160.place(x=25,y=390)

    hora170 = tk.Label(frame2, width=4, height=1,bg='#EEEEEE', text= '17:00', font=('Arial',10))
    hora170.place(x=25,y=420)

    hora180 = tk.Label(frame2, width=4, height=1,bg='#EEEEEE', text= '18:00', font=('Arial',10))
    hora180.place(x=25,y=450)

    hora190 = tk.Label(frame2, width=4, height=1,bg='#EEEEEE', text= '19:00', font=('Arial',10))
    hora190.place(x=25,y=480)

    hora200 = tk.Label(frame2, width=4, height=1,bg='#EEEEEE', text= '20:00', font=('Arial',10))
    hora200.place(x=25,y=510)

    hora210 = tk.Label(frame2, width=4, height=1,bg='#EEEEEE', text= '21:00', font=('Arial',10))
    hora210.place(x=25,y=540)

    DIAG.mainloop()