##----------------------------------------------------------------------##------------------------------------------------##
import cx_Oracle
import csv
import os
from datetime import datetime

# Conectar ao banco de dados Oracle
conn = cx_Oracle.connect(user='user_default', password='pw_default', dsn='PRD')

# Criar um cursor
cursor = conn.cursor()

# Data inicial e final que você deseja na consulta
data_inicio = '01/01/2024'
data_fim = '10/01/2024'
data_inicio_n = '01-01-2024'
data_fim_n = '10-01-2024'

# Converter as datas para o formato desejado na consulta
data_inicio_formatada = datetime.strptime(data_inicio, '%d/%m/%Y').strftime('%d/%m/%Y')
data_fim_formatada = datetime.strptime(data_fim, '%d/%m/%Y').strftime('%d/%m/%Y')

# Sua consulta SQL
query = '''
SELECT A.CD_ATENDIMENTO AS ATENDIMENTO,
    to_char(A.HR_ATENDIMENTO , 'dd/mm/yyyy HH24:MI:SS' ) DATA_ATENDIMENTO,
    Decode(A.tp_atendimento, 'I','INTERNAÇÃO', 'E', 'EXTERNO','U', 'URGÊNCIA', 'A', 'AMBULATORIO') AS TIPO_ATENDIMENTO,
FROM ATENDIME A
WHERE TRUNC(A.DT_ATENDIMENTO) BETWEEN 
to_date(:data_inicio,'dd/mm/yyyy') AND 
to_date(:data_fim,'dd/mm/yyyy')
ORDER BY A.CD_ATENDIMENTO, A.HR_ATENDIMENTO
'''

parametros = {'data_inicio': data_inicio_formatada, 'data_fim': data_fim_formatada}

# Executar a consulta
cursor.execute(query,parametros)

# Obter os resultados
resultados = cursor.fetchall()

# Nome do arquivo CSV de saída
nome_arquivo = f'Extração_Mensal_{data_inicio_n}_a_{data_fim_n}.csv'

# Caminho completo para a pasta onde o arquivo será salvo
pasta_especifica = 'C:/Users/ronanDocuments'

# Caminho completo para o arquivo CSV
caminho_arquivo = os.path.join(pasta_especifica, nome_arquivo)

# Escrever os resultados em um arquivo CSV na pasta específica
with open(caminho_arquivo, 'w', newline='') as arquivo_csv:
    csv_writer = csv.writer(arquivo_csv, delimiter=';') ##Por usar excel usa o delimitador ";"
    # Escrever o cabeçalho (nome das colunas)
    csv_writer.writerow([i[0] for i in cursor.description])
    # Escrever os dados
    dados_formatados = [[str(valor).replace('.', ',') if isinstance(valor, (int, float)) else valor for valor in linha]
        for linha in resultados]
    csv_writer.writerows(dados_formatados)

# Fechar o cursor e a conexão
cursor.close()
conn.close()

print(f'Arquivo CSV salvo em: {caminho_arquivo}')