from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from threading import Thread, Barrier





def main(x, y, width, height, barrier):
    driver = webdriver.Chrome()
    driver.set_window_size(width, height)
    driver.set_window_position(x, y)
    driver.get(url)
    # driver.find_element(By.CLASS_NAME, 'tiktok-g11lbl-Button-StyledLoginButton').click()
    # driver.find_element(By.XPATH, '//span[@data-e2e="bottom-sign-up"]').click()
    # driver.find_element(By.XPATH, '//p[text()="Continue with Google"]').click()
    # driver.find_element(By.XPATH, "//input[@name='identifier']").click()
    inputSeaerch = driver.find_element(By.XPATH, "//yt-icon[@icon='yt-icons:search']")
    inputSeaerch.click()
    inputSearch = driver.find_element(By.XPATH, "//input[@name='search_query']")
    searchKey = "SƠN TÙNG M-TP | CHÚNG TA CỦA HIỆN TẠI | OFFICIAL MUSIC VIDEO"
    for index in range(len(searchKey)):
        inputSearch.send_keys(searchKey[index])
        # time.sleep(0.2)
    barrier.wait()
    inputSearch.send_keys(Keys.ENTER)
    time.sleep(2)
    elementClick = driver.find_element(By.XPATH,
                                       "//a[@title='SƠN TÙNG M-TP | CHÚNG TA CỦA HIỆN TẠI | OFFICIAL MUSIC VIDEO']")
    elementClick.click()
    time.sleep(2)
    nextAds = driver.find_element(By.CLASS_NAME, "ytp-ad-skip-button")
    if nextAds:
        time.sleep(10)
        nextAds.click()
    else:
        time.sleep(5)
    time.sleep(100)


number_of_threads = 6

barrier = Barrier(number_of_threads)
url = 'https://www.facebook.com/'

threads = []
x = 0
y = 0
width = 320
height = 240
for _ in range(number_of_threads):
    t = Thread(target=main(x, y, width, height, barrier), args=(barrier,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
