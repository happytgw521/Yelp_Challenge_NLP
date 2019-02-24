import pymongo
import json
from os import listdir
 
class MongoLoad:
	def __init__(self):
		# list files in directory
		self.file_list = []
		self.json_dir_dict = dict()

		#initiate pymongo
		self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")


	def __load_dataset(self, ds_name, ds_dir):
		
		myCollection = self.mydb[ds_name]

		# convert string file to list since yelp data is a list of sets	
		with open(ds_dir,'r') as raw_file:
			print(ds_dir)
			raw_list = raw_file.readlines()
		raw_file.close()

		# read out each record from string to json
		for i in range(0,len(raw_list)):
			try:
				json_item = json.loads(raw_list[i][:-1])
				myCollection.insert(json_item)
			except:
				# print error and jump
				print("ERROR:")
				print(raw_list[i])
				continue

		

	def execute(self, db_name, db_dir):
		# list files in directory
		file_list = listdir(db_dir)
		json_dir_dict = {x[:-5]: db_dir + "/" + x for x in file_list if '.json' in x}

		#initiate db
		self.mydb = self.myclient[db_name]

		for ds_name, ds_dir in json_dir_dict.items():
			print(ds_name, " is under process")
			self.__load_dataset(ds_name,ds_dir)
			print("Mission Complete")

		print("--------------------------DB Complete-------------------------")

		return 0

