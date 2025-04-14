import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from .utils import get_logger

logger = get_logger("fetcher")

class HTMLFetcher:
    @staticmethod
    def from_file(file_path):
        from pathlib import Path
        logger.info(f"📂 Loading HTML from file: {file_path}")
        return Path(file_path).read_text(encoding="utf-8")

class SeleniumFetcher:
    def __init__(self, url, wait_for=".vehicle-tile-inner", headless=False):
        self.url = url
        self.wait_for = wait_for
        self.headless = headless

    def fetch(self):
        logger.info(f"🌐 Opening browser to fetch: {self.url}")

        options = Options()
        if self.headless:
            options.add_argument("--headless")  # Use "old" headless mode
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-features=VizDisplayCompositor")
        options.add_argument("--window-size=1280,1024")
        options.add_argument("--remote-debugging-port=9222")

        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.set_page_load_timeout(20)
            driver.get(self.url)

            try:
                cookie_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button#evidon-banner-acceptbutton"))
                )
                cookie_btn.click()
            except:
                logger.info("No cookie banner found.")

        
            logger.info(f"⏳ Waiting for element: {self.wait_for}")
            
            WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.wait_for))
            )
            time.sleep(4)  # Small delay for safety
            html = driver.page_source
            logger.info("✅ Page source successfully fetched.")
            return html
        except Exception as e:
            logger.error(f"❌ Error loading dynamic content: {e}")
            return ""
        finally:
            driver.quit()
