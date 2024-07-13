import pytest
from selenium import webdriver
from util import config
from selenium.webdriver.chrome.options import Options

driver = None


@pytest.fixture()
def setUp():
    global driver
    browser_choice=config.browser_name
    if driver == None:
        driver = webdriver.Chrome(config.driver_path)

    elif(browser_choice=="headless_chrome"):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(config.driver_path,options=chrome_options)
    else:
        driver = webdriver.firefox(config.otherDriver_path)


    driver.get(config.url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


@pytest.fixture(scope="module")
def teardown():
    yield
    driver.close()
    driver.quit()






