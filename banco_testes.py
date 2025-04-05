# Separar as opções em funções e criar duas novas ( cadastrar usuário e cadastrar conta bancária)

# A função saque deve receber os argumentos apenas por nome. Sugestões de argumentos: saque, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato. Tipo saldo=saldo, numero_saques=numero_saques...and 
# Deposito deve receber os argumentos apenas por posição. Sugestão de arg: saldo, valor e extrato. Retorno, saldo e extrato.
# Extrato deve ser passado por posição e nomeados: posi: saldo, arg nomeados: extrato.
# Criar usuário, o programa deve armazenar usuários em uma lista, cada usuário deve ter: nome, data de nascimento, cpf e endereço (o endereço é uma string com o formato: logradoudo, numero, bairro - cidade/sigla do estado). Deve guardar apenas os números do cpf (sem simbolos). Não podemos cadastrar 2 usuários com o mesmo cpf. 
# Criar conta bancária, o programa deve armazenar as contas em uma lista, cada conta deve ter: numero da conta, agencia e cpf do usuário.O número da conta é sequencial e começa em 1. O número da agência é fixo: "0001". Não podemos cadastrar 2 contas com o mesmo número. Cada usuário pode ter mais de uma conta, mas a conta só pode ter um usuário.
# Para vincular um usuário a uma conta filtre a lista de usuários buscando o cpf informado para cada usuário da lista.

import datetime
import string

titulo = " Banco Duzz "
print("")
print(titulo.center(100, "="))
print("""
    Selecione uma opção:
    
    1 - Saque
    2 - Deposito
    3 - Extrato
    4 - Criar Usuário
    5 - Criar Conta Bancária
    6 - Sair
    
    Obrigado por ser nosso cliente!
""")
valor_em_conta = 50
limite = 500.00
quantidade_transações = 3
extrato = []
mascara = "%d/%m/%Y %H:%M:%S"
usuarios = []
contas_bancarias = []
numero_da_conta = 1

# FAZER SAQUE
def fazer_saque(*, saque, valor_em_conta, extrato, quantidade_transações):
    
    if saque <= 0:
        print("\nVocê não pode fazer saque de valor negativo")
        
    elif saque > valor_em_conta:
        print("\nVocê não possui saldo suficiente")
        print(f"\nSeu saldo atual é de R$ {valor_em_conta:.2f}")
        
    elif saque > limite: 
        print(f"\nO limite de saque é de R$ {limite:.2f}, verifique o valor e tente novamente")
    
    elif quantidade_transações <= 0:
        print("\nLimite de operações atingido! O limite de operações será redefinido após a 00:00h")
            
    else:
        valor_em_conta -= saque
        print(f"\nSaque realizado com sucesso")
        quantidade_transações -= 1
        data = datetime.datetime.now()
        extrato.append(f"Saque: R$ {saque:.2f}, data {data.strftime(mascara)}")

    return valor_em_conta, extrato, quantidade_transações

# FAZER DEPÓSITO
def fazer_deposito(deposito, valor_em_conta, extrato, quantidade_transações, /):
   
    if deposito > 0:
        valor_em_conta += deposito
        print(f"\nDepósito realizado com sucesso")
        data = datetime.datetime.now()
        extrato.append(f"Deposito: R$ {deposito:.2f} , data {data.strftime(mascara)}")
        quantidade_transações -= 1
    else: 
        print("\nValor digitado é negativo ou incorreto, tente novamente")
               
    return valor_em_conta, extrato, quantidade_transações

# EXIBIR EXTRATO
def exibir_extrato( valor_em_conta, /, *, extrato = extrato, ):
    
        if len(extrato) > 0:
            for i in extrato:
                print("")
                print(i)
                
        else:
            print("\nNão foram realizadas movimentações")
        
        print("")
        print(f"\nSeu saldo atual é de R$ {valor_em_conta:.2f}")

# CRIAR USUÁRIO        
def criar_usuarios(nome, data_nascimento, cpf, endereco, usuarios,):
    try:
        simbolos = string.digits
        mascara = "%d/%m/%Y"
        format_data_nascimento = datetime.datetime.strptime(data_nascimento, mascara)
        format_cpf = "".join([i for i in cpf if i in simbolos])
        
        for i in usuarios:
            if i["cpf"] == format_cpf:
                print("\nEsse usuário já tem cadastro!")
                return " "
            
        dados = {
            "nome": nome,
            "data_nascimento": format_data_nascimento.date(),
            "cpf": format_cpf,
            "endereço": endereco,
        }
        usuarios.append(dados)
        print("\nUsuário cadastrado com sucesso. Bem vindo ao banco Duzz!")
                
        return dados # retorna os usuários cadastratdos
        # return nome, data_nascimento, cpf, endereco - não tão uteis
    
    except ValueError:
        print("\nFormato de data ou cpf inválido")
        return ""

# CRIAR CONTA BANCÁRIA
def criar_conta_bancaria(cpf,usuarios,numero_da_conta):
    agencia = "0001"
    
    if cpf in usuarios["cpf"]:
        contas_bancarias.append({"Num_conta": numero_da_conta, "agencia": agencia, "cpf": cpf})
        print("\nConta criada com sucesso!")
    else:
        print("\nUsuário não encontrado!")
        
    numero_da_conta += 1
        

while quantidade_transações > 0:
    print("=" * 100)
    opcao = int(input("\nDigite a opção desejada: \n"))
    if opcao == 1:
        valor_saque = float(input("\nValor que deseja sacar:"))
        valor_em_conta, extrato, quantidade_transações = fazer_saque(saque = valor_saque, valor_em_conta = valor_em_conta, extrato = extrato, quantidade_transações = quantidade_transações)
    
    elif opcao == 2:
        valor_deposito = float(input("\nValor que deseja depositar:"))
        valor_em_conta, extrato, quantidade_transações = fazer_deposito(valor_deposito, valor_em_conta, extrato, quantidade_transações)
        
    elif opcao == 3:
        exibir_extrato(valor_em_conta, extrato = extrato)
        
    elif opcao == 4:
        
        print("\nCadastro de Usuário:")
        nome = input("Nome:").capitalize()
        data_nascimento = input("Data de nascimento: ")
        cpf = input("CPF: ")
        endereco = {"logradouro": input("logradouro: "), "numero": input("numero: "), "bairro": input("bairro: "), "cidade": input("cidade: "), "estado": input("estado: ")}
        
        novo_usuario = criar_usuarios(nome = nome, data_nascimento = data_nascimento, cpf = cpf, endereco = endereco, usuarios = usuarios)
        print(novo_usuario)
        
    elif opcao == 5:
        if len(usuarios) > 0:
            print("\nCadastro de Conta Bancária:")
            cpf = input("CPF do usuário: ")
            criar_conta_bancaria(cpf,usuarios,numero_da_conta)
        else:
            print("\nNenhum usuário cadastrado!")
    
    elif opcao == 6:
        print("\nOperação finalizada")
        break

    else:
        print("\nOpção inválida. Tente novamente")

        
else:
    print("\nLimite de operações atingido! O limite de operações será redefinido após às 00:00h")




# Criar conta bancária, o programa deve armazenar as contas em uma lista, cada conta deve ter: numero da conta, agencia e cpf do usuário.O número da conta é sequencial e começa em 1. O número da agência é fixo: "0001". Não podemos cadastrar 2 contas com o mesmo número. Cada usuário pode ter mais de uma conta, mas a conta só pode ter um usuário.
# Para vincular um usuário a uma conta filtre a lista de usuários buscando o cpf informado para cada usuário da lista.




