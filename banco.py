# Criar um sistema de banco com 3 opções - Saque - Deposito - Extrato
# O sistema só deve permitir 3 saques diários com limite máximo de 500 reais
# Os saques devem ser armazenados em uma variável e exibidos no extrato
# O estrato deve registrar todos os saques e depositos feitos na conta

print("""
    Selecione uma opção:
    
     1 - Saque
     2 - Deposito
     3 - Extrato
     4 - Sair
     
    Obrigado por ser nosso cliente!
""")
    

valor_conta = 0
limite_saque = 500.00
QUANTIDADE_SAQUE = 3
movimentacoes = []


while True:
    opcao = int(input("Digite a opção desejada: /n"))
    
    if opcao == 1:
        saque = float(input("Valor que deseja sacar:"))
        if saque <= limite_saque and QUANTIDADE_SAQUE > 0 and saque <= valor_conta and saque > 0:
            valor_conta -= saque
            print(f"Saque realizado com sucesso")
            QUANTIDADE_SAQUE -= 1
            movimentacoes.append(f"Saque: {saque:.2f}")
            
        elif saque > limite_saque: 
            print(f"O limite de saque é de R$ {limite_saque:.2f}, verifique o valor e tente novamente")
        
        elif QUANTIDADE_SAQUE == 0:
            print("Você atingiu o limite de saques diários")
            
        elif saque <= 0:
            print("Você não pode fazer saque de valor negativo")
            
        elif saque > valor_conta:
            print("Você não possui saldo suficiente")
            print(f"Seu saldo atual é de R$ {valor_conta:.2f}")
        
    
    elif opcao == 2:
        deposito = float(input("Valor que deseja depositar:"))
        if deposito > 0:
            valor_conta += deposito
            print(f"Depósito realizado com sucesso")
            movimentacoes.append(f"Depósito: {deposito:.2f}")
        else: 
            print("Valor digitado é negativo ou incorreto, tente novamente")   
        
    
    elif opcao == 3:
        if len(movimentacoes) > 0:
            for i in movimentacoes:
                print(i)
                
        else:
            print("Não foram realizadas movimentações")
        
        print("")
        print(f"Seu saldo atual é de R$ {valor_conta:.2f}")
        
    elif opcao == 4:
        print("Operação finalizada")
        break
    
    else:
        print("Opção inválida. Tente novamente")
        
