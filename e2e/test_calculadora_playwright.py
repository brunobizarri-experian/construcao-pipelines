import os
import pytest
from playwright.sync_api import sync_playwright

BASE_URL = os.environ["APP_BASE_URL"]

@pytest.mark.parametrize(
    "num1, num2, operacao, esperado",
    [
        ("2", "3", "soma", "5"),
        ("5", "3", "subtracao", "2"),
        ("4", "6", "multiplicacao", "24"),
        ("10", "2", "divisao", "5"),
    ],
)
def test_operacoes_calculadora(num1, num2, operacao, esperado):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(BASE_URL, timeout=15000)

        page.fill('input[name="num1"]', num1)
        page.fill('input[name="num2"]', num2)
        page.select_option('select[name="operacao"]', operacao)
        page.click('button[type="submit"]')

        page.wait_for_selector("h2", timeout=5000)

        resultado = page.text_content("h2")
        assert esperado in resultado

        browser.close()

def test_divisao_por_zero():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(BASE_URL)

        page.fill('input[name="num1"]', '10')
        page.fill('input[name="num2"]', '0')
        page.select_option('select[name="operacao"]', 'divisao')
        page.click('button[type="submit"]')

        page.wait_for_selector("h2")

        assert "Erro: divisão por zero" in page.text_content("h2")

        browser.close()