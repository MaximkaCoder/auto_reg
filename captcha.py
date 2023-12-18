from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from time import sleep

from selenium import webdriver

from solve_captcha import solveRecaptcha


def send_solve(browser, phone):
    browser.get("chrome-extension://mdabanckblelbopgfojpkglhpknaceop/popup/popup.html")
    sleep(1)
    browser.refresh()
    browser.find_element(By.CLASS_NAME, 'default-btn').click()
    sleep(2)
    browser.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[3]/table/tbody/tr[3]/td[2]/input[2]').click()
    sleep(2)

    browser.get("https://vulkanvegas.com/ru/register")
    sleep(2)
    list_button = browser.find_elements(by=By.XPATH, value="//li[contains(text(), 'Телефон')]")[0]
    browser.execute_script("arguments[0].scrollIntoView();", list_button)
    list_button.click()
    sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[4]/div/div/div[3]/form[2]/div[2]/div[1]/div/input').click()
    browser.find_element(By.XPATH, '/html/body/div[4]/div/div/div[3]/form[2]/div[1]/div[1]/div[1]/label').click()
    browser.find_element(By.XPATH,
                         '/html/body/div[4]/div/div/div[3]/form[2]/div[1]/div[1]/div[1]/div/div/div[1]').click()
    sleep(1)
    set_country = browser.find_element(By.XPATH,
                                       '//*[@id="popup-phone-sign-up"]/div[1]/div[1]/div[1]/div/div/div['
                                       '2]/section/div[1]'
                                       )
    browser.execute_script("arguments[0].click();", set_country)

    browser.find_element(By.XPATH,
                         '/html/body/div[4]/div/div/div[3]/form[2]/div[1]/div[1]/div[1]/div/input'
                         ).send_keys(phone)
    browser.find_element(By.XPATH,
                         '/html/body/div[4]/div/div/div[3]/form[2]/div[1]/div[2]/div[1]/div/input'
                         ).send_keys("dsbjfbdsjhbdshj")
    reg_butt = browser.find_element(By.XPATH, '/html/body/div[4]/div/div/div[3]/form[2]/button')
    browser.execute_script("arguments[0].click();", reg_butt)
    sleep(5)

    button = WebDriverWait(browser, 180).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[2]/div[2]/button')))
    button.click()
    print("clicked!")
