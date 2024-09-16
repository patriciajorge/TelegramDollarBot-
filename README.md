# TelegramDollarBot-
um bot em Python que monitora a cotação do dólar e envia alertas via Telegram quando o valor cai abaixo de um limite definido. Utiliza a API da AwesomeAPI para cotações e a Telegram Bot API para notificações. 

# Recursos
- Monitora a cotação do dólar utilizando a API da AwesomeAPI.
- Envia notificações e imagens via Telegram usando a Telegram Bot API.
- Configuração segura de tokens utilizando variáveis de ambiente com python-dotenv.

# Como Funciona
- Monitoramento de Cotação: O bot consulta a cotação do dólar a cada 30 segundos.
- Envio de Alertas: Quando a cotação cai abaixo de um valor específico, o bot envia uma mensagem e imagem para um chat do Telegram.
- Segurança: Tokens e variáveis de ambiente são gerenciados com python-dotenv.

# Pré-requisitos
- Python 3.6 ou superior
- Biblioteca requests
- Biblioteca rich
- Biblioteca python-dotenv

# Configuração
- Instale as dependências:

```bash
pip install -r requirements.txt
```

- Configure as variáveis de ambiente: Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
```bash
TELEGRAM_BOT_TOKEN=seu_token_aqui
```

# Uso
Execute o bot:
```bash
python app.py
```

# Notas:
O bot enviará alertas quando a cotação do dólar estiver abaixo do limite especificado no código.
