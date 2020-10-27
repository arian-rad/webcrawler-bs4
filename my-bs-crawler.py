import requests
import csv
import json
from bs4 import BeautifulSoup

user_url = input("Enter a valid website url: ")

result = requests.get(user_url)  # using get function to get access to the web page
print("Status:", result.status_code)  # checking if the response is OK.
# The 200 (k) output indicates that the web page is available

page_src = result.content  # Assigning the source of the page to page_src
my_soup = BeautifulSoup(page_src, 'html.parser')  # Creating an instance of BeautifulSoup Class named my_soup

# opening(creating) a csv file called scraped-a-tags.csv to store a tag links
csv_file_a_tags = open('scraped-a-tags.csv', 'w')
a_writer = csv.writer(csv_file_a_tags)

a_tags = my_soup.find_all("a")
a_href_content = []
# The loop below extracts only the links
for tag in a_tags:
    if "https:" in tag.attrs['href'] or "http:" in tag.attrs['href']:
        a_href_content.append(tag.attrs['href'])
        a_writer.writerow(a_href_content)  # Writing in to a csv file

# opening(creating) a json file called scraped-a-tags.json to store a tag links in a json file
with open("scraped-a-tags.json", "w") as writeJSON:
    json.dump(a_href_content, writeJSON, ensure_ascii=False)

# opening(creating) a csv file called scraped-p-tags.csv to store p tags
csv_file_p_tags = open('scraped-p-tags.csv', 'w')
p_writer = csv.writer(csv_file_p_tags)

p_tags = my_soup.find_all('p')
p_tags_text = []
# The loop below extracts the text between each p tag
for p in p_tags:
    p_tags_text.append(p.text)
    p_writer.writerow(p_tags_text)

# opening(creating) a json file called scraped-p-tags.json to store p tags in a json file
with open("scraped-p-tags.json", "w") as writeJSON:
    json.dump(p_tags_text, writeJSON, ensure_ascii=False)

# opening(creating) a csv file called scraped-img-links.csv to store img links
csv_file_img_links = open('scraped-img-links.csv', 'w')
img_writer = csv.writer(csv_file_img_links)

img_src = my_soup.find_all('img')
img_src_links = []
# The loop below extracts the links for all images in the page
for img in img_src:
    img_src_links.append(img.attrs['src'])
    img_writer.writerow(img_src_links)

# opening(creating) a json file called scrape-img-links.json to store img links in a json file
with open("scraped-img-links.json", "w") as writeJSON:
    json.dump(img_src_links, writeJSON, ensure_ascii=False)

# Closing all opened files
csv_file_a_tags.close()
csv_file_p_tags.closed
csv_file_img_links.close()
writeJSON.close()
