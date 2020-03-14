from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

numOfVids = input("Would you like to download a single video or multiple (single/multiple)? ")
while True:
    if numOfVids != "single" and numOfVids != "multiple":
        numOfVids = input("Invalid choice. Would you like to download a single video or multiple (single/multiple)? ")
    else:
        break

videoType = input("Would you like to download as an audio file(mp3) or video file(mp4)? ")
while True:
    if videoType != "mp3" and videoType != "mp4":
        videoType = input("Invalid choice. Would you like to download as an audio file(mp3) or video file(mp4)? ")   
    else:
        break

numOfVids = numOfVids.lower()
if numOfVids == "single":
    if videoType == "mp3":
        videoLink = input("Please paste in the youtube link to the video you would like to download: ")
        driver = webdriver.Chrome('/Users/Jinha/Downloads/chromedriver')
        driver.get("https://ytmp3.cc/en13/")
        element = driver.find_element_by_id("input")
        for character in videoLink:
            element.send_keys(character)
            time.sleep(0.1)
        element = driver.find_element_by_id("submit")
        element.click()
        time.sleep(10)
        element = driver.find_element_by_link_text("Download")
        element.click()        
        print("Your youtube video has been downloaded as an mp3 file. Enjoy!")
        driver.close()

    elif videoType == "mp4":
        videoLink = input("Please paste in the youtube link to the video you would like to download: ")
        driver = webdriver.Chrome('/Users/Jinha/Downloads/chromedriver')
        driver.get("https://ytmp3.cc/en13/")
        element = driver.find_element_by_id("mp4")
        element.click()
        time.sleep(3)
        element = driver.find_element_by_id("input")
        for character in videoLink:
            element.send_keys(character)
            time.sleep(0.1)
        element = driver.find_element_by_id("submit")
        element.click()
        time.sleep(20)
        element = driver.find_element_by_link_text("Download")
        element.click()        
        print("Your youtube video has been downloaded as an mp4 file. Enjoy!")
        driver.close()

elif numOfVids == "multiple":
    if videoType == "mp3":
        videoLinks = ["blank"]
        while True:
            videoLinks.append(input("Please paste in the youtube link to the video you would like to download. Type 'stop' to stop entering links. "))
            if videoLinks[-1] == 'stop':
                break
            else:
                continue
        driver = webdriver.Chrome('/Users/Jinha/Downloads/chromedriver')
        driver.get("https://ytmp3.cc/en13/")
        for i in range(len(videoLinks) - 1):
            element = driver.find_element_by_id("input")
            for character in videoLinks[i + 1]:
                element.send_keys(character)
                time.sleep(0.1)
            time.sleep(2)
            element = driver.find_element_by_id("submit")
            element.click()
            time.sleep(10)
            element = driver.find_element_by_link_text("Download")
            element.click()
            time.sleep(2)
            element = driver.find_element_by_link_text("Convert next")
            element.click()
            time.sleep(2)
            driver.switch_to.active_element
        print("Your youtube videos have been downloaded as mp3 files. They can be found in your 'downloads' folder. Enjoy!")

    elif videoType == "mp4":
        element = driver.find_element_by_id("mp4")
        element.click()
        videoLinks = []
        while True:
            videoLinks.append(input("Please paste in the youtube link to the video you would like to download. Type 'stop' to stop entering links. "))
            if videoLinks[-1] == 'stop':
                break
            else:
                continue
        driver = webdriver.Chrome('/Users/Jinha/Downloads/chromedriver')
        driver.get("https://ytmp3.cc/en13/")
        element = driver.find_element_by_link_text("Convert")
        for i in range(len(videoLinks) - 1):
            element = driver.find_element_by_id("input")
            for character in videoLinks[i]:
                element.send_keys(character)
                time.sleep(0.1)
            element = driver.find_element_by_id("submit")
            element.click()
            time.sleep(10)
            element = driver.find_element_by_link_text("Download")
            element.click()
            time.sleep(2)
            element = driver.find_element_by_link_text("Convert next")
            element.click()
            time.sleep(2)
        print("Your youtube videos have been downloaded as mp4 files. They can be found in your 'downloads' folder. Enjoy!")
        driver.close()



            
        


     