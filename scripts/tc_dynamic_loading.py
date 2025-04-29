from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Inicializa o driver usando WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Imprime data e hora do início do teste
    print(f"Início do teste: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    # Abre a página de teste
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    
    # Localiza e clica no botão Start
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()
    
    # Aguarda até que o texto "Hello World!" esteja visível (timeout de 10 segundos)
    hello_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )
    
    # Valida se o texto está presente
    if hello_text.text == "Hello World!":
        print("Teste passou: O texto 'Hello World!' está presente!")
    else:
        print(f"Teste falhou: Texto encontrado foi '{hello_text.text}'")

finally:
    # Imprime data e hora do final do teste
    print(f"Fim do teste: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    # Encerra a sessão do navegador
    driver.quit()
