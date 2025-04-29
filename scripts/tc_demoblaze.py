from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
from datetime import datetime

def create_evidence_txt(purchase_id, amount, timestamp):
    evidence_content = f"""Status: Sucesso – pedido confirmado e dados extraídos.
ID da Compra: {purchase_id}
Valor Total: {amount}
Data/Hora da execução: {timestamp}"""
    
    if not os.path.exists("relatorios/evidence"):
        os.makedirs("relatorios/evidence")
    
    evidence_file = os.path.join("relatorios", "evidence", "tc_demoblaze_evidence.txt")
    with open(evidence_file, "w", encoding="utf-8") as f:
        f.write(evidence_content)

def main():
    # Inicializar o driver
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        # Acessar o site
        driver.get("https://www.demoblaze.com/")
        
        # Maximizar a janela
        driver.maximize_window()
        
        # Escolher um produto (primeiro da lista)
        product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".card-title a")))
        product.click()
        
        # Clicar em Add to cart
        add_cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-success")))
        add_cart.click()
        
        # Esperar e aceitar o alerta
        time.sleep(1)  # Pequena pausa para garantir que o alerta apareça
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        
        # Ir para o carrinho
        cart = wait.until(EC.element_to_be_clickable((By.ID, "cartur")))
        cart.click()
        
        # Clicar em Place Order
        place_order = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-success")))
        place_order.click()
        
        # Preencher o formulário
        wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Test User")
        driver.find_element(By.ID, "country").send_keys("Brazil")
        driver.find_element(By.ID, "city").send_keys("São Paulo")
        driver.find_element(By.ID, "card").send_keys("4111111111111111")
        driver.find_element(By.ID, "month").send_keys("12")
        driver.find_element(By.ID, "year").send_keys("2025")
        
        # Confirmar a compra
        driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-primary").click()
        
        # Capturar informações do modal de confirmação
        confirmation = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sweet-alert")))
        confirmation_text = confirmation.text
        
        # Extrair ID e valor da compra
        lines = confirmation_text.split('\n')
        purchase_id = next(line for line in lines if "Id:" in line).split(": ")[1]
        amount = next(line for line in lines if "Amount:" in line).split(": ")[1]
        
        # Criar diretório para evidências se não existir
        if not os.path.exists("relatorios/evidence"):
            os.makedirs("relatorios/evidence")
        
        # Gerar timestamp atual
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        
        # Criar arquivo txt com evidências
        create_evidence_txt(purchase_id, amount, timestamp)
        
        # Capturar screenshot (sempre novo)
        screenshot_path = os.path.join("relatorios", "evidence", "tc_demoblaze_evidence.png")
        driver.save_screenshot(screenshot_path)
        
        # Clicar em OK para finalizar
        driver.find_element(By.CSS_SELECTOR, ".confirm").click()
        
    except Exception as e:
        print(f"Erro durante a execução do teste: {str(e)}")
        raise
    
    finally:
        # Fechar o navegador
        driver.quit()

if __name__ == "__main__":
    main()