## Códigos feitos por Zac Milioli https://www.linkedin.com/in/zac-milioli

## Descomentar para instalar bibliotecas necessárias 
# import os
# os.system('pip install pandas')
# os.system('pip install numpy')

from glob import glob
import pandas as pd
import numpy as np

separators = '- '*30
path_principal = 'principal/*.xlsx'
path_retiradas = 'retiradas/*.xlsx'

df_principal_em_path = glob(path_principal)[0]
glob_retiradas = glob(path_retiradas)

df_principal = pd.read_excel(df_principal_em_path)

for retirada in glob_retiradas:
    remover = pd.read_excel(retirada)
    print(separators)
    print(f"\n\tLeu {retirada}\n")
    if 'Tombo' in remover.columns:
        print("\n\tEste dataframe possui tombos, verificando cada um...\n")
        for tombo in remover['Tombo']:
            if tombo != np.nan:
                print(f"- Verificando existência de {tombo} na planilha principal", end='\r')
                df_principal.loc[df_principal['Tombo'] == tombo] = np.nan
    else:
        print(f'\n\tA planilha {retirada} não possui tombos, será ignorada')

print(separators)
df_principal.dropna(axis=0, inplace=True)
df_principal.to_excel(df_principal_em_path, na_rep='')
print(f"\n- Arquivo {df_principal_em_path} atualizado\n")
print(separators)
