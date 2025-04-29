# Testes Automatizados com Selenium

Este projeto contém uma suíte de testes automatizados utilizando Selenium WebDriver em Python para validar diferentes funcionalidades em diversos sites.

## Sumário dos Testes

### 1. Testes do SauceDemo
- [TC-001: Login bem-sucedido](./relatorios/tc_saucedemo_01.md)
  - Validação de login com credenciais válidas
  - Script: [tc_saucedemo_01.py](./scripts/tc_saucedemo_01.py)

- [TC-002: Falha de login](./relatorios/tc_saucedemo_02.md)
  - Validação de mensagem de erro com senha inválida
  - Script: [tc_saucedemo_02.py](./scripts/tc_saucedemo_02.py)

### 2. Teste de Carregamento Dinâmico
- [TC-003: Hello World](./relatorios/tc_dynamic_loading.md)
  - Validação de elemento com carregamento dinâmico
  - Script: [tc_dynamic_loading.py](./scripts/tc_dynamic_loading.py)

### 3. Teste E-commerce DemoBlaze
- [TC-004: Fluxo de Compra](./relatorios/tc_demoblaze.md)
  - Simulação completa de compra de produto
  - Script: [tc_demoblaze.py](./scripts/tc_demoblaze.py)

### 4. Teste de Formulário Formy
- [TC-005: Preenchimento de Formulário](./relatorios/tc_formy.md)
  - Validação de preenchimento e submissão de formulário
  - Script: [tc_formy.py](./scripts/tc_formy.py)

## Estrutura do Projeto

```
TestesAutomatizadosSelenium/
├── scripts/               # Scripts Python com os testes
└── relatorios/           # Documentação detalhada dos casos de teste
    └── evidence/         # Evidências geradas durante execução
```

## Principais Funcionalidades Testadas

1. **Autenticação (SauceDemo)**
   - Login com credenciais válidas
   - Tratamento de credenciais inválidas

2. **Carregamento Dinâmico (The Internet)**
   - Espera explícita por elementos
   - Validação de conteúdo dinâmico

3. **E-commerce (DemoBlaze)**
   - Seleção de produtos
   - Fluxo de checkout
   - Confirmação de compra
   - Geração de evidências

4. **Formulários (Formy)**
   - Preenchimento de campos
   - Validação de submissão
   - Geração de relatórios

## Links para Relatórios Detalhados

### Relatórios de Teste
- [Login Bem-sucedido SauceDemo](./relatorios/tc_saucedemo_01.md)
- [Login Falha SauceDemo](./relatorios/tc_saucedemo_02.md)
- [Carregamento Dinâmico](./relatorios/tc_dynamic_loading.md)
- [Fluxo de Compra DemoBlaze](./relatorios/tc_demoblaze.md)
- [Formulário Formy](./relatorios/tc_formy.md)

### Scripts de Teste
- [tc_saucedemo_01.py](./scripts/tc_saucedemo_01.py)
- [tc_saucedemo_02.py](./scripts/tc_saucedemo_02.py)
- [tc_dynamic_loading.py](./scripts/tc_dynamic_loading.py)
- [tc_demoblaze.py](./scripts/tc_demoblaze.py)
- [tc_formy.py](./scripts/tc_formy.py)

## Evidências
As evidências dos testes (screenshots e logs) são armazenadas em:
- `relatorios/evidence/`