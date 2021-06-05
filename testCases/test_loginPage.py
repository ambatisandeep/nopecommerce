import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage


class Test_001_Login:
    baseUrl="https://admin-demo.nopcommerce.com/"
    userName="admin@yourstore.com"
    password="admin"

    def test_homePage_title(self,setup):
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        actual_title = self.driver.title
        self.driver.close()
        if actual_title=="Your store. Login":
            assert  True
        else:
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




