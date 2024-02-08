from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Web sürücüsü yolu (örnek: ChromeDriver için)
driver_path = 'C:\\Users\\dogan.irmak\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'  # Chromedriver'ın yolu

# Assuming driver_path is the path to your chromedriver
s=Service(driver_path)
driver = webdriver.Chrome(service=s)

# Web sayfasını açma
driver.get('https://www.tefas.gov.tr/FonKarsilastirma.aspx')

try:
    # Elementin yüklenmesini bekleyin (örneğin, bir ID'ye göre)
    element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "div"))
    )
    # Elementle ilgili işlemler burada
    print(element.text)  # Örnek: elementin metnini yazdır
finally:
    driver.quit()  # Tarayıcıyı kapat
