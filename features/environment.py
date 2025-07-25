# features/environment.py
# pylint: skip-file
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
import tempfile

# --- Configuración General ---
FRONTEND_URL = "http://localhost:3000"
API_URL = "http://localhost:10000"
BROWSER = os.environ.get('BEHAVE_BROWSER', 'chrome').lower()



# --- Funciones de Ganchos (Hooks) ---

def before_all(context):
    """
    Se ejecuta una vez antes de todas las features.
    Configuraciones globales.
    """
    context.frontend_url = FRONTEND_URL
    context.api_url = API_URL
    print(f"\nIniciando pruebas E2E con Behave y Selenium en {BROWSER.capitalize()}...")
    print(f"Frontend URL: {context.frontend_url}")
    print(f"API URL: {context.api_url}")

def before_scenario(context, scenario):
    """
    Se ejecuta antes de cada escenario.
    Inicializa el WebDriver para un nuevo navegador por escenario.
    """
    print(f"\n--> Ejecutando escenario: {scenario.name}")

    if BROWSER == 'chrome':
        import tempfile
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-features=ChromeWhatsNewUI')
        # Directorio temporal único para evitar conflicto de perfil:
        user_data_dir = tempfile.mkdtemp()
        options.add_argument(f'--user-data-dir={user_data_dir}')
        context.driver = webdriver.Chrome(service=service, options=options)
    elif BROWSER == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        context.driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Navegador no soportado: {BROWSER}. Elige 'chrome' o 'firefox'.")

    # Tiempo de espera implícito:
    # El driver esperará hasta 10 segundos para que un elemento aparezca antes de lanzar una excepción.
    # Útil para la mayoría de los casos, pero las esperas explícitas (WebDriverWait) son más robustas.
    context.driver.implicitly_wait(10)
    context.driver.maximize_window() # Maximiza la ventana del navegador (si no está en headless)


def after_scenario(context, scenario):
    """
    Se ejecuta después de cada escenario.
    Cierra el WebDriver.
    """
    print(f"<-- Escenario '{scenario.name}' finalizado. Estado: {scenario.status}")

    # Si el escenario falló, toma una captura de pantalla para depurar.
    if scenario.status == "failed":
        if hasattr(context, 'driver'):
            screenshot_dir = "test_screenshots"
            os.makedirs(screenshot_dir, exist_ok=True) # Crea la carpeta si no existe
            screenshot_name = f"{scenario.name.replace(' ', '_').replace('/', '_')}_FAILED.png"
            screenshot_path = os.path.join(screenshot_dir, screenshot_name)
            context.driver.save_screenshot(screenshot_path)
            print(f"   ¡Escenario fallido! Captura de pantalla guardada en: {screenshot_path}")

    # Asegúrate de cerrar el navegador después de cada escenario.
    # Esto garantiza que cada escenario sea independiente y no tenga efectos secundarios de los anteriores.
    if hasattr(context, 'driver'):
        context.driver.quit()


def after_all(context):
    """
    Se ejecuta una vez después de todas las features.
    Limpieza global.
    """
    print("\nPruebas E2E con Behave y Selenium finalizadas.")
    # Si iniciaste la API Flask aquí, asegúrate de detenerla.
    # if hasattr(context, 'api_process'):
    #     context.api_process.terminate()
    #     context.api_process.wait() # Espera a que el proceso termine
    #     print("API Flask detenida.")
