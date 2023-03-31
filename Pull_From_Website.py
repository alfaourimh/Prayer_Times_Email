from selenium import webdriver

def print_athan():
    driver = webdriver.Chrome()
    driver.get('https://www.islamicfinder.org/')

    element = driver.find_element_by_css_selector('#main-column > div:nth-child(7) > div > div > div.testscrollable.m-b-sm > fieldset')
    global etxt
    etxt = element.text
    return print_athan
print_athan()

today = etxt[0:15] #today this week
fajr = etxt[15:30] #fajr
sunrise = etxt[30:47] #sunrise
dhuhr = etxt[47:61] #dhuhr
asr = etxt[61:74] #asr
maghrib = etxt[74:91] #maghrib
isha = etxt[91:105] #isha
