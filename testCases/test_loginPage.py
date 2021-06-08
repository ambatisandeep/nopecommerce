import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilites.readProperties import Readconfiq
from utilites.logger import LogGen

class Test_001_Login:
    baseUrl = Readconfiq.getUrl()
    userName = Readconfiq.getUseremail()
    password = Readconfiq.getPassword()

    def test_homePage_title(self,setup):
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        actual_title = self.driver.title
        self.driver.close()
        if actual_title=="Your store. Login":
            assert  True
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png")
            assert False

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
        self.driver.quit()
        if act_title=="Dashboard / nopCommerce administration":
            assert True
        else:
            assert False




