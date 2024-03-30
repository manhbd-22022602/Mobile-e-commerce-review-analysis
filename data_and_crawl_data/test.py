from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://www.thegioididong.com/dtdd")


# Tìm phần tử bằng XPath
product = driver.find_element(By.XPATH, '//*[@id="categoryPage"]\
                              /div[3]/ul/li[1]/a[1]')
product.click()

comment = driver.find_element(By.XPATH,
                              '/html/body/section[1]/div[3]/div[1]\
                                /div[18]/div[2]\
                                /div/div/div[6]/div/a')
comment.click()

comment_detail = driver.find_element(By.XPATH, '//*[@id=\
                                     "r-56509474"]/div[3]/p')
print(comment_detail.text)
