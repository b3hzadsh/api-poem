import databases
from sqlalchemy import MetaData, Table, create_engine

db_path = "sqlite:///assets/khayam__.sqlite3"
# Create the engine
engine = create_engine(db_path)

# Reflect the tables
metadata = MetaData()
metadata.reflect(bind=engine)

# Access a table
poems_table = metadata.tables["poem"]  # Replace 'my_table_name' with your table name
verses_table = metadata.tables["verse"]  # Replace 'my_table_name' with your table name

engine = create_engine(db_path, connect_args={"check_same_thread": True})  # todo may need True
metadata.create_all(engine)
database: databases.Database = databases.Database(db_path, force_rollback=True)

min_poem_id = 1119
max_poem_id = 1296
