import sys

class ContaBancaria:
    def __init__(self, nome, agencia, conta, senha, saldo=0.0):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.senha = senha
        self.saldo = saldo
        self.limite = 0.0
        self.chaves_pix = []
        self.extrato = []

    def mostrar_dados(self):
        print(f"\nCliente: {self.nome}")
        print(f"Agência: {self.agencia}")
        print(f"Conta: {self.conta}")
        print(f"Saldo atual: R${self.saldo:.2f} (Limite: R${self.limite:.2f})\n")

    def cadastrar_chave_pix(self, chave):
        self.chaves_pix.append(chave)
        self.extrato.append(f"Chave Pix cadastrada: {chave}")
        print("✅ Chave Pix cadastrada com sucesso!")

    def fazer_pix(self, chave, valor):
        if chave in self.chaves_pix:
            print("❌ Não é possível fazer PIX para sua própria chave.")
            return
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            self.extrato.append(f"Pix enviado: -R${valor:.2f} para {chave}")
            print("✅ Seu Pix foi realizado com sucesso!")
        else:
            print("❌ Saldo insuficiente para realizar o Pix.")

    def alterar_limite(self, novo_limite):
        if 0 <= novo_limite <= 1000:
            self.limite = novo_limite
            self.extrato.append(f"Limite alterado para R${novo_limite:.2f}")
            print("✅ Seu limite foi alterado com sucesso!")
        else:
            print("❌ Valor inválido. O limite deve ser entre R$0 e R$1000.")

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        self.extrato.append("Senha alterada com sucesso")
        print("✅ Senha alterada com sucesso!")

    def ver_extrato(self):
        print("\n📜 Extrato de operações:")
        for item in self.extrato:
            print("-", item)
        print(f"Saldo atual: R${self.saldo:.2f}")
        print(f"Limite disponível: R${self.limite:.2f}\n")


#Simulação de login
usuario = ContaBancaria("João Silva", "0001", "12345-6", "1234", 500.0)

print("=== LOGIN ===")
agencia = input("Digite sua agência: ")
conta = input("Digite sua conta: ")
senha = input("Digite sua senha: ")

if agencia != usuario.agencia or conta != usuario.conta or senha != usuario.senha:
    print("❌ Algo não está certo. Verifique seus dados.")
    sys.exit()

print("✅ Login realizado com sucesso!")
usuario.mostrar_dados()

#Menu principal
while True:
    print("=== MENU ===")
    print("1 - Cadastrar chave Pix")
    print("2 - Fazer Pix")
    print("3 - Alterar limite de crédito")
    print("4 - Suporte (alterar senha)")
    print("5 - Ver extrato")
    print("6 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        chave = input("Digite a chave Pix para cadastrar: ")
        usuario.cadastrar_chave_pix(chave)

    elif opcao == "2":
        chave = input("Digite a chave Pix do destinatário: ")
        valor = float(input("Digite o valor do Pix: "))
        usuario.fazer_pix(chave, valor)

    elif opcao == "3":
        novo_limite = float(input("Digite o novo limite (máx R$1000): "))
        usuario.alterar_limite(novo_limite)

    elif opcao == "4":
        nova_senha = input("Digite sua nova senha: ")
        usuario.alterar_senha(nova_senha)

    elif opcao == "5":
        usuario.ver_extrato()

    elif opcao == "6":
        print("Saindo... Obrigado por usar nosso banco!")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")