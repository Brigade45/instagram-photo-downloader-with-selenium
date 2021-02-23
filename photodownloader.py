from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import urllib.request
import os
instaID = ''                                #Fotoğrafını indirmek istediğiniz kişi
ID2 = ''                                    #İnstagram kullanıcı adınız
PW2 = ''                                    #İnstagram şifreniz
imagedizin='C:/Users/Brigade/Desktop/'      #Fotoğraflar verdiğiniz konum/imgs/instaID dizinine yüklenecektir.

def getAllPhotoLinkFromApi(L):
    driver.get(L+'?__a=1')
    driver.implicitly_wait(10)
    api_image_sources = []
    div = '/html/body/pre'
    foto=WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.XPATH,div)))
    api_image_sources.append(foto.text)
    splitted_source = foto.text.split(',')
    z = 0
    for source in splitted_source:
        if "\"src\":" in source:
            z+=1
            if z == 3:
                HighQualityPhotoLinks.append(source.replace('{"src":"', '').replace('"', ''))
    
HighQualityPhotoLinks = []
LL = [] 
linkler = []
Chrome_options = webdriver.ChromeOptions()
#Chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=Chrome_options)
driver.get('https://www.instagram.com/')
xpath_ID = '//*[@id="loginForm"]/div/div[1]/div/label/input'
xpath_PW = '//*[@id="loginForm"]/div/div[2]/div/label/input'
xpath_LB = '//*[@id="loginForm"]/div/div[3]/button'
xpath_NN = '//*[@id="react-root"]/section/main/div/div/div/div/button'
xpath_NN2 = '/html/body/div[4]/div/div/div/div[3]/button[2]'
xpath_PS = '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span'
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath_ID)))
ID = driver.find_element_by_xpath(xpath_ID).send_keys(ID2)
PW = driver.find_element_by_xpath(xpath_PW).send_keys(PW2)
LB = driver.find_element_by_xpath(xpath_LB).click()
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath_NN)))
NN = driver.find_element_by_xpath(xpath_NN).click()
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath_NN2)))
NN2 = driver.find_element_by_xpath(xpath_NN2).click()
driver.get('https://www.instagram.com/'+ instaID + '/')
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath_PS)))
PS = driver.find_element_by_xpath(xpath_PS).text
### SCROOL
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(2)
### SCROOL
driver.implicitly_wait(10)
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.TAG_NAME, 'a')))
linkler = driver.find_elements_by_tag_name('a')
for link in linkler:
    if 'https://www.instagram.com/p/' in link.get_attribute('href'):
        LL.append(link.get_attribute('href'))
for L in LL:
    getAllPhotoLinkFromApi(L)
    time.sleep(2)
driver.quit()

try:
    try:
        os.mkdir(imagedizin+'imgs/')
        print("imgs\\"+" dizini oluşturuldu.") 
    except:
        print("Dizin zaten var.")
    try:
        os.mkdir(imagedizin+'imgs/'+ instaID + '/')
        print("imgs\\"+instaID+"\\"+" dizini oluşturuldu.") 
    except:
        print("Dizin zaten var.")
except:
    print("Bir sorun oluştu.")


i = 1
for HighQualityPhoto in HighQualityPhotoLinks:
    urllib.request.urlretrieve(HighQualityPhoto, imagedizin+'imgs/' + instaID + '/' + str(i) + '.jpg')
    i+=1
print(str(i-1)+" adet fotoğraf kaydedildi.")
