import sys

print("Bem vindo ao simulador de investimentos!")
print("---------------INSTRUÇÕES---------------")
print("----------------------------------------")

print("Você informará os seguintes elementos: \n1 - O valor do investimento inicial \n2 - O valor do aporte mensal \n3 - Quanto tempo você pretende investir mensalmente \n4 - Qual a taxa de rendimento mensal esperada")

resp = str(input("Digite qualquer letra para dar continuidade ou 'f' para finalizarmos :\n "))

if resp == "f":
    print("Obrigao pela visita, volte sempre!")
    sys.exit()
    
print("---------------------------")
print("Vamos continuar o processo!")
print("---------------------------")

aporteInicial = float(input("Digite o valor do primeiro aporte, o valor inicial: R$ "))
while aporteInicial < 0:    
    print("O aporte inicial não pode ser menor igual a 0. \n")
    aporteInicial = float(input("Por favor digite um valor válido: "))   
print("----------------------------------------------------------------------")
aporteMensal = float(input("Digite o valor de investimento mensal: R$ "))
while aporteMensal < 0:    
    print("O aporte mensal não pode ser menor que 0. \n")
    aporteMensal = float(input("Por favor digite um valor válido: "))   
print("----------------------------------------------------------------------")
taxa = float(input("Digite o valor da taxa mensal: "))
taxaMensal = float(taxa/100)   
while taxa < 0:    
    print("A taxa não pode ser menor que 0. \n")
    taxa = float(input("Por favor digite um número válido: "))
    taxaMensal = float(taxa/100)   
    
print("----------------------------------------------------------------------")
meses = int(input("Digite por quantos meses você pretende investir: "))
while meses < 0:    
    print("Os meses não podem ser menor que 0. \n")
    meses = int(input("Por favor digite um tempo de meses válido: "))   
print("----------------------------------------------------------------------")

montanteFinal: float

if meses == 0:
    aporteTotal = aporteInicial
    montanteFinal = aporteInicial
elif taxaMensal == 0:
    aporteTotal =  aporteInicial + aporteMensal * (meses-1)
    montanteFinal = aporteTotal
else:
    aporteTotal = aporteInicial + aporteMensal * (meses - 1)
    montanteFinal = aporteInicial * ((1 + taxaMensal)**meses) + aporteMensal * ((((1+taxaMensal)**(meses - 1)) - 1)/taxaMensal) * (1+ taxaMensal)
    

print("------------RELATÓRIO DE INVESTIMENTO------------")
print("status---------------------------------Concluída \n\n")
print("--------------Informações Iniciais-------------- \n")
print(f"Aporte Inicial--------------------R$ {aporteInicial:.2f}")
print(f"Aporte Mensal---------------------R$ {aporteMensal:.2f}")
print(f"Total de meses------------------------------ {meses}")
print("---------------------------------------------------- \n")
print("--------------INFORMAÇÕES FINAIS-------------- \n")
print("--------------Juros por mês-------------- \n")

if meses > 0:
    valorInvestido = float(aporteInicial)
    jurosGerado = float(aporteInicial * taxaMensal)
    saldoFimMes = float(aporteInicial + jurosGerado)
    jurosAcumuladoMensalmente = float(jurosGerado) #Juros do aporte inicial
    print(f"Saldo do fim do 1° mês: R$ {saldoFimMes:.2f} \nJuros gerado no primeiro mês: R$ {jurosGerado:.2f} ")
    print(f"-----------------------------------------------------")
    for i in range(2, meses + 1):
        valorInvestido = float(valorInvestido + aporteMensal)
        saldoFimMes = saldoFimMes + aporteMensal  #saldo sem juros do mês
        jurosGerado = saldoFimMes * taxaMensal
        jurosAcumuladoMensalmente = jurosAcumuladoMensalmente + jurosGerado #Soma o valor do jurosAcumalo + o jurosGerado no Mês
        saldoFimMes = saldoFimMes + jurosGerado
        print(f"Saldo do fim do {i}° mês: R$ {saldoFimMes:.2f} \nJuros gerado no {i}° mês: R$ {jurosGerado:.2f} \nValor investido até agora: {valorInvestido:.2f}")
        print(f"-----------------------------------------------------")
        
else:
    jurosAcumuladoMensalmente = 0.0
    print("Nenhum mês decorrido para gerar juros.")
    print("-----------------------------------------------------")
    
print(f"Juros totais acumulados: R$ {jurosAcumuladoMensalmente:.2f}")    
print(f"-----------------------------------------------------")    
print(f"Aporte Total---------------------R$ {aporteTotal:.2f}")
print("+")
JurosTotais = float(montanteFinal - aporteTotal)
print(f"Juros Totais--------------------R$ {JurosTotais:.2f}")
print("=")
print(f"Montante Final--------------------R$ {montanteFinal:.2f}")
      
    