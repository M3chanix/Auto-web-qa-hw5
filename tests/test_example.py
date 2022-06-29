import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw4.MainPage import MainPage
from hw4.CatalogPage import CatalogPage
from hw4.ProductPage import ProductPage
from hw4.AdminPage import AdminPage
from hw4.RegisterPage import RegisterPage


def test_main_page(driver):
    main_page = 'http://192.168.0.190:8081/'
    driver.get(main_page)
    driver.find_element(*MainPage.CURRENCY_SWITCH)

    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located(MainPage.SLIDE_PANNEL))

    driver.find_element(*MainPage.SUPPORT_PHONE)
    driver.find_element(*MainPage.CART_BUTTON)
    driver.find_element(*MainPage.FEATURED_LIST)


def test_catalog_page(driver):
    catalog_page = 'http://192.168.0.190:8081/laptop-notebook'
    driver.get(catalog_page)
    driver.find_element(*CatalogPage.BREADCRUMB)
    driver.find_element(*CatalogPage.PRODUCT_LIST)
    driver.find_element(*CatalogPage.FIRST_PRODUCT)
    driver.find_element(*CatalogPage.LIMIT_INPUT)
    driver.find_element(*CatalogPage.SORT_INPUT)

def test_product_page(driver):
    product_page = 'http://192.168.0.190:8081/laptop-notebook/hp-lp3065'
    driver.get(product_page)
    driver.find_element(*ProductPage.PRICE)
    driver.find_element(*ProductPage.WISHLIST_BUTTON)
    driver.find_element(*ProductPage.THUMBNAIL)
    driver.find_element(*ProductPage.ADD_CART_BUTTON)
    
    wait = WebDriverWait(driver, 2)
    wait.until(EC.visibility_of_element_located(ProductPage.RATING_STARS))

def test_admin_page(driver):
    admin_page = 'http://192.168.0.190:8081/admin'
    driver.get(admin_page)
    driver.find_element(*AdminPage.NAVBAR_IMAGE)
    driver.find_element(*AdminPage.USERNAME_INPUT)
    driver.find_element(*AdminPage.PASSWORD_INPUT)
    driver.find_element(*AdminPage.FORGOT_LINK)
    driver.find_element(*AdminPage.LOGIN_BUTTON)
    

def test_register_page(driver):
    register_page = 'http://192.168.0.190:8081/index.php?route=account/register'
    driver.get(register_page)
    driver.find_element(*RegisterPage.FIRST_NAME_INPUT)
    driver.find_element(*RegisterPage.LOGIN_PAGE_LINK)
    driver.find_element(*RegisterPage.PASSWORD_INPUT)
    driver.find_element(*RegisterPage.SUBSCRIBE_YES_CHECKBOX)
    driver.find_element(*RegisterPage.CONTINUE_BUTTON)


