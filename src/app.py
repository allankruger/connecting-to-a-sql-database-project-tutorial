import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
print(connection_string)
engine = create_engine(connection_string).execution_options(autocommit=True)
engine.connect()

def execute_SQL_from_file(file_name):
    with engine.connect() as con:
        with open(f"./sql/{file_name}") as file:
            query = text(file.read())
            con.execute(query)

#Drop tables
execute_SQL_from_file("drop.sql")

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
execute_SQL_from_file("create.sql")

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
execute_SQL_from_file("insert.sql")

# 4) Use pandas to print one of the tables as dataframes using read_sql function
dataframe = pd.read_sql("Select * from authors;", engine)
print(dataframe.head())