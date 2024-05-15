import tkinter
import customtkinter
from PIL import ImageTk,Image

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("green")  

def botao_login():
    global email, senha, ErroCerto

    EmailInserido = email.get()
    SenhaInserida = senha.get()

    Usuarios = {
        "AlessandroLindao@gmail.com": "123",
        "HenqiueChad@gmail.com": "123",
        "JaoGrandao@gmail.com": "123"
    }

    if EmailInserido in Usuarios:
        if Usuarios[EmailInserido] == SenhaInserida:
            ErroCerto.configure(text="Login bem-sucedido")
            app.destroy()  
            nova_janela() 
        else:
            ErroCerto.configure(text="Senha inválida", text_color="red")
    else:
        ErroCerto.configure(text="Email inválido")

def nova_janela():
    app.destroy()
    main = customtkinter.CTk()
    main.geometry("1280x720")
    main.title("Página Principal")
    main.mainloop()


app = customtkinter.CTk()  
app.geometry("600x440")
app.title('Login')


img1=ImageTk.PhotoImage(Image.open("image.png"))
Plano1=customtkinter.CTkLabel(master=app,image=img1)
Plano1.pack()

Caixa=customtkinter.CTkFrame(master=Plano1, width=320, height=360, corner_radius=15)
Caixa.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

Plano2 = customtkinter.CTkLabel(master=Caixa, text="Faça login com sua conta", font=("Century Gothic", 20))
Plano2.place(x=35,y=45)

email = customtkinter.CTkEntry(master=Caixa, placeholder_text="Email", width=220)
email.place(x=50, y=110)

ErroCerto = customtkinter.CTkLabel(master=app, text="")
ErroCerto.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(master=Caixa, placeholder_text="Senha", width=220, show="*")
senha.place(x=50, y=165)

Plano2 = customtkinter.CTkLabel(master=Caixa, text="Esqueceu a senha?", font=("Century Gothic", 12))
Plano2.place(x=155,y=195)

Login = customtkinter.CTkButton(master=Caixa, width=220, text="Login", corner_radius=6, fg_color="#EFB810", text_color="black", command=botao_login, hover_color='#a87b05')
Login.place(x=50, y=240)

img2=customtkinter.CTkImage(Image.open("124010.png").resize((20,20)))
img3 = customtkinter.CTkImage(Image.open("Google__G__Logo.svg.webp").resize((20,20)))


google = customtkinter.CTkButton(master=Caixa, image=img3, text="Google", width=100, height=20, corner_radius=6, compound="left", text_color="black",
                                fg_color="white",
                                hover_color="#AAAAAA")
google.place(x=50, y=290)

facebook = customtkinter.CTkButton(master=Caixa, image=img2, text="Facebook", width=100, height=20, corner_radius=6, compound="left", text_color="black",
                                fg_color="white",
                                hover_color="#AAAAAA")
facebook.place(x=170, y=290)



app.mainloop()

