import textwrap

def menu():
    menu = """\n
    =================== MENU ===================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar conta
    [nu]\tNovo usuário
    [q]\tSair
    =============== FIM MENU ===================
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósitado:\tR$ {valor:.2f}\n"
        print("\nDepósito realizado  com sucesso!")
    else:
        print("\n Operação inválida, valor inválido")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, lim__saques):

    excd_saldo = valor > saldo
    excd_limite = valor > limite
    excd_saques = numero_saques >= lim__saques

    if excd_saldo:
        print("Operação inválida! Saldo suficiente.")
        
    elif excd_limite:
        print("Operação inválida! Excedeu o limite do saque.")
        
    elif excd_saques:
        print("Operação inválida! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"saque:\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nOperação realizada com sucesso!")
    else:
        print("Operação inválida! Valor inválida.")
        
    return saldo, extrato

def imprimir_extrato(saldo, /, *, extrato):

    print("\n================= EXTRATO =================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}\n")
    print("\n============= FIM EXTRATO =================")
        
    
    
    return

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o número de cpf: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso")
        return {"Agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado")

def listar_conta(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['Agência']}
            C/c:\t\t{conta['Número_conta']}
            Titular:\t{conta['Usuário']['nome']}
        """
        print("=" *100)
        print(textwrap.dedent(linha))

def novo_usuario(usuarios):
    cpf = input("Informe o número do CPF (apenas números são válidos): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if(usuario):
        print("cpf já cadastrado")
        return

    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço(logradouro/bairro/cidade-estado): ")
    
    usuarios.append({"nome": nome, "data nascimento": data_nascimento, "endereço": endereco})
    
    print("Usuário cadastrado com sucesso")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def banco():
    
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    num_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("valor do saque: "))
            saldo, extrato = sacar(
                    saldo = saldo,
                    valor = valor,
                    extrato = extrato,
                    limite = limite,
                    numero_saques=num_saques,
                    lim__saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            imprimir_extrato(saldo, extrato = extrato)
            
        elif opcao == "nu":
            novo_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_conta(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, selecione a operação desejada.")

banco()