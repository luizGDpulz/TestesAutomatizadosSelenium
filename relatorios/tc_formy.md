# Caso de Teste (TC-005): Preenchimento completo do formulário Formy

## Site-alvo  
https://formy-project.herokuapp.com/form

---

## Objetivo  
Preencher todos os campos do formulário (nome, sobrenome, e-mail, telefone, gênero, experiência, profissão, ferramentas, continente e comandos de automação) e submeter, validando a exibição do alerta de sucesso.

---

## Requisitos  
1. Explorar diferentes localizadores (name, id, CSS selector e XPath).  
2. Em dropdowns, usar a classe `Select` do Selenium.  
3. Registrar em relatório Markdown os valores finais selecionados em cada campo.  
4. Gerar arquivo TXT de evidência com os mesmos dados.

---

## Passos Executados  
1. Inicializar o **WebDriver** do Chrome via WebDriver Manager e instanciar `WebDriverWait(driver, 10)`.  
2. Navegar para `https://formy-project.herokuapp.com/form`.  
3. Aguardar presença do campo **First name** (`ID: first-name`) e inserir **“João”**.  
4. Aguardar presença do campo **Last name** (`ID: last-name`) e inserir **“Silva”**.  
5. Aguardar presença do campo **Job Title** (`ID: job-title`) e inserir **“QA Engineer”**.  
6. Selecionar o rádio **College** (`ID: radio-button-2`).  
7. Marcar o checkbox **Male** (`ID: checkbox-1`).  
8. Aguardar presença do dropdown **Years of experience** (`ID: select-menu`), instanciar `Select`, e escolher **“2-4”**.  
9. Aguardar presença do campo **Datepicker** (`ID: datepicker`) e inserir **“04/29/2025”**.  
10. Clicar no botão **Submit** (`CSS: .btn.btn-lg.btn-primary`).  
11. Aguardar presença do alerta de sucesso (`CSS: .alert.alert-success`).  
12. Extrair texto do alerta e validar se contém **“successfully submitted”**.  
13. Registrar data/hora de início e fim, gerar arquivo TXT em `relatorios/evidence/tc_formy_evidence.txt` e relatório Markdown.

---

## Dados de Entrada Utilizados  
- **First name:** João  
- **Last name:** Silva  
- **Job Title:** QA Engineer  
- **Highest level of education:** College  
- **Sex:** Male  
- **Years of experience:** 2-4  
- **Date:** 04/29/2025  

---

## Resultado Esperado  
- Todos os campos preenchidos corretamente.  
- Ao submeter, exibição de mensagem de sucesso contendo “successfully submitted”.  
- Registro em relatório Markdown dos valores preenchidos.  
- Geração de arquivo TXT de evidência com os mesmos dados.  

---

## Resultado Obtido  
- **Status:** Sucesso – formulário enviado com sucesso.  
- **Alerta exibido:** “The form was successfully submitted!”  
- **Data/Hora da execução:** 29/04/2025 15:02:10  
- **Dados preenchidos confirmados no relatório Markdown e no TXT de evidência.**  
- **Arquivo TXT gerado:** `relatorios/evidence/tc_formy_evidence.txt`  