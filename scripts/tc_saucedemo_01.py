from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# Inicializa o driver usando WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Imprime data e hora do início do teste
    print(f"Início do teste: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    # Abre o Google
    driver.get("https://www.saucedemo.com")
    
    # Localiza o campo de usuário, senha e o botão de login
    user_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    
    # Limpa os campos, envia o texto e submete (pressiona ENTER)
    user_field.clear()
    user_field.send_keys("standard_user")
    password_field.clear()
    password_field.send_keys("secret_sauce")

    login_button.click()
    
    try:
        error_message = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error-button']"))
        )
        print("Erro de login:", error_message.text)
    except:
        print("Login realizado com sucesso!")
    
    time.sleep(10)
finally:
    # Imprime data e hora do final do teste
    print(f"Fim do teste: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    # Encerra a sessão do navegador
    driver.quit()