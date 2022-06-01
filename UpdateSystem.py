import requests
import sqlite3
from git import Repo
import os
import shutil
import glob
import pip
import pwd

val = requests.get("https://raw.githubusercontent.com/Numbers-Technologies/Gorgona/update_system/VERSION")
val = val.text.replace("\n", "")


class WWD:
	def __init__(self):
		pass
	
	def __initialize(self):
		self.sqlite_connection = sqlite3.connect(f"/home/{pwd.getpwuid(os.getuid()).pw_name}/.config/Gorgona/settings.db")
		self.cursor = self.sqlite_connection.cursor()
	
	def get_version_from_db(self):
		try:
			self.__initialize()
			self.cursor.execute("select * from test;")
			record = self.cursor.fetchall()
			self.cursor.close()
			return record[0][0]
		except:
			return "None"

	def set_new_version(self,vers):
		try:
			self.__initialize()
			self.cursor.execute(f"update test set version = '{vers}'")
			self.sqlite_connection.commit()
		except:
			pass

	def create_new_database(self, vers):
		os.mkdir(f"/home/{pwd.getpwuid(os.getuid()).pw_name}/.config/Gorgona/")
		self.__initialize()
		self.cursor.execute("create table test (version String)")
		self.cursor.execute(f"insert into test (version) VALUES ('{vers}')")
		self.sqlite_connection.commit()

def install_package(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


def update():
	try:
		files = glob.glob("main/*")
		shutil.rmtree('main')
	except:
		pass
	WWD().set_new_version(val)
	Repo.clone_from("https://github.com/Numbers-Technologies/Gorgona.git", "main", branch="AVX-notSupported")
	

def install():
	count = 0
	print("Start installing")
	WWD().create_new_database(val)
	update()
	packages = []
	with open("main/requirements.txt", "r") as file:
		for line in file:
			packages.append(line.replace("\n",""))
	for package in packages:
		print(f"{count}-{package}")
		install_package(package)



def main():
	new_version = val
	current_version = WWD().get_version_from_db()
	if current_version == "None":
		print("Installing")
		install()

	elif current_version != new_version:
		print("Updating")
		update()
	
	else:
		print("Nothing update")
main()
