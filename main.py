import os
import sys
from src.bot import Bot
from utils.logger_config import logger

def resource_path(relative_path):
    '''
    Retorna o caminho absoluto para o recurso especificado pelo caminho relativo.    
    '''
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


def main():
    try:
        driver = resource_path('./driver/chromedriver.exe')
        config_path = resource_path('config.yaml')
        logger.info("Inicializando o bot com o arquivo de configuraçao.")
        bot = Bot(config_path, chrome_driver_path=driver)
        logger.info("Bot inicializado com sucesso.")
        
        logger.info("Carregando a pagina do Google.")
        bot.load_page('https://www.google.com')
        
        logger.info("Pesquisando 'python' na caixa de busca do Google.")
        search_box = bot.find(metodo="xpath", tag='//*[@id="APjFqb"]')
        search_box.send_keys('python')
        search_box.submit()
        
        logger.info("Aguardando resultados da pesquisa.")
        bot.click(metodo='xpath', tag='(//h3)[1]' )

        
        logger.info("Fechando o bot.")
        bot.quit()
    except Exception as e:
        logger.critical(f"Erro ao instanciar Navegador: {e}")

if __name__ == '__main__':
    main()