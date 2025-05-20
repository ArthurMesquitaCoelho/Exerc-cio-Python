from datetime import datetime

# Classe para gerenciar a conta bancária
class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.limite_saque = 500.0
        self.limite_saques_diarios = 3
        self.saques_realizados = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Depósito: R$ {valor:.2f}")
            print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("❌ Valor de depósito inválido.")

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saques_diarios:
            print("❌ Limite diário de saques atingido.")
        elif valor > self.limite_saque:
            print(f"❌ Saque excede o limite de R$ {self.limite_saque:.2f}.")
        elif valor > self.saldo:
            print("❌ Saldo insuficiente.")
        elif valor > 0:
            self.saldo -= valor
            self.saques_realizados += 1
            self.extrato.append(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Saque: R$ {valor:.2f}")
            print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("❌ Valor de saque inválido.")

    def exibir_extrato(self):
        print("\n========== EXTRATO ==========")
        if not self.extrato:
            print("⚠️  Nenhuma movimentação registrada.")
        else:
            for item in self.extrato:
                print(item)
        print(f"\n💰 Saldo atual: R$ {self.saldo:.2f}")
        print("=============================\n")

# Classe para gerenciar os usuários
class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.conta = ContaBancaria()

# Base simulada de usuários (simulação de banco de dados)
usuarios = {}

# Funções auxiliares
def cadastrar_usuario():
    nome = input("Escolha um nome de usuário: ")
    if nome in usuarios:
        print("❌ Nome já está em uso.")
        return
    senha = input("Defina uma senha: ")
    usuarios[nome] = Usuario(nome, senha)
    print("✅ Cadastro realizado com sucesso.")

def autenticar_usuario():
    nome = input("Usuário: ")
    senha = input("Senha: ")
    usuario = usuarios.get(nome)
    if usuario and usuario.senha == senha:
        print(f"✅ Bem-vindo, {nome}!")
        return usuario
    else:
        print("❌ Usuário ou senha incorretos.")
        return None

# Menu principal
def menu_principal():
    while True:
        print("\n=== BANCO PYTHON ===")
        print("[1] Cadastrar novo usuário")
        print("[2] Login")
        print("[0] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            usuario = autenticar_usuario()
            if usuario:
                menu_usuario(usuario)
        elif opcao == "0":
            print("👋 Até logo!")
            break
        else:
            print("❌ Opção inválida.")

# Menu do usuário logado
def menu_usuario(usuario):
    while True:
        print(f"\n=== Conta de {usuario.nome} ===")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Ver Extrato")
        print("[0] Logout")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                valor = float(input("Valor do depósito: R$ "))
                usuario.conta.depositar(valor)
            except ValueError:
                print("❌ Entrada inválida.")
        elif opcao == "2":
            try:
                valor = float(input("Valor do saque: R$ "))
                usuario.conta.sacar(valor)
            except ValueError:
                print("❌ Entrada inválida.")
        elif opcao == "3":
            usuario.conta.exibir_extrato()
        elif opcao == "0":
            print(f"🔒 Logout de {usuario.nome} realizado.")
            break
        else:
            print("❌ Opção inválida.")

# Inicia o programa
menu_principal()
