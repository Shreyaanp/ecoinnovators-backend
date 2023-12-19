import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

def download_file(url, folder_path):
    response = requests.get(url, stream=True)
    file_name = url.split("/")[-1]

    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)

    print(f"Downloaded: {file_name}")

def scrape_and_download_data(url, folder_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a', href=True):
        file_url = urljoin(url, link['href'])
        download_file(file_url, folder_path)

if __name__ == "main":
    # Replace 'YOUR_URL' with the actual URL of the dataset page
    dataset_url = 'https://data.world/nz-stats-nz/dabe5fa6-a03f-4e46-8951-5c955f68f426'
    
    # Replace 'YOUR_LOCAL_FOLDER_PATH' with the folder where you want to save the downloaded files
    local_folder_path = 'Scraped/'

    # Create the folder if it doesn't exist
    os.makedirs(local_folder_path, exist_ok=True)

    scrape_and_download_data(dataset_url, local_folder_path)