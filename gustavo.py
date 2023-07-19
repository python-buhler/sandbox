# Constantes
LOCAL_FILE = 'credito.py'
ID_VENDEDOR = 'id_vendedor'
VALOR_EMPRESTIMO = 'valor_emprestimos'
QUANTIDADE_EMPRESTIMO = 'quantidade_emprestimos'
DATA ='data'


# Variáveis
credito = '''id_vendedor,valor_emprestimos,quantidade_emprestimos,data
104271,448.0,1,20161208
21476,826.7,3,20161208
87440,313.6,3,20161208
15980,-8008.0,6,20161208
215906,2212.0,5,20161208
33696,2771.3,2,20161208
33893,2240.0,3,20161208
214946,-4151.0,18,20161208
123974,2021.95,2,20161208
225870,4039.0,2,20161208'''

# PASSO 1. CRIAR ARQUIVO FÍSICO
print("1. Escrita de dados em arquivo CSV - comma separated values \n")

with open (LOCAL_FILE , mode='w') as file :
    file.write(credito)

# PASSO 2. LER O ARQUIVO FÍSICO
print("2. Leitura de dados em arquivo CSV - comma separated values \n")

with open (LOCAL_FILE , mode='r', encoding='utf8' ) as conteudo :
    emprestimos = []

    linha = conteudo.readline()
    
    linha = conteudo.readline()
    while linha:

            linha_elementos = linha.strip().split(sep=',')
            
            linha_emprestimo = {}
            linha_emprestimo[ID_VENDEDOR] = linha_elementos[0]
            linha_emprestimo[VALOR_EMPRESTIMO] = linha_elementos[1]
            linha_emprestimo[QUANTIDADE_EMPRESTIMO] = linha_elementos[2]
            linha_emprestimo[DATA] = linha_elementos[3]

            emprestimos.append(linha_emprestimo)
            
            linha = conteudo.readline()

for linha_emprestimo in emprestimos:
  print(linha_emprestimo)

print('\n') # caracter não imprimível - quebra de linha

# PASSO 3. USAR A FUNÇÃO MAP PARA CRIAR UMA LISTA COM OS VALORES DOS EMPRÉSTIMOS TRANSFORMADOS EM FLOAT
print("3. Uso da função Map \n")

valores_emprestimos_lista = []

lista_valores_float = list(map(lambda x: { float(x[VALOR_EMPRESTIMO]) }, emprestimos ))

for valor in lista_valores_float:
    print(valor)

print('\n') # caracter não imprimível - quebra de linha