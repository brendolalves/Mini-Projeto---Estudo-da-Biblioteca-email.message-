# **Sistema de Busca Automática e Alerta por E-mail** 

Este repositório foi criado com o objetivo de estudar e aplicar a biblioteca padrão do Python email.message (especificamente a classe EmailMessage), integrando-as com técnicas de busca online para automatizar o envio de informações relevantes — como ofertas, rastreamento de documentos ou atualizações importantes — diretamente para o e-mail de usuários cadastrados.


## Objetivo do Projeto

O sistema funciona em três etapas principais:

1. **Busca Online (Scraping/API):** Monitora e coleta informações específicas na web (ex: uma queda de preço ou a atualização de um documento regulatório).  
2. **Processamento:** Identifica se a informação atende aos critérios definidos para o disparo.  
3. **Notificação:** Constrói e envia um e-mail formatado (em texto plano ou HTML) de forma automatizada utilizando o protocolo SMTP e o módulo email.message.

## Tecnologias e Ferramentas

* **Linguagem:** Python 3.x  
* **Módulos Nativos:**  
  * [email.message](https://docs.python.org/3/library/email.message.html) \- Para a construção estruturada das mensagens de e-mail.  
  * smtplib \- Para a comunicação com o servidor SMTP e envio do e-mail.  
* **Bibliotecas Externas:**  
  * requests / BeautifulSoup4 (para Web Scraping ou consumo de APIs).  
  * python-dotenv (para gerenciamento seguro de credenciais e variáveis de ambiente).

## Foco do Estudo: email.message.EmailMessage

A escolha da API moderna EmailMessage permite manipular e-mails como objetos Python de forma muito mais intuitiva. Os principais conceitos explorados neste estudo são:

* **Gerenciamento de Cabeçalhos (Headers):** Definição dinâmica de Subject, From e To.  
* **Conteúdo Avançado:** Configuração de corpos de e-mail em formato HTML para notificações mais visuais (set\_content e add\_alternative).  
* **Anexos:** Manipulação e inclusão automatizada de arquivos usando add\_attachment.

## Como Executar o Projeto

### **1\. Pré-requisitos e Ambiente Virtual**

Certifique-se de ter o Python 3 instalado em sua máquina. É altamente recomendável utilizar um ambiente virtual (venv) para isolar as dependências do projeto.  
`# Criar o ambiente virtual local`  
`python -m venv venv`

`# Ativar o ambiente virtual:`  
`# No Linux/macOS:`  
`source venv/bin/activate`  
`# No Windows (Prompt de Comando):`  
`.\venv\Scripts\activate`  
`# No Windows (PowerShell):`  
`.\venv\Scripts\Activate.ps1`

### **2\. Configuração das Variáveis de Ambiente**

Para mitigar riscos de segurança e evitar a exposição inadvertida de credenciais privadas em repositórios públicos, a aplicação utiliza uma arquitetura baseada em arquivos de configuração externa (.env). Crie um arquivo chamado .env na raiz do seu projeto e preencha conforme o modelo abaixo:

| Variável | Descrição | Exemplo / Valor Sugerido |
| :---- | :---- | :---- |
| EMAIL\_REMETENTE | Endereço de e-mail de origem responsável pelo envio das notificações. | seu\_email@gmail.com |
| EMAIL\_SENHA | Senha de aplicativo gerada exclusivamente para acesso SMTP. | abcd efgh ijkl mnop |
| SMTP\_SERVER | Endereço do servidor SMTP do seu provedor. | smtp.gmail.com |
| SMTP\_PORT | Porta de conexão segura para criptografia de dados (SSL/TLS). | 465 (SSL) ou 587 (TLS) |

*Nota Importante:* Caso utilize provedores modernos como o Gmail, senhas de login padrão serão bloqueadas. É mandatório ativar a "Verificação em duas etapas" em sua Conta Google e gerar uma **Senha de Aplicativo** específica para o script.

### **3\. Instalação e Inicialização**

Com o terminal devidamente indexado ao ambiente isolado (exibindo o prefixo (venv)), proceda com a atualização de pacotes e inicialização:  
`# Atualização recomendada do gerenciador de pacotes nativo`  
`python -m pip install --upgrade pip`

`# Instalação em lote das dependências listadas no projeto`  
`pip install -r requirements.txt`

`# Execução do módulo central do sistema`  
`python main.py`


## Funcionalidades Planejadas / Roadmap

O fluxo de engenharia do software foi mapeado de forma incremental, garantindo testes isolados de integridade para cada subsistema.

* **Fase 1: Motor de Scraping e Extração Online**  
  * Implementação de requisições HTTP seguras com a biblioteca requests.  
  * Mapeamento estrutural de seletores HTML utilizando BeautifulSoup4 para filtragem de ofertas e documentos históricos ou comerciais.  
* **Fase 2: Estruturação do Objeto de Mensagem**  
  * Migração e uso exclusivo da classe moderna email.message.EmailMessage para manipulação semântica de cabeçalhos.  
  * Padronização de codificação de texto em UTF-8.  
* **Fase 3: Visualização Rica e Templates Alternativos**  
  * Construção de templates de e-mail dinâmicos renderizados em HTML estruturado.  
  * Configuração de fallback para formato texto-plano através do método add\_alternative.  
* **Fase 4: Cadastro e Persistência de Dados**  
  * Desenvolvimento de camada de dados simples (JSON ou SQLite) para o registro indexado de múltiplos destinatários e termos-chave de busca.  
* **Fase 5: Orquestração e Agendamento Automatizado**  
  * Implementação de um loop de verificação contínuo utilizando rotinas do pacote schedule ou vinculação a utilitários de sistema (Cron Jobs / Task Scheduler).
