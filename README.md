# LinkedIn Post Automation

Automação de ponta a ponta (E2E) para publicar posts no LinkedIn usando Python e Selenium WebDriver.

## Objetivo

Este projeto automatiza todo o fluxo de publicação de um post no LinkedIn: abre o navegador, faz login, cria o post, define a privacidade, publica e salva uma captura de tela como evidência.

Foi um dos meus primeiros projetos de automação web. Nele pratiquei os fundamentos usados em automação de testes: localização de elementos, esperas, validação de estado e geração de evidências.

## Como funciona

1. Abre o Chrome e acessa o LinkedIn
2. Clica em "Sign in with email" e preenche usuário e senha
3. Valida o login conferindo se a URL foi redirecionada para o feed
4. Clica em "Start a post" e escreve o texto
5. Define a privacidade do post como "Anyone"
6. Publica o post
7. Salva uma captura de tela como evidência (`evidencia_post_linkedin.png`)

## Conceitos aplicados

- **Localizadores variados:** `ID`, `CSS_SELECTOR`, `XPATH` e `CLASS_NAME`
- **Esperas explícitas:** `WebDriverWait` com `expected_conditions`
- **Validação de resultado:** checagem da URL após o login
- **Evidência de execução:** screenshot gerado ao final do fluxo

## Tecnologias utilizadas

- [Python 3.14.0](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- Google Chrome (o driver é baixado automaticamente pelo Selenium Manager)
- Ambiente virtual com `venv`

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/Psolla/Linkedin_post_automation.git
cd Linkedin_post_automation
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS/Linux
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como executar

1. No arquivo `post_linkedin_automation.py`, substitua os textos de exemplo pelo seu e-mail, senha e o conteúdo do post.
2. Execute:

```bash
python post_linkedin_automation.py
```

Ao final, o resultado é exibido no terminal e a evidência é salva na pasta do projeto.

## Limitações conhecidas

- Contas com verificação em duas etapas ou captcha exigem intervenção manual
- Algumas etapas usam `time.sleep()` fixo, que pode falhar em conexões lentas
- Mudanças no layout do LinkedIn podem quebrar os seletores

## Aviso

Projeto criado para fins de estudo e portfólio. Os Termos de Uso do LinkedIn não permitem automação não autorizada na plataforma; use por sua conta e risco.

## Autor

Pedro Henrique Solla Nunes — [LinkedIn](https://www.linkedin.com/in/pedrohsn) · [GitHub](https://github.com/Psolla)
