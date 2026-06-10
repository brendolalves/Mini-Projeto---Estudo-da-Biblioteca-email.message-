import os
import asyncio
import smtplib
import mimetypes
from datetime import datetime
from email.message import EmailMessage
from playwright.async_api import async_playwright
from dotenv import load_dotenv
import requests

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')

hoje = datetime.now()
data = hoje.strftime("%d/%m/%Y")

class Folheto:
    def __init__(self):
        self.savegnago_url = "https://imagens.savegnagoonline.com.br/jornal-semanal-app/Rio_Claro.pdf"

    def baixar_folheto(self, nome_arquivo="ofertas.pdf"):
        try:
            res = requests.get(self.savegnago_url, headers={'User-Agent': 'Mozilla/5.0'})
            if res.status_code == 200:
                with open(nome_arquivo, "wb") as f:
                    f.write(res.content)
                return True
            return False
        except Exception as e:
            print(f"Erro ao baixar o PDF: {e}")
            return False
        
