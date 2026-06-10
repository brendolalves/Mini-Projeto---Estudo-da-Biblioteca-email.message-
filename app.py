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