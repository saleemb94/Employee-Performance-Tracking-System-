#this file parses the data in the .ini file and returns it to the main.py 
#to complete the connection with the database

from configparser import ConfigParser

def config(filename = "database.ini", section= "postgresql"):
	#create a parser
	parser = ConfigParser()
	#read the config file
	parser.read(filename)
	db = {} #creating an empty dictionary
	if parser.has_section(section):
		params = parser.items(section)  
		#assigning the items in the .ini file into the dictionary
		for param in params: 			
			db[param[0]] = param[1]
	else:								
		raise Exception('Section {0} is not found in the {1} file.'.format(section,filename))	 	
	return db
