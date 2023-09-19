import pandas as pd
from db import engine, metadata

data = pd.read_csv('data.csv', delimiter=';')

data['код'].ffill(inplace=True)
data['проект'].ffill(inplace=True)

data_grouped = data.groupby(['код', 'проект']).sum().reset_index()
data_transposed = data_grouped.melt(id_vars=['код', 'проект'], var_name='год', value_name='значение')

metadata.create_all(engine)

data_transposed.to_sql('data', engine, if_exists='replace', index=False)

sql_query = "SELECT код, проект, год, значение FROM data"

df = pd.read_sql_query(sql_query, engine)

df['значение'] = pd.to_numeric(df['значение'], errors='coerce')

df['проект'] = df['код'].str.split('.').str[0]
df['подпроект'] = df['код'].str.split('.').str[1]

aggregated_project_df = df.groupby(['год', 'проект'])['значение'].sum().reset_index()
df['подпроект'] = df['проект'] + '.' + df['подпроект']
aggregated_subproject_df = df.groupby(['год', 'подпроект'])['значение'].sum().reset_index()

print("Сумма по проектам:")
print(aggregated_project_df)

print("\nСумма по подпроектам:")
print(aggregated_subproject_df)
