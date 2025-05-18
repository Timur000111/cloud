from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_example_page():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://example.com")
    assert "Example" in driver.title
    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "More information"))
    )
    link.click()
        assert driver.current_url == "https://www.iana.org/help/example-domains"
    driver.quit()
    
if __name__ == "__main__":
    test_example_page()
