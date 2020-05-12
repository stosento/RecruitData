from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
import requests
import time
import csv

def main():

	# Instantiate the driver
	driver = open_driver()

	csv_data = ''
	first = True

	# Find the next button
	while driver.find_elements_by_class_name('next'):
		print("printing to page")
		csv_data += append_data(driver, first)
		first = False

		driver.find_element_by_class_name('next').click()
		time.sleep(1)

	csv_data += append_data(driver, False)
	driver.close()

	write_file(csv_data)

def append_data(driver, first):
	# Grab the li class & hover
	li_element = WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(),'Share & more')]")))
	hover = ActionChains(driver).move_to_element(li_element)
	hover.perform()

	# Wait after the hover action
	driver.implicitly_wait(10)

	# Grab the button class & click
	button = driver.find_element(By.XPATH, "//button[contains(text(),'Get table as CSV (for Excel)')]");
	ActionChains(driver).move_to_element(button).click(button).perform()

	# Cycle through the page and grab the csv data
	html = driver.page_source.encode('utf-8')
	soup = bs(driver.page_source, 'html.parser')
	results = soup.find('pre', id='csv_results')

	raw_results = results.get_text()

	if (first):
		lines_to_skip = 2
	else:
		lines_to_skip = 3

	formatted = '\n'.join(raw_results.split('\n')[lines_to_skip:]) + '\n'
	data = str(formatted)

	return data

def open_driver():
	driver = webdriver.Chrome()
	year_start = 2009
	year_end = 2020
	URL = 'https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min={0}&year_max={1}&draft_slot_min=1&draft_slot_max=500&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&pos%5B%5D=e&pos%5B%5D=t&pos%5B%5D=g&pos%5B%5D=c&pos%5B%5D=ol&pos%5B%5D=dt&pos%5B%5D=de&pos%5B%5D=dl&pos%5B%5D=ilb&pos%5B%5D=olb&pos%5B%5D=lb&pos%5B%5D=cb&pos%5B%5D=s&pos%5B%5D=db&pos%5B%5D=k&pos%5B%5D=p&conference=any&show=all&order_by=default&order_by_asc=Y'.format(year_start, year_end)
	driver.get(URL)

	return driver

def write_file(data):
	draft_file = open("draft_data.csv", "w")
	draft_file.write(data)
	draft_file.close()

main()




