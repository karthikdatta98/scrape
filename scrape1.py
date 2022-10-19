import os
from time import sleep
import wget
import base64
from selenium import webdriver
# from selenium import By
from selenium.webdriver.common.by import By
import urllib
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# driver.find_element(By.CLASS_NAME, "content")
DRIVER_PATH = '/Users/kedi/Downloads/chromedriver'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
CURRENT_DIR = os.getcwd()
from tqdm import tqdm


def get_driver(download_dir=None):
    if download_dir is None:
        download_dir = os.path.join(CURRENT_DIR, 'data')
    link1 = '/Users/kedi/Downloads/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
      "download.default_directory": download_dir,
      "download.prompt_for_download": False,
      "download.directory_upgrade": True,
      "safebrowsing.enabled": True,
      "plugins.always_open_pdf_externally": True
    })
    options.add_argument("--disable-extensions")
    options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options=options, executable_path=link1)
    return driver


driver = get_driver()


import urllib.request
def download_file(name,url,folder_name=None):
    print(f"Downloading {name} ...")
    if folder_name is not None:
        final_directory = os.path.join(os.getcwd(),folder_name)
        print(final_directory)
        # if not os.path.exists(final_directory):
        #     os.makedirs(final_directory)
        # opener = urllib.request.build_opener()
        # opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        # urllib.request.install_opener(opener)   
        # driver = get_driver(f"{final_directory}/{folder_name}")
        driver.get(url)     
        # checkbox = driver.find_elements_by_xpath('//*[@id="recaptcha-anchor"]')
        # if not checkbox.isSelected():
        #     print ('Checkbox is selected')

        

        # urllib.request.urlretrieve(url, f"{final_directory}/{name}")
def  main():
    # url = "https://www.statista.com/download/{}"
    url = "https://www-statista-com.ezproxy.cul.columbia.edu/download/{}"
    formats = ["xlsx","png"]

    # pageid = 297955
    for pageid in tqdm(range(565500,585173)):
        for format in formats:
            data = f"1664398992##579517##{pageid}##1##{format}##Statistic"
            b64_data = base64.b64encode(data.encode())
            toDown = url.format(b64_data.decode())
            print(toDown)
            download_file(f"{pageid}.{format}",toDown,str(pageid))
            WebDriverWait(driver, 30)
            sleep(6)
            
            

    # wget.download(url)
             
if __name__ == "__main__" :
    main()