

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from util import config


# ---Test Case ->  User should be able to Perform functionalities on BT web page ---#
def test_validlogin(setUp,teardown):
    # Launch the application URL
    driver = setUp

    try:
        # Close the accept Cookie pop-up if it appears
        cookie_popup = driver.find_element(By.XPATH,"//*[contains(text(),'Accept all cookies')]")
        cookie_popup.click()
    except Exception as e:
        print("Cookie pop-up not found or closed")
    mobile_menu = driver.find_element(By.XPATH, "//*[@class='bt-navbar-screen-sm-main']//a//span[@class='bt-navbar-underline']")
    actions = ActionChains(driver)
    actions.move_to_element(mobile_menu).perform()
    mobile_phones = driver.find_element(By.XPATH, "//li[@class='bt-navbar-menu-col-20-percent']//li//a[contains(text(),'Mobile phones')]")
    mobile_phones.click()

    # Verify the number of banners present below "See Handset details" is not less than 3
    banners = driver.find_elements(By.XPATH, "//div[@class='flexpay_flexpaycard_container__GnRx9']")
    if len(banners) < 3:
        print("Error: Less than 3 banners found.")
    else:
        print(f"{len(banners)} banners found below 'See Handset details'.")

  # Scroll down and click View SIM only deals
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    view_sim_only_deals = driver.find_element(By.XPATH, "//*[@class='bt-btn bt-btn-primary']")
    view_sim_only_deals.click()

    # Validate the title for the new page
    expected_title = "SIM Only Deals | Compare SIMO Plans & Contracts | BT Mobile"
    if expected_title in driver.title:
        print(f"Page title validated: {driver.title}")
    else:
        print(f"Error: Page title does not match expected title '{expected_title}'.")

    # Validate "30% off and double data" for 125GB 250GB Essential Plan
    plan_info = driver.find_element(By.XPATH, "//*[@class='paragraph-md banner-ee-promo_description__O7XMK banner-ee-promo_description_margin__1jcB9']")
    if "125GB 250GB Essential Plan, was £27 £18.90 per month" in plan_info.text:
        print("Plan info validated.")
    else:
        print("Error: Plan info does not match expected text.")
    # Close the browser and exit
    driver = teardown
