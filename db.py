from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table, text, Inspector, inspect

db_params = {
    'user': 'test',
    'password': 'test',
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres'
}


engine = create_engine(
    f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}")

metadata = MetaData()
table_name = 'data'
inspector = inspect(engine)

if table_name in inspector.get_table_names():
    with engine.connect() as connection:
        drop_table_query = text(f"DROP TABLE {table_name};")
        connection.execute(drop_table_query)

data_table = Table(
    table_name,
    metadata,
    Column('id', Integer, primary_key=True),
    Column('код', String(255)),
    Column('проект', String(255)),
    Column('год', Integer),
    Column('значение', Float)
)
