## Códigos feitos por Zac Milioli https://www.linkedin.com/in/zac-milioli

## Descomentar para instalar bibliotecas necessárias 
# import os
# os.system('pip install pandas')
# os.system('pip install xlrd')
# os.system('pip install openpyxl')

from glob import glob
import pandas as pd
from datetime import datetime

separators = '- '*50
path_principal = 'principal/*.xlsx'
path_retiradas = 'retiradas/*.xl*'

df_principal_em_path = glob(path_principal)[0]
glob_retiradas = glob(path_retiradas)

print(separators)
print(f"\n\tEncontrada planilha principal {df_principal_em_path}\n")
print(f"\n\tEncontradas planilhas de retirada em\n{glob_retiradas}\n")
print(separators)

df_principal = pd.read_excel(df_principal_em_path)

for retirada in glob_retiradas:
    if 'biblioSaida' in retirada:
        print(separators)
        print("\n\tEncontrou arquivo biblioSaida, verificando sheet Total Doados\n")
        remover = pd.read_excel(retirada, sheet_name='Total Doados')
        remover.dropna(subset='Tombo', inplace=True)
        print(f"\n\tLeu {retirada}\n")
        print("\n\tTombos em comum com a planilha principal:\n")
        print(df_principal[df_principal['Tombo'].isin(remover['Tombo'])])
        df_principal = df_principal[df_principal['Tombo'].isin(remover['Tombo'])]
        print("\n\tRemoveu os tombos em comum\n")
    else:
        remover = pd.read_excel(retirada)
        print(separators)
        print(f"\n\tLeu {retirada}\n")
        if 'Tombo' in remover.columns:
            print("\n\tEsta planilha possui tombos\n")
            remover.dropna(subset='Tombo', inplace=True)
            print("\n\tTombos em comum com a planilha principal:\n")
            print(df_principal[df_principal['Tombo'].isin(remover['Tombo'])])
            df_principal = df_principal[~df_principal['Tombo'].isin(remover['Tombo'])]
            print("\n\tRemoveu os tombos em comum\n")
        else:
            print(f'\n\tEsta planilha não possui tombos, será ignorada\n')

print(separators)
df_principal.to_excel(f'output/biblio_{datetime.now().strftime("%d%m%Y")}.xlsx', sheet_name='Todos Livros')
print(f"\n- Planilha nova criada\n")
print(separators)
