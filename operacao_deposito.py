menu = """
=================== MENU ===================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
=============== FIM MENU ===================
    
    
=> """

saldo = 0
lim_saque = 500
extto = ""
num_saques = 0
NUM_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("valor do depósito: "))

        if valor > 0:
            saldo += valor
            extto += f"Depósitado: R$ {valor:.2f}\n"

        else:
            print("Operação inválida! Valor inválida.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excd_saldo = valor > saldo

        excd_limite = valor > lim_saque

        excd_saques = num_saques >= NUM_SAQUE

        if excd_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excd_limite:
            print("Operação falhou! O saque excedeu o limite.")
        
        elif excd_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extto += f"saque: R$ {valor:.2f}\n"
            num_saques += 1
            
        else:
            print("Operação inválida! Valor inválida.")
            
    elif opcao == "e":
        print("\n================= EXTRATO =================")
        print("Não foram realizadas movimentações." if not extto else extto)
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("\n============= FIM EXTRATO =================")
        
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, selecione a operação desejada.")
        
