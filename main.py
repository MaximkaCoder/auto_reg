import multiprocessing
from playwright.sync_api import sync_playwright
from time import sleep


def register(num, position):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://vulkanvegas.com/ru/register")
        page.get_by_text("Телефон", exact=True).click()
        sleep(1)
        page.locator("#popup-phone-sign-up").get_by_text("Номер телефона").click()
        sleep(1)
        page.locator("[type='tel']").fill("+880" + str(num))
        sleep(1)
        page.locator("#popup-phone-sign-up").get_by_text("Пароль").click()
        page.get_by_role("textbox", name="Пароль").fill("abubabhbchsdbhcdbs")
        page.get_by_role("checkbox", name="Мне уже исполнилось 18").check()
        page.get_by_role("button", name="Зарегистрироваться").click()
        sleep(2)
        page.get_by_role("button", name="Получить код подтверждения").click()
        sleep(1)
        print(f"Registering user {num} on page {page.url}")
        sleep(5)  # Simulate registration process
        browser.close()


if __name__ == '__main__':
    num_of_windows = 4
    positions = [(0, 0), (1600, 0), (0, 900), (1600, 900)]  # Positions for each window
    processes = []
    for i in range(num_of_windows):
        p = multiprocessing.Process(target=register, args=(1322896717 + i, positions[i]))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()