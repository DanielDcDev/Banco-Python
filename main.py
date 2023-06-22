import tkinter as tk
from tkinter import messagebox
from connection import Verify_login_senha
from connection import Insert

entry_nome = None
entry_login = None
entry_senha = None
entry_sexo = None

def verificar_senha():
    senha = entry_senha.get()
    if len(senha) == 8:
        realizar_login()
    else:
        messagebox.showerror("Erro", "A senha deve ter exatamente 8 caracteres.")

def realizar_login():
    login = entry_login.get()
    senha = entry_senha.get()

    try:
        if Verify_login_senha(login, senha):
            messagebox.showinfo("Erro", "Login  nao realizado!")
        else:
            messagebox.showerror("Sucesso", "login executado")
            abrir_tela_principal()
    except TypeError:
        messagebox.showerror("Erro", "Ocorreu um erro durante a verificação do login.")

def cadastrar():
    global entry_nome, entry_login, entry_senha, entry_sexo

    nome = entry_nome.get()
    login = entry_login.get()
    senha = entry_senha.get()
    sexo = entry_sexo.get()

    # Verifica campos vazios
    if nome == "" or login == "" or senha == "" or sexo == "":
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    else:
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        Insert(nome, login, senha, sexo)

def mostrar_caracteres():
    entry_senha.configure(show="")

def ocultar_caracteres():
    entry_senha.configure(show="*")

def abrir_tela_cadastro():
    global entry_nome, entry_login, entry_senha, entry_sexo

    root.withdraw()  # Fecha a janela de login
    janela_cadastro = tk.Toplevel(root)
    janela_cadastro.title("Cadastro")
    janela_cadastro.configure(bg="black")

    frame_cadastro = tk.Frame(janela_cadastro, bg="gray", bd=2)
    frame_cadastro.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    label_nome = tk.Label(frame_cadastro, text="Nome:", bg="gray", fg="white")
    label_nome.pack()

    entry_nome = tk.Entry(frame_cadastro)
    entry_nome.pack()

    label_login = tk.Label(frame_cadastro, text="Login:", bg="gray", fg="white")
    label_login.pack()

    entry_login = tk.Entry(frame_cadastro)
    entry_login.pack()

    label_senha = tk.Label(frame_cadastro, text="Senha:", bg="gray", fg="white")
    label_senha.pack()

    entry_senha = tk.Entry(frame_cadastro, show="*")
    entry_senha.pack()

    label_sexo = tk.Label(frame_cadastro, text="Sexo:", bg="gray", fg="white")
    label_sexo.pack()

    entry_sexo = tk.Entry(frame_cadastro)
    entry_sexo.pack()

    button_cadastrar = tk.Button(frame_cadastro, text="Cadastrar", command=cadastrar)
    button_cadastrar.pack()

    def fechar_tela_cadastro():
        janela_cadastro.destroy()
        root.deiconify()  # Exibe novamente a janela de login

    janela_cadastro.protocol("WM_DELETE_WINDOW", fechar_tela_cadastro)  # Trata o evento de fechar a janela de cadastro

def abrir_tela_principal():
    global entry_login

    root.withdraw()  # Fecha a janela de login
    janela_principal = tk.Toplevel(root)
    janela_principal.title("Tela Principal")
    janela_principal.configure(bg="black")

    frame_principal = tk.Frame(janela_principal, bg="gray", bd=2)
    frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    label_bem_vindo = tk.Label(frame_principal, text="Bem-vindo!", bg="gray", fg="white")
    label_bem_vindo.pack()

    label_usuario = tk.Label(frame_principal, text="Usuário:", bg="gray", fg="white")
    label_usuario.pack()

    entry_usuario = tk.Entry(frame_principal)
    entry_usuario.insert(tk.END, entry_login.get())  # Preenche o campo de usuário com o login
    entry_usuario.configure(state="readonly")
    entry_usuario.pack()

    def fechar_tela_principal():
        janela_principal.destroy()
        root.deiconify()  # Exibe novamente a janela de login

    janela_principal.protocol("WM_DELETE_WINDOW", fechar_tela_principal)  # Trata o evento de fechar a janela principal

root = tk.Tk()
root.title("Verificação de Login e Senha")

loginV = None
senhaV = None

root.configure(bg="black")

frame = tk.Frame(root, bg="gray", bd=2)
frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

label_login = tk.Label(frame, text="Login:", bg="gray", fg="white")
label_login.pack()

entry_login = tk.Entry(frame)
entry_login.pack()

label_senha = tk.Label(frame, text="Senha:", bg="gray", fg="white")
label_senha.pack()

entry_senha = tk.Entry(frame, show="*")
entry_senha.pack()

button_mostrar = tk.Button(frame, text="Mostrar", command=mostrar_caracteres)
button_mostrar.pack(side=tk.LEFT)

button_ocultar = tk.Button(frame, text="Ocultar", command=ocultar_caracteres)
button_ocultar.pack(side=tk.LEFT)

button_verificar = tk.Button(frame, text="Verificar Senha", command=verificar_senha)
button_verificar.pack()

button_login = tk.Button(frame, text="Login", command=realizar_login)
button_login.pack()

button_cadastrar_se = tk.Button(frame, text="Cadastrar-se", command=abrir_tela_cadastro)
button_cadastrar_se.pack()

root.mainloop()
