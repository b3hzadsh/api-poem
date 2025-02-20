import databases
import sqlalchemy

# Define the database path
db_path = "sqlite:///assets/khayam__.sqlite3"

# Reflect the existing database schema
engine = sqlalchemy.create_engine(db_path, connect_args={"check_same_thread": False})
metadata = sqlalchemy.MetaData()

# Reflect the existing tables from the database
metadata.reflect(bind=engine)

# Access the existing tables using their names
poems_table = metadata.tables["poem"]
verses_table = metadata.tables["verse"]

# Initialize the database connection
database = databases.Database(db_path, force_rollback=False)

# Example IDs for querying or other operations
min_poem_id = 1119
max_poem_id = 1296
