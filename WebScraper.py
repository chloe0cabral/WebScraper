import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path = "/Users/chloecabral/Downloads/chromedriver 2")
driver.get("https://www.inc.com/lolly-daskal/100-motivational-quotes-that-will-inspire-you-to-succeed.html")
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for a in soup.findAll(attrs = "standardText"):
    quote = a.find("p")
    if quote not in results:
        results.append(quote.text)
        
df = pd.DataFrame({"Quote" : results})
df.to_csv("quotes.csv", index = False, encoding = "utf-8")