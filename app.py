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

async def capturar_produto_savegnago(url_base, seletor_busca, termo_busca, prefixo_arquivo_print):
    """
    Acessa o site, busca o produto, rola a tela e tira múltiplos prints em alta resolução.
    Retorna uma lista com os caminhos dos arquivos gerados.
    """
    arquivos_gerados = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        
        # Mantendo a configuração HD que conversamos!
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2
        )
        page = await context.new_page()
        
        print(f"\nAcessando: {url_base}")
        await page.goto(url_base, wait_until="networkidle", timeout=60000)
        
        print("Aguardando o campo de busca...")
        await page.wait_for_selector(seletor_busca, timeout=15000)
        
        print(f"Pesquisando por: '{termo_busca}'")
        await page.fill(seletor_busca, termo_busca)
        await page.press(seletor_busca, "Enter")
        
        # Aguarda os primeiros resultados aparecerem
        await page.wait_for_timeout(5000) 

        print("Tirando prints em partes...")
        quantidade_de_rolagens = 3
        
        for i in range(quantidade_de_rolagens):
            # Cria nomes como "resultado_savegnago_1.png", "resultado_savegnago_2.png"
            nome_arquivo = f"{prefixo_arquivo_print}_{i+1}.png"
            
            # Tira o print do que está visível
            await page.screenshot(path=nome_arquivo, full_page=False)
            print(f"Sucesso! Print {i+1} salvo como: {nome_arquivo}")
            
            # Guarda o nome do arquivo na nossa lista para enviar depois
            arquivos_gerados.append(nome_arquivo)
            
            # Rola a página para baixo para o próximo print e aguarda carregar
            await page.keyboard.press("PageDown")
            await page.wait_for_timeout(2000) 
            
        await browser.close()
        
        return arquivos_gerados


        
