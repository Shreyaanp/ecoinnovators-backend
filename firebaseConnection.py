import pandas as pd
import firebase_admin
from firebase_admin import db, credentials

key_location = "./sih-backend-key.json"
firebase_url = "https://sih-ecoinnovators-default-rtdb.firebaseio.com/"

cred = credentials.Certificate(key_location)
firebase_admin.initialize_app(cred, {'databaseURL': firebase_url})

def sync_update_local(dataName: str):
	sync = db.reference()
	data = sync.get()


	print("Data dumped to Sync Data")


def sync_update_remote(dataName: str, localCsv: str):
	sync = db.reference(dataName)
	data = pd.read_csv(localCsv)

	data_dict = data.to_dict(orient = 'records')
	existing = sync.get(dataName)
	


def first_update_remote(dataName: str, localCsv: str):
	sync = db.reference(dataName)
	data = pd.read_csv(localCsv)
	data_dict = data.to_dict(orient = 'records')

	sync.set(data_dict)
	print(dataName + " data uploaded to Firebase app")


first_update_remote("EnergyData", "Data/energy_data.csv")
first_update_remote("ImportData", "Data/import_data.csv")
first_update_remote("ExportData", "Data/export_data.csv")
