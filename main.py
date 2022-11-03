import time
from selenium import webdriver

def main():
  options = webdriver.ChromeOptions()
  options.add_argument('--ignore-certificate-errors')
  options.add_argument('--incognito')
  options.add_argument('--headless')
  driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)
  

if __name__ == "__main__":
  main()