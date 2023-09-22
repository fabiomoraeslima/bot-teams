import pandas as pd
from functions import conexoes, sendmessage

pathsql = 'sql/sql_sku_deca.sql'


# Abre o arquivo com a querie
file = open(pathsql)
sql = file.read()
file.close()

# Abre a conexao com o banco
conn = conexoes.con_bdfabio()

# Executa a querie usando o pandas
df_result = pd.read_sql_query(sql, conn)

# Itera o Dataframe pandas para testar todas as linhas
for i in range(len(df_result)):

    if (str(df_result['status'].iloc[i])) == '0':
        print(str(df_result.iloc[i]))
        print()


# sendmessage.send_message('Mariana Muller')