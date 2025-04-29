# Caso de Teste (TC-001): Login bem-sucedido com usuário padrão

## Site-alvo  
https://www.saucedemo.com/

---

## Objetivo  
Verificar se, ao utilizar as credenciais padrão (`standard_user` / `secret_sauce`), o login é realizado com sucesso e a página de produtos é exibida corretamente. Em caso de falha, deve-se capturar a mensagem de erro no elemento com classe `error-message-container`.

---

## Requisitos  
- Acessar a página de login.  
- Preencher usuário e senha com as credenciais válidas.  
- Submeter o formulário de login.  
- Verificar ausência de mensagem de erro e exibição da página de produtos.

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
9. Inserir **`secret_sauce`** no campo de senha.  
10. Clicar no botão **Login**.  
11. Aguardar até 3 segundos pela presença de elemento de erro (`[data-test='error-button']`).  
12. Verificar:
    - Se o elemento de erro aparecer → capturar e registrar a mensagem exibida.  
    - Caso contrário → registrar “Login realizado com sucesso!”.  
13. Aguardar 10 segundos para observação manual (sleep).  
14. Registrar data e hora de término do teste.  
15. Encerrar a sessão do navegador.

---

## Dados de Entrada  
- **Usuário:** `standard_user`  
- **Senha:** `secret_sauce`  

---

## Resultado Esperado  
- A página de produtos (`/inventory.html`) deve ser exibida sem mensagem de erro.  
- Em caso de falha de autenticação, um texto de erro deve aparecer no elemento com classe `error-message-container`.

---

## Resultado Obtido  
- **Status:** Sucesso – login efetuado e página de produtos carregada.  
- **Logs impressos no console:**  
  ```
  Início do teste: 29/04/2025 13:46:40
  Login realizado com sucesso!
  Fim do teste: 29/04/2025 13:46:54
  ```  
- **Data/Hora de Início:** 29/04/2025 13:46:40  
- **Data/Hora de Término:** 29/04/2025 13:46:54  
- **Capturas de Tela:** não aplicável (teste passou sem erros).  

---  

> **Observação:** Se o teste apresentasse falha, o script capturaria a mensagem de erro exibida no contêiner com classe `error-message-container`, conforme requisito.