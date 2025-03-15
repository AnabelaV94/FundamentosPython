import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Caminho para o Brave
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

# Opções do Chrome para rodar com o Brave
options = webdriver.ChromeOptions()
options.binary_location = brave_path
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")  # Abre o browser maximizado

# Inicializa o WebDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Acessa o site
url = "https://www.buyfromportugal.com/export/"
driver.get(url)

# Uso de WebDriverWait para aguardar elementos
wait = WebDriverWait(driver, 10)  # Espera até 10s por um elemento

# Tenta aceitar cookies, se o botão existir
try:
    cookie_button = wait.until(
        EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
    )
    cookie_button.click()
    logging.info("✅ Botão de cookies clicado.")
except (NoSuchElementException, TimeoutException):
    logging.warning("⚠️ Botão de cookies não encontrado ou demorou para aparecer.")

# Pesquisa no campo "Sector"
try:
    sector_input = wait.until(
        EC.visibility_of_element_located((By.ID, "keyword_sector"))
    )
    sector_input.clear()
    sector_input.send_keys("1906")
    
    # Espera a lista de sugestões aparecer
    suggestion_list = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="eac-container-keyword_sector"]/ul'))
    )
    first_suggestion = suggestion_list.find_element(By.TAG_NAME, "li")
    first_suggestion.click()
    logging.info("✅ Sugestão clicada com sucesso!")

    # Clica no botão "Search"
    search_button = wait.until(
        EC.element_to_be_clickable((By.ID, "pesquisar_btn"))
    )
    search_button.click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results-view-detail")))  # Aguarda resultados
except Exception as e:
    logging.error(f"❌ Erro ao interagir com a pesquisa: {e}")

# Loop para percorrer todas as páginas
page = 1
while True:
    logging.info(f"\n🔄 Extraindo dados da página {page}...")

    # Extrai nomes e links das empresas
    try:
        companies = driver.find_elements(By.CLASS_NAME, "search-results-view-detail")
        if not companies:
            logging.warning(f"⚠️ Nenhuma empresa encontrada na página {page}!")
        else:
            logging.info(f"✅ {len(companies)} empresas encontradas na página {page}:\n")
            for company in companies:
                try:
                    name = company.text.strip()
                    link = company.get_attribute("href")
                    logging.info(f"📌 {name} - {link}")
                except Exception as e:
                    logging.error(f"❌ Erro ao extrair informações da empresa: {e}")

    except Exception as e:
        logging.error(f"❌ Erro ao encontrar empresas na página {page}: {e}")

    # Verifica se há próxima página
    try:
        next_button = driver.find_element(
            By.XPATH,
            f'//a[contains(@class, "paginate_button") and text()="{page + 1}"]'
        )

        if next_button.is_displayed():
            next_button.click()
            page += 1
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results-view-detail")))  # Aguarda a nova página carregar
        else:
            logging.info("✅ Não há mais páginas para navegar.")
            break

    except NoSuchElementException:
        logging.info("✅ Fim da paginação. Todas as empresas foram extraídas.")
        break

# Fecha o navegador
driver.quit()