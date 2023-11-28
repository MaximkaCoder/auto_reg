from playwright.sync_api import Playwright, sync_playwright
from time import sleep


def run(playwright: Playwright, num):
    num += 1
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://vulkanvegas.com/ru/register")
    page.get_by_text("Телефон", exact=True).click()
    sleep(1)
    page.locator("#popup-phone-sign-up").get_by_text("Номер телефона").click()
    sleep(1)
    page.locator("[type=\"tel\"]").fill("+880" + str(num))
    sleep(1)
    page.locator("#popup-phone-sign-up").get_by_text("Пароль").click()
    page.get_by_role("textbox", name="Пароль").fill("abubabhbchsdbhcdbs")
    page.get_by_role("checkbox", name="Мне уже исполнилось 18").check()
    page.get_by_role("button", name="Зарегистрироваться").click()
    sleep(2)
    page.get_by_role("button", name="Получить код подтверждения").click()
    sleep(1)
    browser.close()
    run(playwright, num)


with sync_playwright() as playwright:
    run(playwright, 1322595217)
