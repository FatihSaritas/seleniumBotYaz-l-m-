from teamsInfo import email,password
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

class Teams:
    def __init__(self,email,password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
        
    def signIn(self):
        self.browser.get('https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=id_token&scope=openid%20profile&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=eyJpZCI6IjgzZDk5YWNmLTUxNWYtNGE5Ny1hMTM4LWZjZWVlNmFmNzQ0NyIsInRzIjoxNzEwMTc1ODUxLCJtZXRob2QiOiJyZWRpcmVjdEludGVyYWN0aW9uIn0%3D&nonce=c0e0fac3-6c60-4dc4-8798-541050a4940e&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.3.4&client-request-id=b702f219-5d98-408e-8881-db47494bb66f&response_mode=fragment')
        time.sleep(15)
        
        emailInput = self.browser.find_element(By.XPATH,'//*[@id="i0116"]')
        emailInput.send_keys(self.email)
        
        
        ileriButonu = self.browser.find_element(By.XPATH,'//*[@id="idSIButton9"]')
        ileriButonu.send_keys(Keys.ENTER)
        
        time.sleep(10)
        
        
        passwordInput = self.browser.find_element(By.XPATH,'//*[@id="i0118"]')  
        passwordInput.send_keys(self.password)
        
        oturumAcButonu = self.browser.find_element(By.XPATH,'//*[@id="idSIButton9"]')
        oturumAcButonu.send_keys(Keys.ENTER)
        
        time.sleep(10)
        
        oturumuzAcik_Kalsinmi = self.browser.find_element(By.XPATH,'//*[@id="declineButton"]')
        oturumuzAcik_Kalsinmi.send_keys(Keys.ENTER)
        
        time.sleep(20)
        
        
        tekrar_Email = self.browser.find_element(By.XPATH,'//*[@id="i0116"]')
        tekrar_Email.send_keys(self.email)
        
        time.sleep(20)
        
        
        ileriButonu = self.browser.find_element(By.XPATH,'//*[@id="idSIButton9"]')
        ileriButonu.send_keys(Keys.ENTER)
        
        
        
        time.sleep(20)
        input()
        
        
           
       

        # # Mouse'u hareket ettirme
        # action_chains = ActionChains(self.browser)
        # while True:
        #     action_chains.move_by_offset(50, 0).perform()
        #     time.sleep(1)
        #     action_chains.move_by_offset(-50, 0).perform()
        #     time.sleep(1)

        #     # Her 120 saniyede bir tekrar et
        #     time.sleep(120)
       
       
        
        
   

teams = Teams(email,password)
teams.signIn()





