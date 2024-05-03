import logging

from selenium import webdriver
from selenium.webdriver.common.by import By

DRIVER = webdriver.Chrome()

def downloadHWMonitor():
    url = "https://www.cpuid.com/softwares/hwmonitor.html"
    DRIVER.get(url)
    items = DRIVER.find_elements(By.CSS_SELECTOR, ".button.icon-zip")
    if len(items) == 0:
        logging.log(logging.ERROR, "Found 0 elements with the used selector on the page.")
        return


    hasZIPTextList = [item for item in items if "ZIP" in item.text]
    if len(hasZIPTextList) == 0:
        logging.log(logging.ERROR, "Element found does not have the desired text.")
        return

    print(hasZIPTextList)
    print("SUCCESS")

if __name__ == "__main__":
    hwmonitorResult = downloadHWMonitor()