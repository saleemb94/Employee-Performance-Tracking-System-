import main
from prettytable import PrettyTable



def Installation(serial_num,model,delivery_date,installation_date,warranty_duration,installation_loc,customer_id,tender_id,): #installation info
	
	"""serial_num ="7C361K101"
	model = "EG-600WR"
	delivery_date='2020-03-01'
	installation_date='2020-07-01'
	warranty_duration=""
	customer_id =200
	tender_id = "EN620"
	installation_loc ="Al Karak" """

	data = (
	["serial_num",serial_num],
	["model",model],
	["delivery_date",delivery_date],
	["installation_date",installation_date],
	["warranty_duration",warranty_duration],
	["installation_loc",installation_loc],
	["customer_id",customer_id],
	["tender_id",tender_id]
	

	)

	IN = main.insert_Installation(data)
	if IN is None:
		return IN
	else:
		return IN

def Employee(emp_id,first_name,last_name,target): #Employee information
	"""
		emp_id = 15647
		first_name = "Alia"
		last_name = "Mahmoud"
		target = 0 				"""

	data = (
	["emp_id",emp_id],
	["first_name",first_name],
	["last_name",last_name],
	["target",target]
	)
	E = main.insert_Employee(data)
	if E is None:
		return E
	else:
		return E

def customer(customer_id,customer_name,customer_loc): #customer info
	
	customer_id = customer_id
	customer_name = customer_name
	customer_loc = customer_loc


	data = (
	["customer_id",customer_id],
	["customer_name",customer_name],
	["customer_loc",customer_loc]
	)

	C = main.insert_Customer(data)
	
	if C is None:
		return C
	else:
		return C	

def managed_by(customer_id,emp_id): #customer managed by employee
	customer_id = customer_id
	emp_id = emp_id

	data = (
	["customer_id",customer_id],
	["emp_id",emp_id]

	)
	#print('ADDED')
	MB = main.insert_ManagedBy(data)
	if MB is None:
		return MB
	else:
		return MB

def Won(tender_id):
	tender_id = tender_id
	data = (
	["tender_id",tender_id],

	)

	W = main.insert_Won(data)
	
	if W is None:
		return W
	else:
		return W	

def Lost(tender_id,winning_company): #lost tenders
	tender_id = tender_id
	winning_company =winning_company
	data = (
	["tender_id",tender_id],
	["winning_company",winning_company]

	)

	L = main.insert_Lost(data)
	if L is None:
		return L
	else:
		return L

def item(item_id,item_name,item_price): #item information
	item_id = item_id
	item_name = item_name
	item_price = item_price
	data = (
	["item_id",item_id],
	["item_name",item_name],
	["item_price",item_price]

	)

	IT = main.insert_Item(data)
	#print(IT)
	if IT is None:
		return IT
	else:
		return IT

def Offered_in(tender_id,item_id): #item offered in tenders
	item_id = item_id
	tender_id = tender_id
	data = (
	["tender_id",tender_id],
	["item_id",item_id]
	)
	
	OI = main.insert_OfferedIn(data)
	if OI is None:
		return OI
	else:
		return OI

#tender info
def Tender(tender_id,tender_title,announced_in,submitted_in,customer_id,emp_id): 
	tender_id = tender_id
	tender_title = tender_title
	announced_in = announced_in
	submitted_in = submitted_in
	customer_id = customer_id
	emp_id = emp_id

	data = (
	["tender_id",tender_id],
	["tender_title",tender_title],
	["announced_in",announced_in],
	["submitted_in",submitted_in],
	["customer_id",customer_id],
	["emp_id",emp_id]

	)
	T = main.insert_Tender(data)

	if T is None:
		return T
	else:
		return T

def updateQuery(selected_table,update_att,update_val,ref_att,ref_val):

	selected_table1 = selected_table
	
	data = (
	[update_att,update_att]

	)

	reference_att = (
		[ref_att,ref_val]

		)
	main.update(selected_table1,data,reference_att)

def deleteQuery(selected_table,attribute,Value):
	selected_table1 = selected_table
	
	a=0
	try:
		Value = int(Value)
	except:
		a=1

	
	data = (
	[attribute,Value]

	)

	


	D = main.delete(selected_table1,data,a)
	if D is None:
		return D
	else:
		return D

