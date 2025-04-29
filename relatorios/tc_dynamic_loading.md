# Caso de Teste (TC-003): Validação do texto dinâmico “Hello World!”

## Site-alvo  
https://the-internet.herokuapp.com/dynamic_loading/1

---

## Objetivo  
Ao clicar no botão **Start**, aguardar até que o texto **“Hello World!”** esteja visível e validar sua presença na página.

---

## Requisitos  
1. Utilizar **explicit waits** (por exemplo, `WebDriverWait` + `expected_conditions`) para aguardar o carregamento do texto.  
2. **Registrar o tempo total de espera** (intervalo entre o clique e a aparição do texto).  
3. **Capturar exceção** caso o texto não apareça dentro do timeout definido (10 s).

---

## Passos Executados  
1. Inicializar o **WebDriver** do Chrome via WebDriver Manager.  
2. Registrar data/hora de início do teste.  
3. Navegar para `https://the-internet.herokuapp.com/dynamic_loading/1`.  
4. Localizar e clicar no botão **Start** (`CSS_SELECTOR: #start button`).  
5. Aguardar, com timeout de 10 segundos, até que o elemento `#finish h4` esteja visível.  
6. Verificar se o texto encontrado é exatamente **“Hello World!”**.  
7. Imprimir no console:
   - Se o texto for correto → `"Teste passou: O texto 'Hello World!' está presente!"`.  
   - Caso contrário → `"Teste falhou: Texto encontrado foi '<valor>'"`.  
8. Registrar data/hora de término do teste.  
9. Encerrar a sessão do navegador.

---

## Dados de Entrada  
- **URL:** `https://the-internet.herokuapp.com/dynamic_loading/1`  
- **Timeout para espera explícita:** 10 segundos  

---

## Resultado Esperado  
- O texto **“Hello World!”** deve ficar visível antes do fim do timeout.  
- Deve-se imprimir no console a confirmação de sucesso.  
- O intervalo entre início e fim (tempo total de espera) deve ser capturado.  
- Se o texto não surgir em até 10 s, deve-se capturar a exceção (`TimeoutException`) e registrar a falha.

---

## Resultado Obtido  
- **Status:** Sucesso — o texto **“Hello World!”** tornou-se visível antes de 10 s.  
- **Log de console** (exemplo):
  ```
  Início do teste: 29/04/2025 14:20:12
  Teste passou: O texto 'Hello World!' está presente!
  Fim do teste:  29/04/2025 14:20:17
  ```
- **Tempo total de espera:** 5 segundos (diferença entre início e fim).  
- **Captura de exceção:** não aplicável (texto apareceu dentro do timeout).