from selenium import webdriver
import requests
import io
from PIL import Image
import os 

chrome_driver_path = "/Users/kazi/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

search_website = "https://pixabay.com/images/search/{query}"

format_search = search_website.format(query='Python')

driver.get(format_search)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

images = driver.find_elements_by_xpath("//div[@class='item']/a/img")

total_images = len(images)

print(total_images)

image_set = set()

for image in range(0, len(images)):

    current_image = images[image]

    if current_image.get_attribute("src") and "https" in current_image.get_attribute("src"):

        image_set.add(current_image.get_attribute("src"))

directory = "/Users/kazi/Downloads/"

for index, url in enumerate(image_set):

    print(url)

    file_name = str(index) + ".jpg"

    try:
        image_content = requests.get(url).content
    except Exception as e:
        print(f"Could not get url content of {url}")

    try:
        image_file = io.BytesIO(image_content)

        converted_image = Image.open(image_file).convert("RGB")

        path = os.path.join(directory, file_name)

        with open(path, "wb") as image_to_save:
            converted_image.save(image_to_save, "JPEG", quality=90)

    except Exception as e:
        print(f"Could not save {url}")
