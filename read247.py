from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import csv

year_list = range(2006,2018)
state_list = ['MI', 'OH']
driver = webdriver.Chrome()
recruits = []

for year in year_list:
	for state in state_list:
		URL = 'https://247sports.com/Season/%s-Football/CompositeRecruitRankings/?InstitutionGroup=highschool&State=%s' % (year, state)
		
		driver.get(URL)
		html = driver.page_source.encode('utf-8')

		btn_class = 'showmore_blk'
		while driver.find_elements_by_class_name(btn_class):
			driver.find_element_by_class_name(btn_class).click()
			time.sleep(1)

		soup = bs(driver.page_source, 'html.parser')
		results = soup.find_all('li', class_='rankings-page__list-item')

		for item in results:

			name = item.find('a', class_='rankings-page__name-link').text
			stars = len(item.find_all('span', class_='icon-starsolid yellow'))
			rank = item.find('span', class_='score').text

			recruits.append([state, year, name, stars, rank])

driver.close()

with open('recruit_data.csv', mode='w') as recruit_file:
	recruit_writer = csv.writer(recruit_file, delimiter=',')
	recruit_writer.writerow(['State','Year', 'Name', 'Stars', 'Rating'])
	for recruit in recruits:
		recruit_writer.writerow(recruit)
