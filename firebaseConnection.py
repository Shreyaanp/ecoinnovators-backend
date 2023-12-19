import pandas as pd
import firebase_admin
from firebase_admin import db, credentials

key_location = "./sih-backend-key.json"
firebase_url = "https://sih-ecoinnovators-default-rtdb.firebaseio.com/"

cred = credentials.Certificate(key_location)
firebase_admin.initialize_app(cred, {'databaseURL': firebase_url})

def dump_to_local(dataName: str, targetFile: str):
	sync = db.reference()
	data = sync.get()[dataName]

	data_df = pd.DataFrame(data, columns = data[0].keys())

	data_df.to_csv(targetFile, index = False)

	print("Data dumped from " + dataName)


def sync_update_remote(dataName: str, localCsv: str):
	sync = db.reference(dataName)
	data = pd.read_csv(localCsv)

	data_dict = data.to_dict(orient = 'records')
	existing = sync.get()[dataName]
	
	existing.extend(data_dict)

	print(existing)
	sync.set(existing)
	print(dataName + " data updated in Firebase app")


def first_update_remote(dataName: str, localCsv: str):
	sync = db.reference(dataName)
	data = pd.read_csv(localCsv)
	data_dict = data.to_dict(orient = 'records')

	sync.set(data_dict)
	print(dataName + " data uploaded to Firebase app")


import argparse
parser = argparse.ArgumentParser(
	description = "Firebase connectivity handler"
)
parser.add_argument(
	'remote_name',
	type = str,
	help = "Remote Data Name"
)
parser.add_argument(
	'local_name',
	type = str,
	help = "Local File name"
)

group = parser.add_mutually_exclusive_group(required = True)
group.add_argument(
	'-f', '--first',
	action = "store_true",
	help = "Insert data for the first time"
)
group.add_argument(
	'-u', '--update',
	action = "store_true",
	help = "Insert data to remote as append"
)
group.add_argument(
	'-d', '--dump',
	action = "store_true",
	help = "Dump data from remote to local csv"
)

args = parser.parse_args()

if args.first:
	first_update_remote(args.remote_name, args.local_name)
elif args.update:
	sync_update_remote(args.remote_name, args.local_name)
elif args.dump:
	dump_to_local(args.remote_name, args.local_name)