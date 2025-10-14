from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
# Configura o WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
 
# Acessa a página inicial do LinkedIn
driver.get("https://www.linkedin.com")
 
# Aguarda o carregamento da página
time.sleep(2)
 
# Clica no botão "Sign in with email"
sign_in_email_button = driver.find_element(By.CSS_SELECTOR, '[data-test-id="home-hero-sign-in-cta"]')
sign_in_email_button.click()
 
# Aguarda o redirecionamento para a página de login
time.sleep(2)
 
# Preenche o campo de e-mail
email_input = driver.find_element(By.ID, "username")
email_input.send_keys("Coloque seu email aqui EX: pedroqeateste@gmail.com")
 
# Preenche o campo de senha
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("Coloque sua senha aqui EX: Senha123")
 
# Clica no botão de login
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
 
# Aguarda para verificar se o login foi bem-sucedido
time.sleep(2)
 
if "feed" in driver.current_url:
    print("Login realizado com sucesso!")
else:
    print("Falha no login.")
 
# Aguarda a página carregar
time.sleep(1)
 
# Clica no botão "Start a post"
start_post_button = driver.find_element(By.XPATH, "//button[contains(., 'Start a post')]")
start_post_button.click()
 
time.sleep(1)
 
# Localiza o campo de texto da postagem
post_text_area = driver.find_element(By.CLASS_NAME, "ql-editor")
post_text_area.click()
post_text_area.send_keys("Este é um post automatizado com Selenium!")
 
time.sleep(2)
 
# Clica no botão "Postar"
post_button = driver.find_element(By.XPATH, "//button[contains(., 'Post')]")
post_button.click()
time.sleep(2)
 
# Aguarda a janela de privacidade aparecer
wait = WebDriverWait(driver, 10)
 
# Seleciona a opção de privacidade "Anyone"
privacy_button = wait.until(EC.element_to_be_clickable((By.ID, "ANYONE")))
privacy_button.click()
time.sleep(2)

# Clica no botão "Done"
done_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.artdeco-button--primary")))
done_button.click()
time.sleep(2)
 
# Confirma a postagem clicando no botão "Post"
final_post = driver.find_element(By.CSS_SELECTOR, "button.share-actions__primary-action.artdeco-button--primary")
final_post.click()

# Gera uma captura de tela da postagem antes de finalizar
driver.save_screenshot("evidencia_post_linkedin.png")
 
print("Post publicado com sucesso!")
 
input("Pressione Enter para encerrar o navegador...")
driver.quit()
