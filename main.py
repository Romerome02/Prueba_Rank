from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurar el navegador Selenium (en este caso, Chrome)
driver = webdriver.Chrome()

# Abre Google y realiza una búsqueda de "Coches en Londres"
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Coches en Londres gumtree")
search_box.submit()

# Esperar a que se carguen los resultados de la búsqueda
time.sleep(3)

# Obtener todos los enlaces de los resultados de la búsqueda
gumtree_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='gumtree.com']")

# Mostrar todos los resultados de búsqueda y contar los enlaces de Gumtree
print("Resultados de búsqueda:")
for link in gumtree_links:
    print(link.get_attribute("href"))
print("Número de enlaces de Gumtree disponibles:", len(gumtree_links))

# Navegar a cada enlace de Gumtree y verificar el título y el número de resultados
for link in gumtree_links:
    href = link.get_attribute("href")
    driver.get(href)
    title = driver.title
    results_count = driver.find_element(By.CSS_SELECTOR, "span[aria-label='results count']")
    results_count = int(results_count.text.replace(",", ""))
    if results_count > 0:
        print("Título de la página:", title)
        print("Número de resultados:", results_count)

# Cerrar el navegador
driver.quit()
