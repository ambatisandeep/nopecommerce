import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilites.readProperties import Readconfiq
from utilites.logger import LogGen

class Test_001_Login:
    baseUrl = Readconfiq.getUrl()
    userName = Readconfiq.getUseremail()
    password = Readconfiq.getPassword()
    logger=LogGen.loggen()

    def test_homePage_title(self,setup):
        self.logger.info("*************** Test_001_Login *************** \n " + "*************** Verifying Home Page ***************")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        actual_title = self.driver.title
        self.driver.close()
        if actual_title=="Your store. Login":
            assert  True
            self.logger.info("*************** Home Page Test Passed *************** ")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png")
            assert False
            self.logger.error("*************** Home Page Test Failed *************** ")

    def test_Login(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        lp=LoginPage(self.driver)
        lp.setUserName(self.userName)
        lp.setPassword(self.password)
        lp.clickLogin()
        act_title=self.driver.title
        lp.logout()
        if act_title=="Dashboard / nopCommerce administration":
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False





