## Códigos feitos por Zac Milioli https://www.linkedin.com/in/zac-milioli

## Descomentar para instalar bibliotecas necessárias 
# import os
# os.system('pip install pandas')
# os.system('pip install xlrd')

from glob import glob
import pandas as pd
import numpy as np
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

df_principal = pd.read_excel(df_principal_em_path, sheet_name='Todos Livros')

for retirada in glob_retiradas:
    if 'biblioSaida' in retirada:
        print(separators)
        print("\n\tEncontrou arquivo biblioSaida, ignorando...\n")
    else:
        remover = pd.read_excel(retirada)
        remover.dropna(inplace=True)
        print(separators)
        print(f"\n\tLeu {retirada}\n")
        if 'Tombo' in remover.columns:
            print("\n\tEsta planilha possui tombos\n")
            df_principal = df_principal[~df_principal['Tombo'].isin(remover['Tombo'])]
        else:
            print(f'\n\tEsta planilha não possui tombos, será ignorada\n')

print(separators)
df_principal.to_excel(f'output/biblio_{datetime.now().strftime("%d%m%Y")}.xlsx', sheet_name='Todos Livros')
print(f"\n- Planilha atualizada\n")
print(separators)
