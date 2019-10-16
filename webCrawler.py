import re
from bs4 import BeautifulSoup
from selenium import webdriver

def extractLinks(fileToWrite, html, numOfTabs):
	tabsToIndent = ""

	for tab in range(0, numOfTabs):
		tabsToIndent+="\t"

	for link in html.find_all("a"):
		url = link.get('href')
		if url == "#":
			continue
		else:
			fileToWrite.write(tabsToIndent)
			fileToWrite.write(str(url) + "\n")

url = 'https://www.sportchek.ca'
driver = webdriver.PhantomJS()
driver.get(url)
data = driver.find_element_by_tag_name('html').get_attribute('innerHTML')
file = open("RESULTS.txt", "w")
soup = BeautifulSoup(data, features="html.parser")

# Title of the home page
title = soup.find('title')
file.write("Title: " + title.getText()+"\n")

# navigating through the nav bar top categories
for element in soup.find_all("div", {"class":"page-nav__flyout"}):
	nameOfCat = element.get('data-flyout-key')
	file.write("\tSub-category: "+nameOfCat+"\n")
	div = element # we do this step so that we can get the last drop down category to get a product list page

# file.write("\tAll urls in the page: \n")
# extractLinks(file, soup, 2)

# Here we find the first product list page
ulOfNav = div.find('ul', class_ = "page-nav__list")
firstHref = ulOfNav.find('a')
firstHref = firstHref.get('href')

# Product list page retrieval
productListPageUrl = url+firstHref
driver.get(productListPageUrl)
productListData = driver.find_element_by_tag_name('html').get_attribute('innerHTML')
soup = BeautifulSoup(productListData, features="html.parser")

# This is the ul item which holds all the product li items
ul = soup.find("ul", {"class" : ["product-grid__list", "product-grid__list_quickview"]})
		

# THIS LOOP IS TO GET TO THE PRODUCT PAGE OF EACH PRODUCT IN THE UL
for li in ul.find_all("li", {"class" : ["product-grid__list-item", "product-grid__list-item_state_comparable "]}):
	file.write("\n\n")

	# Getting the product page url
	productLink = li.find('a').get('href')
	productPageUrl = url+productLink
	driver.get(productPageUrl)
	productData = driver.find_element_by_tag_name('html').get_attribute('innerHTML')
	soup = BeautifulSoup(productData, features="html.parser")
	numOfTabs = 0

	# Title of product poag
	productPageTitle = soup.find('title').getText()
	file.write("Title: "+productPageTitle+"\n")
	numOfTabs+=1

	# Finding the breadcrumb to find the categories, and sub-categories
	breadcrumb = soup.find("div", class_ = "page-breadcrumb__list")
	currentCategoryLevel = 0

	for category in breadcrumb.find_all("a"):
		currentString = "Sub-category: "
		if currentCategoryLevel == 0:
			currentCategoryLevel += 1
			continue

		if currentCategoryLevel == 1:
			currentString = "Category: "

		for x in range(0, numOfTabs):
			file.write("\t")

		file.write(currentString + category.getText().strip() + "\n")
		numOfTabs += 1
		currentCategoryLevel += 1

	numOfTabs += 1
	# Finding name of the product
	titleDiv = soup.find("div", class_ = "product-detail__title")
	productName = titleDiv.find('h1', class_ = "global-page-header__title").getText()
	
	# Finding the product number
	productNumber = soup.find('em', class_ = "product-detail__description-item-num").getText()
	tempProdNum = re.search(".*#: ([0-9]*)", productNumber)
	if tempProdNum:
		productNumber = tempProdNum.group(1)
	
	# Finding the model number
	tempModelNum = soup.find_all("div", class_ = "product-description__content")
	tempModelNum = tempModelNum[2]
	tempModelNum = tempModelNum.find("ul")
	tempModelNum = tempModelNum.find("li").getText()
	tempModelNum = re.search(".*: (.*)", tempModelNum)
	if tempModelNum:
		modelNum = tempModelNum.group(1)
	
	tabsToIndent = ""
	for x in range(1, numOfTabs):
		tabsToIndent += "\t"
	file.write(tabsToIndent + "Product name: " + productName +"\n")
	file.write(tabsToIndent + "Product product num: " + productNumber +"\n")
	file.write(tabsToIndent + "Product model num: " + modelNum +"\n")
	file.write(tabsToIndent + "Product page url: " + productPageUrl +"\n")
	# file.write(tabsToIndent + "All urls in this page: \n")
	# extractLinks(file, soup, numOfTabs)

file.close()
