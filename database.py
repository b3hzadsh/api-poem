import databases
import sqlalchemy

metadata = sqlalchemy.MetaData()
db_path = "sqlite:///assets/khayam__.sqlite3"

poems_table: sqlalchemy.Table = sqlalchemy.Table(
    "poem",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("cat_id", sqlalchemy.Integer),
    sqlalchemy.Column("title", sqlalchemy.String),
)
verses_table: sqlalchemy.Table = sqlalchemy.Table(
    "verse",
    metadata,
    # sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("position", sqlalchemy.Integer),
    sqlalchemy.Column("vorder", sqlalchemy.Integer),
    sqlalchemy.Column("poem_id", sqlalchemy.ForeignKey("poem.id"), nullable=False),
)

engine = sqlalchemy.create_engine(db_path, connect_args={"check_same_thread": False})  # todo may need True
metadata.create_all(engine)
database: databases.Database = databases.Database(db_path, force_rollback=False)

min_poem_id = 1119
max_poem_id = 1296
