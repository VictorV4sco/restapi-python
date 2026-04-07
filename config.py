import os
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis do arquivo .env

class Config:
    # Formato: mysql+pymysql://usuario:senha@host:porta/nome_do_banco
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