def showTenderTable(SelectedTable):
 #print("printing tenders table .....")
 columnData = tuple(main.get_allTenders(SelectedTable))

 if SelectedTable == "all":

 	headings = ["Tender id","Tender Title","Offered Item","Announced in","Submitted in","Customer Name","Worked By"]
 	#TendersTable = PrettyTable(headings)
 	b = 6
 if SelectedTable == "won":
 	headings = ["Tender id","Tender Title","Offered Item","Announced in","Submitted in","Customer Name","Worked By","Value"]
 	#TendersTable = PrettyTable(headings)
 	b=7
 if SelectedTable == "lost":
 	headings = ["Tender id","Tender Title","Offered Item","Announced in","Submitted in","Customer Name","Worked By","winning Company"]
 	#TendersTable = PrettyTable(headings)
 	b=7 
 
 Rdata =[]
 Tdata =[]

 a = 0

 for i in columnData:
 	
 	Rdata = Rdata + [i]

 	if a==b:
 	#	TendersTable.add_row(Rdata) 
 		Tdata.append(Rdata)
 		Rdata = []	
 		
 		

 		a = 0
 	else:

 		a+=1

 #print (TendersTable)
 return headings,Tdata

def showEmployeeTable():
 
 #print("printing employees table .....")
 columnData = tuple(main.get_allEmployees())

 
 headings = ["Employee id","First Name","Last Name","Target"]
 #EmployeesTable = PrettyTable(headings) 
 
 Rdata =[]
 Tdata =[]

 a = 0
 
 for i in columnData:
 	
 	Rdata = Rdata + [i]
 	
 	if a==3:
 		#EmployeesTable.add_row(Rdata) 
 		Tdata.append(Rdata)
 		#print(Tdata)
 		Rdata = []	
 		
 		

 		a = 0
 	else:

 		a+=1

 #print (EmployeesTable)
 #return EmployeesTable
 return headings,Tdata

def showInstallationTable():
 #print("printing installations table .....")
 columnData = tuple(main.get_allInstallations())

 
 headings = ["Serial Number","Model","Delivery Date","Installation Date","Warranty Duration","Installation Location","Customer Name","Tender id"]
 #InstallationsTable = PrettyTable(headings) 
 
 Rdata =[]
 Tdata = []

 a = 0
 
 for i in columnData:
 	
 	Rdata = Rdata + [i]
 	
 	if a==7:
 			
 		#InstallationsTable.add_row(Rdata) 
 		Tdata.append(Rdata)
 		Rdata = []	
 
 		a = 0
 	else:

 		a+=1

 #print (InstallationsTable)
 return headings,Tdata

	
def get_namesList():
 #print("printing customers table .....")
 columnData = tuple(main.get_employeeNames())

 
 
 #CustomerTable = PrettyTable(headings) 
 """
 Rdata =[]
 Tdata =[]
 a = 0
 for i in columnData:
 	
 	Rdata = Rdata + [i]
 	
 	if a==1:
 			
 		#CustomerTable.add_row(list[Rdata]) 
 		Tdata.append(Rdata)
 		Rdata = []	
 
 		a = 0
 	else:

 		a+=1

 #print (CustomerTable) """
 return columnData

def get_ItemsList():
 #print("printing customers table .....")
 columnData = tuple(main.get_ItemsNames())

 
 """
 #CustomerTable = PrettyTable(headings) 
 
 Rdata =[]
 Tdata =[]
 a = 0
 for i in columnData:
 	
 	Rdata = Rdata + [i]
 	
 	if a==1:
 			
 		#CustomerTable.add_row(list[Rdata]) 
 		Tdata.append(Rdata)
 		Rdata = []	
 
 		a = 0
 	else:

 		a+=1

 #print (CustomerTable)"""
 return columnData

def get_TendersList():
 #print("printing customers table .....")
 columnData = tuple(main.get_tendersNames())

 
 
 #CustomerTable = PrettyTable(headings) 
 
 """ Rdata =[]
 Tdata =[]
 a = 0
 for i in columnData:
 	
 	Rdata = Rdata + [i]
 	
 	#if a==1:
 			
 	#CustomerTable.add_row(list[Rdata]) 
 	Tdata.append(Rdata)
 	Rdata = []	
 
 	#a = 0
 	#else:

 	#	a+=1

 #print (CustomerTable)
 print(Tdata)"""
 return columnData

