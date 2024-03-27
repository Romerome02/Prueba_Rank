from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

# Configuramos el navegador Selenium (en este caso, Chrome o Firefox)
driver = webdriver.Chrome()
#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Abre Google y realiza una búsqueda de "Coches en Londres"
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Cars at London") # Si se pasa como parametro Cars at London gumtree Veras los resultados.
search_box.submit()

# Esperar a que se carguen los resultados de la búsqueda
time.sleep(2)

# Obtener todos los enlaces de los resultados de la búsqueda
gumtree_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='gumtree.com']")

# Mostrar todos los resultados de búsqueda y contar los enlaces de Gumtree
num_links = len(gumtree_links)

print("Número de enlaces de Gumtree disponibles:",num_links)

print("Resultados de búsqueda:")

for link in gumtree_links:
    print(link.get_attribute("href"))

    # Iterar sobre los enlaces de Gumtree y verificar su funcionamiento
gumtree_links_list = []
for link in gumtree_links:
    href = link.get_attribute("href")
    if "gumtree.com" in href:
        gumtree_links_list.append(href)
    
driver.quit()