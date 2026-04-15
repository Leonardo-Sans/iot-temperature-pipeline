import pandas as pd
from sqlalchemy import create_engine

# conexão com postgres
engine = create_engine(
    "postgresql://iotuser:123456@localhost:5432/iotdb"
)

print("Carregando dataset...")

df = pd.read_csv("../data/temperature_readings.csv")

print("Inserindo dados no banco...")

df.to_sql(
    "temperature_readings",
    engine,
    if_exists="replace",
    index=False
)

print("Dados inseridos com sucesso!")