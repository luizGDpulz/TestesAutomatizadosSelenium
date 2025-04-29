from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os

def create_test_report(form_data):
    report_content = f"""RELATÓRIO DE TESTE - TC-005: Preenchimento do formulário Formy

Site: https://formy-project.herokuapp.com/form
Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

DADOS PREENCHIDOS NO FORMULÁRIO:
------------------------------
First name: {form_data['first-name']}
Last name: {form_data['last-name']}
Job Title: {form_data['job-title']}
Highest level of education: {form_data['education']}
Sex: {', '.join(form_data['sex'])}
Years of experience: {form_data['experience']}
Date: {form_data['date']}

RESULTADO:
---------
Status: {form_data['status']}"""

    # Criar diretório evidence se não existir
    if not os.path.exists("relatorios/evidence"):
        os.makedirs("relatorios/evidence")

    # Salvar relatório como arquivo txt
    with open("relatorios/evidence/tc_formy_evidence.txt", "w", encoding="utf-8") as f:
        f.write(report_content)

def main():
    # Inicializar o driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)
    form_data = {
        'first-name': 'N/A',
        'last-name': 'N/A',
        'job-title': 'N/A',
        'education': 'N/A',
        'sex': [],
        'experience': 'N/A',
        'date': 'N/A',
        'status': 'N/A'
    }

    try:
        # Acessar o formulário
        driver.get("https://formy-project.herokuapp.com/form")
        
        try:
            # Preencher dados pessoais
            first_name = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
            first_name.send_keys("João")
            form_data['first-name'] = "João"

            last_name = wait.until(EC.presence_of_element_located((By.ID, "last-name")))
            last_name.send_keys("Silva")
            form_data['last-name'] = "Silva"

            job_title = wait.until(EC.presence_of_element_located((By.ID, "job-title")))
            job_title.send_keys("QA Engineer")
            form_data['job-title'] = "QA Engineer"

            # Selecionar nível de educação (radio button)
            education = wait.until(EC.presence_of_element_located((By.ID, "radio-button-2")))
            education.click()
            form_data['education'] = "College"

            # Selecionar sexo (checkbox)
            sex_male = wait.until(EC.presence_of_element_located((By.ID, "checkbox-1")))
            sex_male.click()
            form_data['sex'].append("Male")

            # Selecionar anos de experiência (dropdown)
            experience_select = wait.until(EC.presence_of_element_located((By.ID, "select-menu")))
            select = Select(experience_select)
            select.select_by_visible_text("2-4")
            form_data['experience'] = "2-4"

            # Preencher data
            date_input = wait.until(EC.presence_of_element_located((By.ID, "datepicker")))
            date_input.send_keys("04/29/2025")
            form_data['date'] = "04/29/2025"

            # Submeter o formulário
            submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")))
            submit_button.click()

            # Aguardar e validar mensagem de sucesso
            success_alert = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".alert.alert-success"))
            )
            
            if success_alert.is_displayed() and "successfully submitted" in success_alert.text:
                form_data['status'] = "Sucesso - Formulário enviado com sucesso"
            else:
                form_data['status'] = "Falha - Mensagem de sucesso não encontrada"

        except Exception as field_error:
            form_data['status'] = f"Falha ao preencher campo: {str(field_error)}"

    except Exception as e:
        form_data['status'] = f"Erro durante execução: {str(e)}"
    
    finally:
        # Criar relatório
        create_test_report(form_data)
        # Fechar o navegador
        driver.quit()

if __name__ == "__main__":
    main()