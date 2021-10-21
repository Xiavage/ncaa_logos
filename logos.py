import os
import time
import urllib.request
from pathlib import Path
import pandas as pd
from selenium import webdriver

df = pd.read_csv('d1_colleges.csv')

def wait_for_element(driver, byType, byValue, maxWait: int):
    """
    This method, takes properties of an element and looks for the element in page.
    if the element is found, it will return the element else None is returned

    Args:
        driver ([webdriver]): [Selenium webdriver]
        byType ([By Type]): [Which property we are using to get element. ex: By.XPATH or BY.Id]
        byValue ([type]): [value of property]
        maxWait (int): [wait for element to be found]

    Returns:
        [webdriverelement]: [identified element]

    Taken from https://dev.to/dillir07/a-python-package-with-selenium-to-download-high-res-image-using-google-search-by-image-6ok

    """
    try:
        element = WebDriverWait(driver, maxWait).until(
            EC.presence_of_element_located((byType, byValue)))
        return element
    except TimeoutException:
        print("Element not found")
        return None

def google_search_logos(school):

    google_query = school + " logo"

    # print(google_query)

    #create or go to the logos path
    logo_path = Path(r'C:/Users/alber/Projects/sports_project/logos')
    # print(logo_path)
    if not os.path.exists(logo_path):
        print('logo directory created')
        os.mkdir(logo_path)

    #search for the logo
    google_base_url = "https://www.google.com/search?q=" + \
        google_query + "&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj7sb265vHsAhVEnq0KHVt5A30Q_AUoAXoECA4QAw&biw=1280&bih=610&dpr=1.5"

    #use selenium to find the logo on google using the google_query search
    # driver = webdriver.Firefox(executable_path=r"" + os.getcwd() + "\geckodriver-v0.27.0-win64\geckodriver.exe")
    driver = webdriver.Firefox(executable_path=r"geckodriver") 
    # browser = webdriver.Firefox()
    driver.get(google_base_url)
    #save the image using the source url
    college_logo = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img')
    college_logo.click()
    src = college_logo.get_attribute('src')
    #save the picture into a directory (logos)
    urllib.request.urlretrieve(src, logo_path)
    #close the webbrowser
    driver.close()

    # print(google_base_url)

# colleges = []
for row in df.itertuples():
    google_search_logos(row.Colleges)




# print("hello world")