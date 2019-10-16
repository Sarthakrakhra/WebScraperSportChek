# Assignment 2 3172

This assignment involves the creation of a web scraper going through the sportchek website. The way this scraper works is by going through the navigation bar of the site and selects the first link in the last dropdown of that navigation bar. Next, it goes into each product in the product list page and takes our the product name, number, product model number, the categories and sub-categories of where the product is found and the product page's url.

Date created: 06 10 2019
Last modification date: 10 10 2019

## Authors
Name: **Sarthak Rakhra**<br />
Email: sarthak.rakhra@dal.ca

## Executing the file
To run the file there are a couple things which need to be installed first. 
### Prerequisites
```
pip install selenium
pip install phantomjs-binary
pip install bs4
pip install requests
```

To run the program ensure you have python 3 installed and run this command in the terminal:

```
python3 webCrawler.py
```
## Output
The output of the program will be available in the RESULTS.txt
The format of the file will have the first block of text containing the landing page of sportchek details. The order includes,<br/>
_Title of the page<br/>_
&nbsp;&nbsp;&nbsp;&nbsp;_Sub categories present in the navigation_

The next blocks of texts are the details for all the products in the first product list available in the last navigation dropdown sub-category
The details retrieved are part of the product page. They order includes,<br/>
_Title of the page_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;_Category_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Sub-category_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Sub-sub-category_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Product name_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Product number_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Product model number_<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Product page url_<br/>

If you want to see all the URLS available in each page scraped, please uncomment lines **37**, **38**, **119**, **120**
<br><br>
**MAKE SURE TO RUN THE FILE TWICE AS SPORTCHEK SOMETIMES DOES NOT LET THE CRAWLER SCRAPE THE PAGE DETAILS**
## References
Help was taken by referencing the Beautiful Soup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
