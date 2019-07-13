from bs4 import BeautifulSoup
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import requests
import pandas as pd
import os
import pymongo
import time

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)



def scrape():
    mars_data = {}
    mars_hem_img_urls = []
    browser = init_browser()
    url_1 = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest."
    browser.visit(url_1)
    html = browser.html 
    soup_1 = BeautifulSoup(html, 'html.parser')

    
    news_title = soup_1.find("div", class_="content_title").text
    news_p = soup_1.find("div", class_="rollover_description_inner").text


    mars_data['news_title'] = news_title
    mars_data['news_paragraph'] = news_p




    url_2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_2)
    html = browser.html
    soup_2 = BeautifulSoup(html, 'html.parser')

    images = []
    mars_images = soup_2.find_all('a', class_="fancybox")
    for mars_image in mars_images:
        mars_photo = mars_image['data-fancybox-href']
        images.append(mars_photo)

    featured_image_url = 'https://www.jpl.nasa.gov' + mars_photo
    featured_image_url


    mars_data['featured_image_url'] = featured_image_url




    url_3 = ('https://twitter.com/marswxreport?lang=en')
    browser.visit(url_3)
    html = browser.html
    soup_3 = BeautifulSoup(html, 'html.parser')


    mars_w = soup_3.find_all("div", class_="js-tweet-text-container")
    for weather in mars_w:
        mars_weather = weather.find('p').text
        if "Sol" in mars_weather:
            break
        else:
            pass


    mars_data['weather'] = mars_weather



    url_4 = "https://space-facts.com/mars/"


    mars_facts_table = pd.read_html(url_4)
    mars_facts_table[0]


    mars_facts_data = mars_facts_table[0]
    mars_facts_data.columns = ["Facts", "Mars", "Earth"]
    mars_facts_df = mars_facts_data.set_index(["Facts"])
    mars_facts_df


    mars_facts_html = mars_facts_df.to_html()
    mars_facts_html = mars_facts_html.replace("\n","")
    mars_facts_html


    mars_data['mars_facts'] = mars_facts_html

 
 
    url_5 = ("https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced")
    browser.visit(url_5)
    html = browser.html
    soup_5 = BeautifulSoup(html, 'html.parser')

    cerberus = soup_5.find_all('div', class_="wide-image-wrapper")
    for img in cerberus:
        image_1 = img.find('li')
        img_url_1 = image_1.find('a')['href']
    cerberus_title = soup_5.find('h2', class_='title').text
    cerberus_hem = {"title": cerberus_title, "img_url": img_url_1}
    mars_hem_img_urls.append(cerberus_hem)
    mars_data['mars_hem_img_urls'] = mars_hem_img_urls



    url_6 = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced')
    browser.visit(url_6)
    html = browser.html
    soup_6 = BeautifulSoup(html, 'html.parser')

    shiaparelli = soup_6.find_all('div', class_="wide-image-wrapper")
    for img in shiaparelli:
        image_2 = img.find('li')
        img_url_2 = image_2.find('a')['href']
    shiaparelli_title = soup_6.find('h2', class_='title').text
    shiaparelli_hem = {"title": shiaparelli_title, "img_url": img_url_2}
    mars_hem_img_urls.append(shiaparelli_hem)
    mars_data['mars_hem_img_urls'] = mars_hem_img_urls



    url_7 = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced')
    browser.visit(url_7)
    html = browser.html
    soup_7 = BeautifulSoup(html, 'html.parser')

    syrtris = soup_7.find_all('div', class_="wide-image-wrapper")
    for img in syrtris:
        image_3 = img.find('li')
        img_url_3 = image_3.find('a')['href']
    syrtris_title = soup_7.find('h2', class_='title').text
    syrtris_hem = {"title": syrtris_title, "img_url": img_url_3}
    mars_hem_img_urls.append(syrtris_hem)
    mars_data['mars_hem_img_urls'] = mars_hem_img_urls



    url_8 = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced')
    browser.visit(url_8)
    html = browser.html
    soup_8 = BeautifulSoup(html, 'html.parser')

    valles_marineris = soup_8.find_all('div', class_="wide-image-wrapper")
    for img in valles_marineris:
        image_4 = img.find('li')
        img_url_4 = image_4.find('a')['href']
    valles_marineris_title = soup_8.find('h2', class_='title').text
    valles_marineris_hem = {"title": valles_marineris_title, "img_url": img_url_4}
    mars_hem_img_urls.append(valles_marineris_hem)
    mars_data['mars_hem_img_urls'] = mars_hem_img_urls

    browser.quit()
    return mars_data
    

    





# def scrape_mars_hem():
#     browser = init_browser()
#     mars_hem_img_urls = []
#     ceberus = scrape_mars_cerberus()
#     shiaparelli = scrape_mars_shiaparelli()
#     syrtris = scrape_mars_syrtris()
#     valles_marineris = scrape_mars_valles_marineris()
#     mars_hem_img_urls.append(ceberus)
#     mars_hem_img_urls.append(shiaparelli)
#     mars_hem_img_urls.append(syrtris)
#     mars_hem_img_urls.append(valles_marineris)
#     mars_data['mars_hemisphere_img_urls'] = mars_hem_img_urls
#     return mars_data