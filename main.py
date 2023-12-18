import multiprocessing
import threading

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

import captcha
from solve_captcha import solveRecaptcha
from captcha import send_solve
from time import sleep

import multiprocessing


def registration(phone_num, position):
    options = uc.ChromeOptions()
    options.add_argument(r'--load-extension=D:\Python_projects\amazon_reg\Captcha-Solver')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--no-first-run')
    options.add_argument('--no-default-browser-check')
    options.add_argument("--use_subprocess")
    browser = uc.Chrome(options=options, driver_executable_path="D:\\temp\\chromedriver.exe")

    browser.get('https://accounts.google.com/')
    browser.set_window_position(*position)
    browser.set_window_size(400, 500)
    try:
        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))

        element.send_keys("efrosinovich@gmail.com")
        browser.find_element(By.ID, "identifierNext").click()
        sleep(5)
        browser.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("Genius2003")
        browser.find_element(By.ID, "passwordNext").click()
        sleep(5)
        captcha.send_solve(browser, phone_num)
        sleep(60)
        browser.quit()
    except Exception:
        browser.quit()


def run_registration(position):
    with open('phones.txt', 'r+') as f:
        lines = f.readlines()
        if not lines:
            print("No more phone numbers left in the file.")
            return
        phone_num = lines[0].strip()  # read the first line/phone number
        f.seek(0)  # rewind the file
        for line in lines[1:]:  # write all the other lines back into the file
            f.write(line)
        # f.truncate()  # remove any leftover whitespace

    t = threading.Thread(target=registration, args=(phone_num, position))
    t.start()


if __name__ == '__main__':
    count_of_window = 2
    positions = [(0, 0), (0, 500), (550, 0), (550, 500)]

    for i in range(count_of_window):
        run_registration(positions[i])
