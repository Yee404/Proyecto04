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