from selenium import webdriver

chrome_driver_path = "/Users/kazi/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

search_website = "https://pixabay.com/images/search/{query}"

format_search = search_website.format(query='python')

driver.get(format_search)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

images = driver.find_elements_by_xpath("//div[@class='item']/a/img")

total_images = len(images)

print(total_images)
