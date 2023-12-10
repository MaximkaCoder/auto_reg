import multiprocessing
import threading

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from time import sleep
import multiprocessing


def registration(phone_num, position):
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--use_subprocess")
    browser = uc.Chrome(options=chrome_options, driver_executable_path="D:\\temp\\chromedriver.exe")
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
        browser.get("https://vulkanvegas.com/ru/register")
        sleep(2)
        list_button = browser.find_elements(by=By.XPATH, value="//li[contains(text(), 'Телефон')]")[0]
        browser.execute_script("window.open('https://vulkanvegas.com/ru/register');")
        browser.switch_to.window(browser.window_handles[-1])
        browser.execute_script("arguments[0].scrollIntoView();", list_button)
        list_button.click()
        sleep(1)
        browser.find_element(By.XPATH, '/html/body/div[4]/div/div/div[3]/form[2]/div[2]/div[1]/div/input').click()
        browser.find_element(By.XPATH, '/html/body/div[4]/div/div/div[3]/form[2]/div[1]/div[1]/div[1]/label').click()
        browser.find_element(By.XPATH, '/html/body/div[4]/div/div/div[3]/form[2]/div[1]/div[1]/div[1]/div/div/div[1]').click()
        sleep(1)
        set_country = browser.find_element(By.XPATH,
                                           '//*[@id="popup-phone-sign-up"]/div[1]/div[1]/div[1]/div/div/div['
                                           '2]/section/div[14]'
                                           )
        browser.execute_script("arguments[0].click();", set_country)

        browser.find_element(By.XPATH,
                             '/html/body/div[4]/div/div/div[3]/form[2]/div[1]/div[1]/div[1]/div/input'
                             ).send_keys(phone_num)
        browser.find_element(By.XPATH,
                             '/html/body/div[4]/div/div/div[3]/form[2]/div[1]/div[2]/div[1]/div/input'
                             ).send_keys("dsbjfbdsjhbdshj")
        reg_butt = browser.find_element(By.XPATH, '/html/body/div[4]/div/div/div[3]/form[2]/button')
        browser.execute_script("arguments[0].click();", reg_butt)

        element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/div[2]/button')))
        element.click()
        # browser.save_screenshot("scr.png")
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
        f.truncate()  # remove any leftover whitespace

    t = threading.Thread(target=registration, args=(phone_num, position))
    t.start()


if __name__ == '__main__':
    count_of_window = 4
    positions = [(0, 0), (0, 500), (550, 0), (550, 500)]

    for i in range(count_of_window):
        run_registration(positions[i])
