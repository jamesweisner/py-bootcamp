from time import sleep
from random import choice
from urllib3.exceptions import ProtocolError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import WebDriverException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url='https://onemillioncheckboxes.com/')

def check_batch(checkboxes):
	for checkbox in checkboxes:
		try:
			if not checkbox.is_selected():
				checkbox.click()
				sleep(0.2)
		except UnexpectedAlertPresentException:
			sleep(1.0) # Website told us to slow down.
		except ElementClickInterceptedException:
			continue  # Race condition in the user interface.
		except StaleElementReferenceException:
			return # Checkbox scrolled off the screen.
		except ProtocolError:
			return # User closed the window.

try:
	status = driver.find_element(By.TAG_NAME, 'p')
	while True:
		wait = WebDriverWait(driver, 10)
		selector = 'input[type="checkbox"]:not(:checked)'
		batch = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
		driver.execute_script(f"arguments[0].innerText = 'Checking {len(batch)} checkboxes...';", status)
		check_batch(batch)
		driver.execute_script(f"arguments[0].innerText = 'Looking for unchecked checkboxes...';", status)
		sleep(0.25)
except WebDriverException:
	pass # Computer went to sleep.
except NoSuchWindowException:
	pass # User closed the window.
except KeyboardInterrupt:
	pass # User is ending the program.

driver.quit()
