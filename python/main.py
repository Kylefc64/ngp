from selenium import webdriver
import time

web = webdriver.Chrome()
#choose the url you wish to open
mainGameUrl = 'https://skribbl.io/'

web.get(mainGameUrl)

#allow the website enough time to load before reading or writing in its fields
time.sleep(1)

#choose what you want to write
name = "Nicholas"
customWordsInput = "is, it, working?, i, sure, hope, so"

#all the fields we can write into are listed here
nameXpath = '//*[@id="inputName"]'
customWordsXpath = '//*[@id="lobbySetCustomWords"]'

#all the buttons we can press are listed here
playButtonXpath = '/html/body/div[3]/div[2]/div[2]/div[1]/form/button[1]'
createPrivateRoomXpath = '/html/body/div[3]/div[2]/div[2]/div[1]/form/button[2]'
useCustomWordsOnlyXpath = '//*[@id="lobbyCustomWordsExclusive"]'
startPublicGameXpath = '//*[@id="formLogin"]/button[1]'
startPrivateGameXpath = '//*[@id="buttonLobbyPlay"]'

#the .click method presses the button we have selected


#create the forms you want from the elements listed above
#once created you can perform actions on them...
enterNameForm = web.find_element_by_xpath(nameXpath)
privateRoomButtonForm = web.find_element_by_xpath(createPrivateRoomXpath)
customWordsForm = web.find_element_by_xpath(customWordsXpath)
useCustomWordsOnlyButtonForm = web.find_element_by_xpath(useCustomWordsOnlyXpath)
startPrivateGameButtonForm = web.find_element_by_xpath(startPrivateGameXpath)


#tell our forms to do things, but not too quickly
enterNameForm.send_keys(name)
privateRoomButtonForm.click()
time.sleep(3)
customWordsForm.send_keys(customWordsInput)
useCustomWordsOnlyButtonForm.click()
startPrivateGameButtonForm.click()

