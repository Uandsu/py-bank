menu = """====Bem vindo ao Banco Hoje!======
Por gentileza selecione sua opção:

[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair
=>   """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Infome o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}"

        else:
            print("Operação falhou: o Valor informado é invalido")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saque = valor > LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Opção falhou!Você não possui saldo suficiente")
            
        elif excedeu_limite:
            print("Opção falhou!Valor do saque ultrapassa o limite ")
            
        elif excedeu_saque:
            print("Opção falhou!Número de saque excedido")
            
        elif valor > 0:
            saldo -= valor #aqui no caso quando sacar diminuir valor da conta
            extrato += f"saque: R$ {valor:.2f}\n" #registrar no extrato.
            numero_saque += 1
            
        else:
            print("Operação falhou!O valor informado é invalido")
            
    elif opcao == "e" :
        print("\n==========EXTRATO=========")
        print("Não foram realizado movimentações." if not extrato else extrato)#verifica se extrato está vazio ou não.
        print(f"Saldo: R$ {saldo:.2f}")
        print("============================")
        
    elif opcao == "q":
        print("Obrigado!")
        break      
            
    else:
        print("Opção inválida , por favor selecione novamente a operação desejada")