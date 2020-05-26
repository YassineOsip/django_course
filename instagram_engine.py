from selenium import webdriver
from selenium.webdriver.common.keys import Keys
baseUrl = "https://www.instagram.com/{}/"


def getData(username):
    driver = webdriver.Firefox()
    driver.set_window_position(-3000, 0)
    data = {}
    driver.get(baseUrl.format(username))
    img = driver.find_element_by_class_name("_6q-tv").get_attribute("src")
    levelData = driver.find_element_by_class_name("k9GMp").text.split("\n")
    nameDescription = driver.find_element_by_class_name("-vDIg").text.split("\n")
    data["img"] = img
    data["posts"] = levelData[0]
    data["followers"] = levelData[1]
    data["following"] = levelData[2]
    data["fullName"] = nameDescription[0]
    data["description"] = nameDescription[1]
    driver.close()
    return data

