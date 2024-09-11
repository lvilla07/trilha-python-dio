
menu = """\n
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def depositar(vlr_deposito):
    global saldo
    global extrato
    if vlr_deposito > 0:
        saldo += vlr_deposito
        extrato += f"Depósito:\t\tR$ {vlr_deposito:.2f}\n"
        print(f"Depósito no valor de {vlr_deposito:.2f} realizado com sucesso!")
    else:
        print("O valor inserido é negativo ou inválido !")


def sacar(vlr_saque):
    global saldo
    global numero_saques
    global extrato
    if vlr_saque > saldo:
        print(f"O seu saldo é de R$ {saldo:.2f} portanto não é possível sacar o valor de R$ {vlr_saque:.2f} pois é maior que seu saldo atual")
    elif vlr_saque > 500:
        print("O limite de saque permitido é de R$ 500.00")
    elif numero_saques >= LIMITE_SAQUES:
        print("Foi excedido o número máximo de saques por dia que são 3, por favor tente amanhã !")
    elif vlr_saque > 0:
        saldo -= vlr_saque
        numero_saques += 1
        extrato += f"Saque:\t\tR$ {vlr_saque:.2f}\n"
        print(f"Saque no valor de {vlr_saque:.2f} realizado com sucesso!")
    else:
        print(f"Fluxo de saque falhou, valor inválido")


def mostra_extrato():
    global saldo
    global extrato
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

while True:
    
    opcao = input(menu)

    if opcao == "d":
        vlr_deposito = float(input("Qual valor deseja depositar ? "))
        depositar(vlr_deposito)
    elif opcao == "s":
        vlr_saque = float(input("Qual valor deseja sacar ? "))
        sacar(vlr_saque)
    elif opcao == "e":
        mostra_extrato()
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
