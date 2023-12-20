import requests
import os

url_root = "https://api.data.gov.in"
urls = [
	"/resource/8b75d7c2-814b-4eb2-9698-c96d69e5f128",
	"/resource/7932c3ed-c88d-4e0c-bc39-17e3e3170483",
	"/resource/8d3b6596-b09e-4077-aebf-425193185a5b",
	"/resource/352b3616-9d3d-42e5-80af-7d21a2a53fab",
	"/resource/7932c3ed-c88d-4e0c-bc39-17e3e3170483",
	"/resource/8d3b6596-b09e-4077-aebf-425193185a5b",
	"/resource/7b624b4a-1456-4945-80d0-dfb5e40ddcff"
]
params = {
	'api-key': '579b464db66ec23bdd000001e874bf7fa22e458e75a0a9a5a021d600',
	'format': 'csv',
	'limit': '100'
}
fname_param = {
	'api-key': '579b464db66ec23bdd000001e874bf7fa22e458e75a0a9a5a021d600',
	'format': 'json',
	'limit': '1'
}

api_url_pair = {
	
}
local_folder_path = 'Scraped/'

def download_file(url, folder_path):
	response = requests.get(url, params = params)
	fnameres = requests.get(url, params = fname_param)

	if response.status_code == 200 and fnameres.status_code == 200:
		file_name = fnameres.json()["title"] + ".csv"

		file_path = os.path.join(folder_path, file_name)

		with open(file_path, 'wb') as file:
			for chunk in response.iter_content(chunk_size=128):
				file.write(chunk)

		print(f"Downloaded: {file_name}")
		return
	print("Something went wrong")

# Create the folder if it doesn't exist
os.makedirs(local_folder_path, exist_ok=True)
for url in urls:
	dataset_url = url_root + url
	download_file(dataset_url, local_folder_path)