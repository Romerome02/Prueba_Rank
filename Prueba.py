from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Definir variables
url = "https://www.google.com/"
search_term = "Coches en Londres gumtree"

# Crear el driver de Chrome
driver = webdriver.Chrome()

# Abrir la URL de Google
driver.get(url)

# Buscar "Coches en Londres"
driver.find_element(By.NAME, "q").send_keys(search_term)
driver.find_element(By.NAME, "q").submit()

time.sleep(3)

# Contar los enlaces de Gumtree
gumtree_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='gumtree.com']")
num_links = len(gumtree_links)

# Navegar a cada enlace de Gumtree y validar el título y el número de resultados
for link in gumtree_links:
    link.click()
    assert driver.find_element(By.CSS_SELECTOR, "h1").text != ""
    assert int(driver.find_element(By.CSS_SELECTOR, ".search-results-count").text) > 0
    driver.back()

# Cerrar el driver
driver.quit()

# Generar un informe con los resultados
print(f"Número de enlaces de Gumtree: {num_links}")
