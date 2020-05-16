from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def getSong(songName):
    # disable notifications
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    opt.add_experimental_option("prefs",{"profile.default_content_setting_values.notfications":2})
    # initialize webdriver and set the options for browser
    browser = webdriver.Chrome('/Users/macbookair/Desktop/chromedriver', chrome_options=opt)
    browser.get('http://youtube.com')
    yt_searchBox = browser.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
    yt_searchButton = browser.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
    yt_searchBox.send_keys(songName)
    yt_searchButton.click()
    first_video = browser.find_element(By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img')
    first_video.click()
    # get the current url from the browser
    current_url = browser.current_url
    print('current url',current_url)
    # open new browser window
    browser.execute_script("window.open('')")
    browser.switch_to_window(browser.window_handles[1])
    browser.get('http://ytmp3.cc')
    # initialize click events
    yt_songUrl = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/form/input[1]')
    yt_songUrlConvert = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/form/input[2]')
    yt_songDownlaod = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[3]/a[1]')))
    # yt_songDownlaod = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[1]')
    # paste url from youtube to ytmp3
    yt_songUrl.send_keys(current_url)
    yt_songUrlConvert.click()
    yt_songDownlaod.click()
    # browser.implicitly_wait(10)
    # ActionChains(browser).move_to_element(yt_songDownlaod).click().perform()
    print(songName, ' is being downloaded!')



song = str(raw_input("Enter song name: "))

getSong(song)

    #created by: Siyanda Zama 
    #date 16/05/20
