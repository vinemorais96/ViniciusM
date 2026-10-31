"""
Desafio: Automatizar a coleta de filmes da Disney
Aluno: Vinicius Montagner
RA: 6326020
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def configurar_driver():
    """Configura o Chrome WebDriver com parâmetros adequados para raspagem."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=chrome_options)
    return driver

def raspar_filmes_disney():
    driver = configurar_driver()
    wait = WebDriverWait(driver, 15)
    lista_filmes = []

    try:
        # 1. Aceder à página de filmes da Disney
        url_alvo = "https://disney.com.br/filmes"
        print(f"[1/3] A aceder à página: {url_alvo}...")
        driver.get(url_alvo)
        time.sleep(3)

        # Tratar banner de cookies / LGPD caso surja
        try:
            btn_cookie = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            btn_cookie.click()
            print("  -> Banner de cookies aceite.")
            time.sleep(1)
        except Exception:
            pass

        # 2. Descer na página para ativar o carregamento dinâmico
        print("[2/3] A carregar secção de filmes...")
        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(2)

        # 3. Localizar os cards/elementos dos filmes
        seletores_cards = [
            ".shelf-grid .grid-item",
            "section[data-module='shelf'] .shelf-card",
            "a[data-title]",
            ".card-title",
            "h3.title",
            "h4"
        ]

        elementos_encontrados = []
        for seletor in seletores_cards:
            itens = driver.find_elements(By.CSS_SELECTOR, seletor)
            if len(itens) > 0:
                elementos_encontrados = itens
                print(f"  -> Seletor localizado: '{seletor}' ({len(itens)} itens)")
                break

        # Extrair os nomes dos filmes
        print("[3/3] A recolher os títulos dos filmes...")
        for item in elementos_encontrados:
            nome = ""

            nome_attr = item.get_attribute("data-title") or item.get_attribute("title")
            if nome_attr and nome_attr.strip():
                nome = nome_attr.strip()
            else:
                texto = item.text.strip()
                if texto:
                    nome = texto.split("\n")[0]

            if nome and nome not in lista_filmes and len(nome) > 1:
                lista_filmes.append(nome)

        # Apresentação no terminal
        print("\n" + "=" * 60)
        print(f"{'FILMES DA DISNEY RECOLHIDOS':^60}")
        print("=" * 60)

        for i, filme in enumerate(lista_filmes, start=1):
            print(f"{i:02d}. {filme}")

        print("=" * 60)
        print(f"Total de filmes encontrados: {len(lista_filmes)}\n")

    except Exception as erro:
        print(f"\n[ERRO]: {erro}")

    finally:
        driver.quit()
        print("Sessão finalizada.")

if __name__ == "__main__":
    raspar_filmes_disney()
    