def get_CustomersList():
 #print("printing customers table .....")
 columnData = tuple(main.get_CustomersNames())

 
 
 #CustomerTable = PrettyTable(headings) 
 
 """Rdata =[]
 Tdata =[]
 a = 0
 for i in columnData:
 	
 	Rdata = Rdata + [i]
 	
 	if a==1:
 			
 		#CustomerTable.add_row(list[Rdata]) 
 		Tdata.append(Rdata)
 		Rdata = []	
 
 		a = 0
 	else:

 		a+=1

 #print (CustomerTable)"""
 return columnData

def showItemsTable():

 #print("printing items table .....")
 columnData = tuple(main.get_allItems())

 
 headings = ["Item ID","Item Name","Price"]
 #ItemsTable = PrettyTable(headings) 
 
 Rdata =[]
 Tdata = []
 
 a = 0
 for i in columnData:
 	
 	Rdata = Rdata + [i]
 	
 	if a==2:
 			
 		#ItemsTable.add_row(Rdata)
 		Tdata.append(Rdata) 
 		
 		Rdata = []	
 
 		a = 0
 	else:

 		a+=1

 #print (ItemsTable)
 return headings,Tdata

def showItemsTable():

 #print("printing items table .....")
 columnData = tuple(main.get_allItems())

 
 headings = ["Item ID","Item Name","Price"]
 #ItemsTable = PrettyTable(headings) 
 
 Rdata =[]
 Tdata = []
 
 a = 0
 for i in columnData:
 	
 	Rdata = Rdata + [i]
 	
 	if a==2:
 			
 		#ItemsTable.add_row(Rdata)
 		Tdata.append(Rdata) 
 		
 		Rdata = []	
 
 		a = 0
 	else:

 		a+=1

 #print (ItemsTable)
 return headings,Tdata

def get_EmployeesYearlyPerformance():
	
 columnData = tuple(main.EmployeesYearlyPerformance())
 headings = ["Employee id","Name","Year","Target","Acheived Target","Total Won","Total Lost"]
 Rdata =[]
 Tdata =[]
 a = 0
 for i in columnData:
 	print(i)
 	Rdata = Rdata + [i]
 	if a==6:
 		#CustomerTable.add_row(list[Rdata]) 
 		Tdata.append(Rdata)
 		Rdata = []
 		a = 0
 	else:
 		a+=1

 #print (CustomerTable)
 return headings,Tdata

def get_InstallationsYearlyReport():
	
 columnData = tuple(main.InstallationsReport())
 headings = ["Year","Installations Count"]
 Rdata =[]
 Tdata =[]
 a = 0
 for i in columnData:
 	print(i)
 	Rdata = Rdata + [i]
 	if a==1:
 		#CustomerTable.add_row(list[Rdata]) 
 		Tdata.append(Rdata)
 		Rdata = []
 		a = 0
 	else:
 		a+=1

 #print (CustomerTable)
 return headings,Tdata

def get_TendersYearlyReport():
	
 columnData = tuple(main.TendersYearlyReport())
 headings = ["Year","Won Tenders Count","Lost Tenders Count"]
 Rdata =[]
 Tdata =[]
 a = 0
 for i in columnData:
 	print(i)
 	Rdata = Rdata + [i]
 	if a==2:
 		#CustomerTable.add_row(list[Rdata]) 
 		Tdata.append(Rdata)
 		Rdata = []
 		a = 0
 	else:
 		a+=1

 #print (CustomerTable)
 return headings,Tdata

def get_InstallationsYearlyReport():
	
 columnData = tuple(main.InstallationsReport())
 headings = ["Year","Installations Count"]
 Rdata =[]
 Tdata =[]
 a = 0
 for i in columnData:
 	print(i)
 	Rdata = Rdata + [i]
 	if a==1:
 		#CustomerTable.add_row(list[Rdata]) 
 		Tdata.append(Rdata)
 		Rdata = []
 		a = 0
 	else:
 		a+=1

 #print (CustomerTable)
 return headings,Tdata

def showCustomerTable():
 #print("printing customers table .....")
 columnData = tuple(main.get_allCustomers())

 
 headings = ["Customer ID","Customer Name","Location","Managing Employee"]
 #CustomerTable = PrettyTable(headings) 
 
 Rdata =[]
 Tdata =[]
 a = 0
 for i in columnData:
 	
 	Rdata = Rdata + [i]
 	
 	if a==3:
 			
 		#CustomerTable.add_row(list[Rdata]) 
 		Tdata.append(Rdata)
 		Rdata = []	
 
 		a = 0
 	else:

 		a+=1

 #print (CustomerTable)
 return headings,Tdata
