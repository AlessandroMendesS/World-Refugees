import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def clique():
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
            janelaLogin.destroy()  
            nova_janela() 
        else:
            ErroCerto.configure(text="Senha inválida")
    else:
        ErroCerto.configure(text="Email inválido")

def nova_janela():
    janela = customtkinter.CTk()
    janela.geometry("500x300")
    janela.title("Página Principal")

    janela.mainloop()

janelaInicial = customtkinter.CTk()
janelaInicial.geometry('500x300')
janelaInicial.title('Página Inicial')

texto = customtkinter.CTkLabel(janelaInicial, text='Bem-Vindo', font=('Consolas',25,'bold'))
texto.pack(padx=10, pady=30)

texto1 = customtkinter.CTkLabel(janelaInicial, text='World Refugees', font=('Open Sans',24))
texto1.pack(padx=10,pady=10)

botaoAvancar = customtkinter.CTkButton(janelaInicial, text='Avançar', width=50, height=10)
botaoAvancar.pack(padx=10,pady=10)


texto2 = customtkinter.CTkLabel(janelaInicial, text='From Senai', font=('Open Sans',8))
texto2.pack(padx=10, pady=10)


janelaInicial.mainloop()

    

janelaLogin = customtkinter.CTk()
janelaLogin.geometry("500x300")
janelaLogin.title("Página de Login")

texto = customtkinter.CTkLabel(janelaLogin, text="Fazer Login", font=("Consolas", 18, "bold"))
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janelaLogin, placeholder_text="Seu email", font=("Consolas", 12))
email.pack(padx=10,pady=10)

senha = customtkinter.CTkEntry(janelaLogin, placeholder_text="Sua senha", show="*", font=("Consolas", 12))
senha.pack(padx=10, pady=10)

lembrasenha = customtkinter.CTkCheckBox(janelaLogin, text="Lembrar Login")
lembrasenha.pack(padx=10, pady=10)

botaoLogin = customtkinter.CTkButton(janelaLogin, text="Login", command=clique, fg_color='#EBB600', text_color='black')
botaoLogin.pack(padx=10, pady=10)

ErroCerto = customtkinter.CTkLabel(janelaLogin, text="")
ErroCerto.pack(padx=10, pady=10)

janelaLogin.mainloop()


