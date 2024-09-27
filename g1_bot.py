from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

def main():
    # Substitua pelo caminho correto
    service = Service(r'C:/Users/kaiol/Downloads/chromedriver-win64/chromedriver.exe')

    # Inicialize o WebDriver
    driver = webdriver.Chrome(service=service)

    # Abra o site do G1 Pernambuco
    driver.get('https://g1.globo.com/pe/pernambuco/')

    # Número de recargas
    num_reloads = 5

    for _ in range(num_reloads):
        # Aguarda um tempo aleatório entre recargas (3 a 10 segundos)
        wait_time = random.randint(3, 10)
        time.sleep(wait_time)

        driver.refresh()  # Recarrega a página
        print(f"Recarregando a página após {wait_time} segundos.")

        # Simula um clique em um ponto da tela
        actions = ActionChains(driver)
        actions.move_by_offset(100, 100)  # Mova o mouse para (100, 100)
        actions.click()  # Simula o clique
        actions.perform()  # Executa a ação

    print("A aba será fechada agora!")

    # Opcional: Aguarda um pouco antes de fechar
    time.sleep(3)

    # Fecha o navegador
    driver.quit()

if __name__ == "__main__":
    main()
