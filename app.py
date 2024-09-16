import requests
from rich import print
from datetime import datetime
from time import sleep
import os
from dotenv import load_dotenv
# de 30 em 30 segundos, verificar o preço do dolar(em relação ao real) 
# e se o dolar estiver abaixo de um valor, enviar um sinal, caso contrário fazer nada
# https://economia.awesomeapi.com.br/json/last/USD-BRL

load_dotenv()
def enviar_fotos(chat_id, links_imagens, caption):
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    for link in links_imagens:
        try:
            requests.get(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo={link}&caption={caption}')
        except requests.exceptions.RequestException as e:
            print(f'Erro ao enviar imagem: {e}')
        sleep(2)

def verificar_cotacao():
    try:
        resultado = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL', timeout=10)
        resultado.raise_for_status()
        cotacao = float(resultado.json()['USDBRL']['ask'])
        data_atual = datetime.today().strftime('%d/%m/%Y - %H:%M')
        return cotacao, data_atual
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar cotação: {e}")
        return None, None

def main():
    while True:
        cotacao_atual, data_atual = verificar_cotacao()
        
        if cotacao_atual and cotacao_atual <= 5.777:
            imagens = ['https://i.ibb.co/xMkCjcD/aviso.png']
            mensagem = f'🤑💲 Dólar: ${cotacao_atual}{os.linesep} 🕒Data: {data_atual}{os.linesep} 🔗Link: www.linkdolar.com'
            enviar_fotos(chat_id='-1002210733596', links_imagens=imagens, caption=mensagem)
        
        sleep(10)


if __name__ == '__main__':
    main()