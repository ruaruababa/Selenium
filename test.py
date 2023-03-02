import time
from selenium import webdriver
from threading import Thread, Barrier
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
def func(barrier, x, y, rndNum, randTime):

    driver = webdriver.Chrome()
    driver.set_window_size(320, 240)
    driver.set_window_position(x, y)
    driver.get(url)

    inputSeaerch = driver.find_element(By.XPATH, "//yt-icon[@icon='yt-icons:search']")
    inputSeaerch.click()
    inputSearch = driver.find_element(By.XPATH, "//input[@name='search_query']")
    searchKey = "SƠN TÙNG M-TP | SKY DECADE | Nắng Ấm Ngang Qua"
    for index in range(len(searchKey)):
        inputSearch.send_keys(searchKey[index])
        time.sleep(randTime)
    inputSearch.send_keys(Keys.ENTER)
    print('wait for others')
    # barrier.wait()
    inputSearch.send_keys(Keys.ENTER)
    time.sleep(2)
    elementClick = driver.find_element(By.XPATH,
                                       "//a[@title='SƠN TÙNG M-TP | SKY DECADE | Nắng Ấm Ngang Qua']")
    time.sleep(2)
    elementClick.click()
    barrier.wait()
    time.sleep(6)
    nextAds = driver.find_element(By.CLASS_NAME, "ytp-ad-skip-button-container")
    time.sleep(2)
    nextAds.click()
    # barrier.wait()
    # time.sleep(rndNum)
    # if bool(nextAds):
    #     time.sleep(rndNum)
    #     nextAds.click()
    time.sleep(100)


# ---

url = 'https://youtube.com'

number_of_threads = 5


barrier = Barrier(number_of_threads)

threads = []
width = 480
height = 400
for _ in range(number_of_threads):
    rndNum = random.randrange(5, 8)
    randTime = random.uniform(0.1, 0.5)
    t = Thread(target=func, args=(barrier, _*width, 0, rndNum, randTime))
    if _ > 3:
        t = Thread(target=func, args=(barrier, (_-4)*width, height, rndNum, randTime))
    if _ > 7:
        t = Thread(target=func, args=(barrier, (_-8)*width, height*2-40, rndNum, randTime))
    t.start()
    threads.append(t)

for t in threads:
    t.join()