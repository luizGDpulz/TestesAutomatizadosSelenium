# Caso de Teste (TC-002): Falha de login com senha inválida

## Site-alvo  
https://www.saucedemo.com/

---

## Objetivo  
Verificar se, ao utilizar a senha incorreta para o usuário padrão, o sistema exibe a mensagem de erro adequada no contêiner de erros.

---

## Requisitos  
- Acessar a página de login.  
- Informar usuário válido e senha inválida.  
- Submeter o formulário de login.  
- Capturar a mensagem de erro exibida no elemento com classe `error-message-container`.

---

## Passos Executados  
1. Inicializar o **WebDriver** do Chrome via WebDriver Manager.  
2. Registrar data e hora de início do teste.  
3. Navegar para `https://www.saucedemo.com`.  
4. Localizar o campo de usuário (`ID: user-name`).  
5. Localizar o campo de senha (`ID: password`).  
6. Localizar o botão de login (`ID: login-button`).  
7. Limpar os campos de usuário e senha.  
8. Inserir **`standard_user`** no campo de usuário.  
9. Inserir **`SENHA_ERRADA`** no campo de senha.  
10. Clicar no botão **Login**.  
11. Aguardar até 3 segundos pela presença do elemento de erro (`[data-test='error-button']`).  
12. Capturar e imprimir o texto da mensagem de erro, se presente.  
13. Aguardar 10 segundos para observação manual.  
14. Registrar data e hora de término do teste.  
15. Encerrar a sessão do navegador.

---

## Dados de Entrada  
- **Usuário:** `standard_user`  
- **Senha:** `SENHA_ERRADA`  

---

## Resultado Esperado  
- O sistema **não** deve permitir o acesso.  
- Deve ser exibida, dentro do contêiner de erro, uma mensagem indicando que usuário e senha não correspondem a nenhum registro.

---

## Resultado Obtido  
- **Status:** Falha de autenticação confirmada.  
- **Mensagem de Erro Capturada:**  
  ```
  Epic sadface: Username and password do not match any user in this service
  ```  
- **Data/Hora de Início:** 29/04/2025 14:01:10  
- **Data/Hora de Término:** 29/04/2025 14:01:15  
