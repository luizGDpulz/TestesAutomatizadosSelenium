# Caso de Teste (TC-004): Simulação de compra de um produto

## Site-alvo  
https://www.demoblaze.com/

---

## Objetivo  
Simular o fluxo completo de compra de um produto qualquer, desde a seleção até a confirmação do pedido, incluindo tratamento de alertas JavaScript e captura dos dados do modal de confirmação (ID do pedido e valor), bem como geração de arquivo de relatório em formato TXT.

---

## Requisitos  
1. Selecionar dinamicamente um produto da lista.  
2. Clicar em **Add to cart** e aceitar o alerta.  
3. Acessar o carrinho e clicar em **Place Order**.  
4. Preencher o formulário de compra (nome, país, cidade, cartão, mês e ano).  
5. Confirmar a compra e aguardar o modal de confirmação.  
6. Capturar o texto completo do modal de confirmação (ID e valor).  
7. Tratar alertas JavaScript.  
8. Salvar esses dados: 
   - Em um arquivo TXT (`relatorios/evidence/tc_demoblaze_evidence.txt`).  
9. Gerar evidência em screenshot.

---

## Passos Executados  
1. Inicializar o _WebDriver_ do Chrome e aguardar até 10 s por elementos clicáveis.  
2. Navegar para `https://www.demoblaze.com/` e maximizar a janela.  
3. Aguardar que o primeiro produto esteja clicável (`.card-title a`) e clicar para acessar sua página.  
4. Aguardar que o botão **Add to cart** (`.btn-success`) esteja clicável e clicar.  
5. Aguardar a presença do alerta JavaScript e aceitá-lo (_alert.accept()_).  
6. Aguardar que o link **Cart** (`ID: cartur`) esteja clicável e clicar.  
7. Aguardar que o botão **Place Order** (`.btn-success`) esteja clicável e clicar.  
8. Preencher o formulário de compra:
   - **Name:** `Test User`  
   - **Country:** `Brazil`  
   - **City:** `São Paulo`  
   - **Credit card:** `4111111111111111`  
   - **Month:** `12`  
   - **Year:** `2025`  
9. Clicar em **Purchase** (`#orderModal .btn-primary`).  
10. Aguardar o modal de confirmação (`.sweet-alert`) ficar visível.  
11. Capturar o texto completo do modal e extrair:
    - **ID da Compra** (linha contendo “Id:”)  
    - **Valor Total** (linha contendo “Amount:”)  
12. Salvar screenshot da confirmação em `relatorios/evidence/tc_demoblaze_evidence.png`.  
13. Criar arquivo TXT em `relatorios/evidence/tc_demoblaze_evidence.txt` com ID e valor.  
14. Clicar em **OK** para fechar o modal.  
15. Encerrar o navegador.

---

## Dados de Entrada  
- **Produto:** primeiro item da lista (dinâmico)  
- **Nome:** `Test User`  
- **País:** `Brazil`  
- **Cidade:** `São Paulo`  
- **Cartão:** `4111111111111111`  
- **Mês:** `12`  
- **Ano:** `2025`  

---

## Resultado Esperado  
- Aparecer um alerta JavaScript e ser aceito.  
- O modal de confirmação deve exibir, de forma legível, o **ID da compra** e o **Valor total**.  
- Um screenshot da tela de confirmação deve ser salvo.  
- Gerar e salvar arquivo TXT com as informações do pedido (`relatorios/evidence/tc_demoblaze_evidence.txt`).  