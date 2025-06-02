import PySimpleGUI as sg
import experiment
from operator import itemgetter
from datetime import datetime

#NOTE: all commented code was used for debugging while creating the code

"""AllEmployees = list(experiment.get_namesList())
AllEmployeesID = []
AllEmployeesNames =[]
for i in AllEmployees:
    AllEmployeesID.append(i[0])
    AllEmployeesNames.append(i[1])

AllItems = list(experiment.get_ItemsList())
AllItemsID = []
AllItemsNames = []
for i in AllItems:
    AllItemsID.append(i[0])
    AllItemsNames.append(i[1])


AllCustomers = list(experiment.get_CustomersList())
AllCustomersID = []
AllCustomersNames = []
for i in AllCustomers:
    AllCustomersID.append(i[0])
    AllCustomersNames.append(i[1])

AllTenders = list(experiment.get_TendersList())
AllTendersID = []
AllTendersNames = []
for i in AllTenders:
    AllTendersID.append(i[0])
    AllTendersNames.append(i[1])
"""

def make_win1():    #Main Window

    layout = [[sg.Text('Choose your Operation:')],
              [sg.Button("Add"),sg.Button("Delete")],
              [sg.Button('Exit')]]
    return sg.Window('Tenders Database', layout, finalize=True)

def make_win2():    #Insert Window

    Eheadings,Evalues = experiment.showEmployeeTable() 
    #print(headings,values)
    #sg.Print(experiment.showEmployeeTable())
    #create_tableWinE = create_table(Eheadings,sorted(Evalues,key = itemgetter(0)),'All Employees')
    
    
    
    Cheadings,Cvalues = experiment.showCustomerTable() 
    #print(Cvalues)
    #print(headings,values)
    #sg.Print(experiment.showEmployeeTable())
    #create_tableWinC = create_table(Cheadings,sorted(Cvalues,key = itemgetter(0)),'All Customers')
    
    
    
    Iheadings,Ivalues = experiment.showItemsTable() 
    #print(headings,values)
    #sg.Print(experiment.showItemsTable())
    #create_tableWinI = create_table(Iheadings,sorted(Ivalues,key = itemgetter(0)),"All Items")
    
    
    Theadings,Tvalues = experiment.showTenderTable('all') 
    #print(headings,values)
    #sg.Print(experiment.showEmployeeTable())
    #create_tableWinT = create_table(Theadings,sorted(Tvalues,key = itemgetter(0)),"All Tenders")

        
    INheadings,INvalues = experiment.showInstallationTable() 
    #print(headings,values)
    #sg.Print(experiment.showEmployeeTable())
    #create_tableWinIN = create_table(INheadings,sorted(INvalues,key = itemgetter(0)),'All Installations')

    employee_layout = [[sg.Text('Fill the fields below')],
              [sg.Text('Employee id*'),sg.Input(key='emp_id', enable_events=True)],
              [sg.Text('First Name*'),sg.Input(key='first_name', enable_events=True)],
              [sg.Text('Last Name*'),sg.Input(key='last_name', enable_events=True)],
              [sg.Text('Target'),sg.Input(key='target', enable_events=True)],
              [sg.Button('Add Employee'),sg.Button('Employee Search'),sg.Button('Yearly Performance')],
              [sg.Table(values=Evalues, headings=Eheadings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows=10,
                    key='-E_TABLE-',
                    row_height=25,
                    tooltip='Info')]]

    customer_layout = [[sg.Text('Fill the fields below')],
              [sg.Text('Customer id*'),sg.Input(key='customer_id', enable_events=True)],
              [sg.Text('Customer Name*'),sg.Input(key='customer_name', enable_events=True)],
              [sg.Text('Customer Location*'),sg.Input(key='customer_loc', enable_events=True)],
              #[sg.Text('Managing Employee id*'),sg.Input(key='m_emp_id', enable_events=True)],
              [sg.Text('Managing Employee Name*'),sg.OptionMenu(values=experiment.get_namesList(),size=(25,10), default_value='',key='-MEMP_Name-'),sg.Button('Clear Customer Manager Name')],
              [sg.Button('Add Customer'),sg.Button('Add Managing Employee'),sg.Button('Customer Search')],
              [sg.Table(values=Cvalues, headings=Cheadings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows=10,
                    key='-CTABLE-',
                    row_height=25,
                    tooltip='Info')]]

    item_layout = [[sg.Text('Fill the fields below')],
              [sg.Text('Item id*'),sg.Input(key='item_id', enable_events=True)],
              [sg.Text('Item Name*'),sg.Input(key='item_name', enable_events=True)],
              [sg.Text('Item Price*'),sg.Input(key='item_price', enable_events=True)],
              [sg.Button('Add Item'),sg.Button('Item Search')],
              [sg.Table(values=Ivalues, headings=Iheadings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows=10,
                    key='-ITABLE-',
                    row_height=25,
                    tooltip='Info')]]

    installation_layout = [[sg.Text('Fill the fields below')],
              [sg.Text('Serial Number*'),sg.Input(key='serial_num', enable_events=True),sg.Text('Model*'),sg.Input(key='model', enable_events=True)],
              #[sg.Text('Delivery Date*'),sg.Input(key='delivery_date', enable_events=True)],
              #[sg.Text('Installation Date*'),sg.Input(key='installation_date', enable_events=True)],
              [sg.Text('Delivery Date', key='-TXT-'),sg.Input(key='delivery_date', size=(20,1),enable_events=True), sg.CalendarButton('Choose Delivery Date', close_when_date_chosen=True,format='%y-%m-%d'),sg.Button("Clear Delivery Date")],
              [sg.Text('Insatallation Date', key='-TXT-'),sg.Input(key='installation_date', size=(20,1)), sg.CalendarButton("Choose Installation Date", close_when_date_chosen=True , format='%y-%m-%d'),sg.Button("Clear Installation Date")],
              [sg.Text('Installation Location'),sg.Input(key='installation_loc', enable_events=True),
              sg.Text('Warranty Duration'),sg.Input(key='warranty_duration', enable_events=True)],
              #[sg.Text('Customer id*'),sg.Input(key='in_customer_id', enable_events=True)],
              [sg.Text('Customer Name*'),sg.OptionMenu(values=experiment.get_CustomersList(),size=(25,10), default_value='',key='-IN_Cust_Name-'),sg.Button("Clear Customer Name (installation)"),
              sg.Text('Tender Name*'),sg.OptionMenu(values=experiment.get_TendersList(),size=(25,10), default_value='',key='-IN_Tend_Name-'),sg.Button("Clear Tender Name")],
              #[sg.Text('Tender id*'),sg.Input(key='in_tender_id', enable_events=True)],
              [sg.Button('Add Installation'),sg.Button('Installation Search'),sg.Button('Show Installations Report')],
              [sg.Table(values=INvalues, headings=INheadings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows=10,
                    key='-INTABLE-',
                    row_height=25,
                    tooltip='Info')]] 

    tender_layout = [[sg.Text('Fill the fields below')],
              [sg.Text('Tender id*'),sg.Input(key='tender_id', enable_events=True),sg.Text('Tender Title*'),sg.Input(key='tender_title', enable_events=True)],
              #[sg.Text('Announced in'),sg.Input(key='announced_in', enable_events=True)],
              #[sg.Text('Submitted in'),sg.Input(key='Submitted_in', enable_events=True)],
              [sg.Text('Announcing Date*', key='-TXT-'),sg.Input(key='announced_in', size=(20,1),enable_events=True), 
              sg.CalendarButton('Choose Announcing Date', close_when_date_chosen=True,format='%y-%m-%d'),sg.Button("Clear Announcing Date"),
              sg.Text('Submission Date*', key='-TXT-'),sg.Input(key='Submitted_in', size=(20,1)), sg.CalendarButton("Choose Submission Date", close_when_date_chosen=True , format='%y-%m-%d'),sg.Button("Clear Submission Date")],
              #[sg.Text('Submission Date*', key='-TXT-'),sg.Input(key='Submitted_in', size=(20,1)), sg.CalendarButton("Choose Submission Date", close_when_date_chosen=True , format='%y-%m-%d'),sg.Button("Clear Submission Date")],
              [sg.Text('Customer Name*'),sg.OptionMenu(values=experiment.get_CustomersList(),size=(25,10), default_value='',key='-Cust_Name-'),sg.Button("Clear Customer Name"),
              sg.Text('Worked by Employee Name*'),sg.OptionMenu(values=experiment.get_namesList(),size=(25,10), default_value='',key='-WEMP_Name-'),sg.Button("Clear Employee Name")],
              #[sg.Text('Customer id*'),sg.Input(key='t_customer_id', enable_events=True)],
              #[sg.Text('Employee id*'),sg.Input(key='t_emp_id', enable_events=True)],
              #[sg.Text('Worked by Employee Name*'),sg.OptionMenu(values=AllEmployeesNames,size=(25,10), default_value='',key='-WEMP_Name-'),sg.Button("Clear Employee Name")],
              #[sg.Text('Offered Item*'),sg.Input(key='OF_item_id', enable_events=True)],
              [sg.Text('Offered Item Name*'),sg.OptionMenu(values=experiment.get_ItemsList(),size=(25,10), default_value='',key='-Oitem_Name-'),sg.Button("Clear Item Name")],
              [sg.Text('Winning Company Name (if lost)'),sg.Input(key='winning_company', enable_events=True)],
              [sg.Button('Add as Won'),sg.Button('Add as Lost'),sg.Button('Tender Search'),sg.Button('Show Won Tenders'),sg.Button('Show Lost Tenders'),sg.Button('Show Tenders Report')],
              [sg.Table(values=Tvalues, headings=Theadings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows=10,
                    key='-T_TABLE-',
                    row_height=25,
                    tooltip='Info')],]

    layout = [[sg.TabGroup([[sg.Tab('Employee', employee_layout, tooltip='tip'), sg.Tab('Customer', customer_layout),sg.Tab('Item', item_layout),
          sg.Tab('Installation', installation_layout),sg.Tab('Tender', tender_layout)]], tooltip='TIP2')],
          [sg.Button('Refresh'),sg.Button('Exit')]]

    


    return sg.Window('Add Window', layout, finalize=True)


def make_win4():    #Delete Window
    
    Eheadings,Evalues = experiment.showEmployeeTable() 
    #print(headings,values)
    #sg.Print(experiment.showEmployeeTable())
    #create_tableWinE = create_table(Eheadings,sorted(Evalues,key = itemgetter(0)),'All Employees')
    
    
    
    Cheadings,Cvalues = experiment.showCustomerTable() 
    #print(Cvalues)
    #print(headings,values)
    #sg.Print(experiment.showEmployeeTable())
    #create_tableWinC = create_table(Cheadings,sorted(Cvalues,key = itemgetter(0)),'All Customers')
    
    
    
    Iheadings,Ivalues = experiment.showItemsTable() 
    #print(headings,values)
    #sg.Print(experiment.showItemsTable())
    #create_tableWinI = create_table(Iheadings,sorted(Ivalues,key = itemgetter(0)),"All Items")
    
    
    Theadings,Tvalues = experiment.showTenderTable('all') 
    #print(headings,values)
    #sg.Print(experiment.showEmployeeTable())
    #create_tableWinT = create_table(Theadings,sorted(Tvalues,key = itemgetter(0)),"All Tenders")

        
    INheadings,INvalues = experiment.showInstallationTable() 
    #print(headings,values)
    #sg.Print(experiment.showEmployeeTable())
    #create_tableWinIN = create_table(INheadings,sorted(INvalues,key = itemgetter(0)),'All Installations')
    
    Eoptions = ['emp_id','first_name', 'last_name', 'target']
    Coptions = ['customer_id','customer_name', 'customer_loc']
    Toptions = ['tender_id','tender_title', 'announced_in', 'Submitted_in', 'customer_id','emp_id']
    IToptions = ['item_id','item_name', 'item_price']
    INoptions = ['serial_num','model', 'delivery_date', 'installation_date', 'warranty_duration','installation_loc','customer_id','emp_id']

    employee_layout = [[sg.Text('Fill the fields below')],
              [sg.Text('Delete'),sg.OptionMenu(values=Eoptions,size=(4,8), default_value='',key='-E_Att-'),sg.Text('='),
              sg.Input(key='-E_DATA-', enable_events=True),sg.Button('Delete Employee')],
              [sg.Table(values=Evalues, headings=Eheadings, max_col_width=25,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows=10,
                    key='-E_TABLE-',
                    row_height=25,
                    tooltip='Info')]]

    customer_layout = [[sg.Text('Fill the fields below')],
              [sg.Text('Delete'),sg.OptionMenu(values=Coptions,size=(4,8), default_value='',key='-C_Att-'),sg.Text('='),
              sg.Input(key='-C_DATA-', enable_events=True),sg.Button('Delete Customer')],
              [sg.Table(values=Cvalues, headings=Cheadings, max_col_width=25,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows=10,
                    key='-CTABLE-',
                    row_height=25,
                    tooltip='Info')]]

    item_layout = [[sg.Text('Fill the fields below')],
              [sg.Text('Delete'),sg.OptionMenu(values=IToptions,size=(4,8), default_value='',key='-IT_Att-'),sg.Text('='),
              sg.Input(key='-IT_DATA-', enable_events=True),sg.Button('Delete Item')],
              [sg.Table(values=Ivalues, headings=Iheadings, max_col_width=25,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows=10,
                    key='-ITABLE-',
                    row_height=25,
                    tooltip='Info')]]

    installation_layout = [[sg.Text('Fill the fields below')],
              [sg.Text('Delete'),sg.OptionMenu(values=INoptions,size=(4,8), default_value='',key='-IN_Att-'),sg.Text('='),
              sg.Input(key='-IN_DATA-', enable_events=True),sg.Button('Delete Installation')],
              [sg.Table(values=INvalues, headings=INheadings, max_col_width=25,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows=10,
                    key='-INTABLE-',
                    row_height=25,
                    tooltip='Info')]] 

    tender_layout = [[sg.Text('Fill the fields below')],
              [sg.Text('Delete'),sg.OptionMenu(values=Toptions,size=(4,8), default_value='',key='-T_Att-'),sg.Text('='),
              sg.Input(key='-T_DATA-', enable_events=True),sg.Button('Delete Tender')],
              [sg.Table(values=Tvalues, headings=Theadings, max_col_width=25,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows=10,
                    key='-T_TABLE-',
                    row_height=25,
                    tooltip='Info')],]

    layout = [[sg.TabGroup([[sg.Tab('Employee', employee_layout, tooltip='tip'), sg.Tab('Customer', customer_layout),sg.Tab('Item', item_layout),
          sg.Tab('Installation', installation_layout),sg.Tab('Tender', tender_layout)]], tooltip='TIP2')],
          [sg.Button('Refresh'),sg.Button('Exit')]]

   

    return sg.Window('Delete Window', layout, finalize=True)    

def create_table(headings,values,selected_table):
    table_layout = [
    [sg.Table(values=values, headings=headings, max_col_width=25,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows=10,
                    key='-TABLE-',
                    row_height=25,
                    tooltip='Info')]]
    return sg.Window("{} Information".format(selected_table),table_layout, finalize=True)

mainWindow, insertWindow, deleteWindow, create_tableWin = make_win1(), None, None,None        # start off with 1 window open

while True:             # Event Loop
    X = 0
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        if window == insertWindow:       # if closing insertwindow, mark as closed
            insertWindow = None
        if window == deleteWindow:       # if closing win 2, mark as closed
            deleteWindow = None
        if window == create_tableWin:       # if closing win 2, mark as closed
            create_tableWin = None
        elif window == mainWindow:     # if closing win 1, exit program
            break
    
    
    elif event == 'All Employees':
        selected_table = "All Employees"
        headings,values = experiment.showEmployeeTable() 
        #print(headings,values)
        #sg.Print(experiment.showEmployeeTable())
        create_tableWin = create_table(headings,sorted(values,key = itemgetter(0)),selected_table)
    
    elif event == 'All Customers':
        selected_table = "All Customers"
        headings,values = experiment.showCustomerTable() 
        #print(headings,values)
        #sg.Print(experiment.showEmployeeTable())
        create_tableWin = create_table(headings,sorted(values,key = itemgetter(0)),selected_table)
    
    elif event == 'All Items':
        selected_table = "All Items"
        headings,values = experiment.showItemsTable() 
        #print(headings,values)
        #sg.Print(experiment.showItemsTable())
        create_tableWin = create_table(headings,sorted(values,key = itemgetter(0)),selected_table)
    
    elif event == 'All Tenders':
        selected_table = "All Tenders"
        headings,values = experiment.showTenderTable('all') 
        print(headings,values)
        #sg.Print(experiment.showEmployeeTable())
        create_tableWin = create_table(headings,sorted(values,key = itemgetter(0)),selected_table)

    elif event == 'Yearly Performance':
        
        selected_table = 'Employees Yearly Report'
        headings,values = experiment.get_EmployeesYearlyPerformance() 
        print(headings,values)
        #sg.Print(experiment.showEmployeeTable())
        create_tableWin = create_table(headings,sorted(values,key = itemgetter(0)),selected_table)

    elif event == 'Show Tenders Report':
        selected_table = 'Tenders Yearly Report'
        headings,values = experiment.get_TendersYearlyReport() 
        print(headings,values)
        #sg.Print(experiment.showEmployeeTable())
        create_tableWin = create_table(headings,sorted(values,key = itemgetter(0)),selected_table)


    elif event == 'Show Installations Report':
        selected_table = 'Installations Yearly Report'
        headings,values = experiment.get_InstallationsYearlyReport() 
        print(headings,values)
        #sg.Print(experiment.showEmployeeTable())
        create_tableWin = create_table(headings,sorted(values,key = itemgetter(0)),selected_table)

    elif event == 'Show Won Tenders':
        selected_table = "Won Tenders"
        headings,values = experiment.showTenderTable('won') 
        print(headings,values)
        #sg.Print(experiment.showEmployeeTable())
        create_tableWin = create_table(headings,sorted(values,key = itemgetter(0)),selected_table)
    
    elif event == 'Show Lost Tenders':
        selected_table = "Lost Tenders"
        headings,values = experiment.showTenderTable('lost') 
        print(headings,values)
        #sg.Print(experiment.showEmployeeTable())
        create_tableWin = create_table(headings,sorted(values,key = itemgetter(0)),selected_table)

    elif event == 'All Installations':
        selected_table = "All Installations"
        headings,values = experiment.showInstallationTable() 
        #print(headings,values)
        #sg.Print(experiment.showEmployeeTable())
        create_tableWin = create_table(headings,sorted(values,key = itemgetter(0)),selected_table)    
    
    elif event == 'Add Employee': 
        Eheadings,Evalues = experiment.showEmployeeTable()
        E = experiment.Employee(values['emp_id'],values['first_name'].strip(),values['last_name'].strip(),values['target'])
        
        if E is None:
            Evalues.append([values['emp_id'],values['first_name'].strip(),values['last_name'].strip(),values['target']])
            window['-E_TABLE-'].update(values =Evalues)
            sg.popup('Employee added')
        else: 
            sg.popup(E)

        
    elif event == 'Customer Search':
        Cheadings,Cvalues = experiment.showCustomerTable()

        search_values = [values['customer_id'],values['customer_name'],values['customer_loc'],values['-MEMP_Name-']]
        
        new_search_values = list(filter(None, search_values))
        filtered_serch_values=[]
        for i in new_search_values:
            a=0
            try:
                i = int(i)
            except:
                a=1
                print ("a is not an integer")

            if a==0:
                filtered_serch_values.append(int(i))
            elif a==1:
                filtered_serch_values.append(i)


        #print(filtered_serch_values)

        
        a=0
        NewCvalues=[]
        
        for i in Cvalues:
            if list(set(i) & set(filtered_serch_values)) == filtered_serch_values:
              NewCvalues.append(i)
                #print(NewCvalues)
            #else:
             #   print(type(a))
              #  print(type(i[0]))
        window['-CTABLE-'].update(values = NewCvalues)

    elif event == 'Item Search':
        ITheadings,ITvalues = experiment.showItemsTable()

        search_values = [values['item_id'],values['item_name'],values['item_price']]
        
        new_search_values = list(filter(None, search_values))
        filtered_serch_values=[]
        for i in new_search_values:
            a=0
            try:
                i = int(i)
            except:
                a=1
                #print ("a is not an integer")

            if a==0:
                filtered_serch_values.append(int(i))
            elif a==1:
                filtered_serch_values.append(i)
            


        print(filtered_serch_values)
        
        NewITvalues=[]
        
        for i in ITvalues:
            if (set(i) & set(filtered_serch_values) == set(filtered_serch_values)):
                NewITvalues.append(i)
                print(NewITvalues)
            else:
                print(type(a))
                print(type(i[0]))
        window['-ITABLE-'].update(values = NewITvalues)

    elif event == 'Installation Search':
        INheadings,INvalues = experiment.showInstallationTable()
        a=0
        T_IN_id =[]
        for i in AllTenders:
                if i[1] == values['-IN_Tend_Name-']:
                    
                    T_IN_id = AllTenders[a][0]
                    a+=1
                else:
                    a+=1

        search_values = [values['serial_num'],values['model'],values['delivery_date'],values['installation_date'],values['warranty_duration'],
                        values['installation_loc'],values['-IN_Cust_Name-'],T_IN_id]
        
        new_search_values = list(filter(None, search_values))
        filtered_serch_values=[]
        for i in new_search_values:
            a=0
            try:
                i = int(i)
            except:
                a=1
                #print ("a is not an integer")
            if a==0:
                filtered_serch_values.append(int(i))
            elif a==1:
                filtered_serch_values.append(i)


        print(filtered_serch_values)
        
        NewINvalues=[]
        
        for i in INvalues:
            if (set(i) & set(filtered_serch_values) == set(filtered_serch_values)):
                NewINvalues.append(i)
                #print(NewINvalues)
            #else:
                #print(type(a))
                #print(type(i[0]))
        window['-INTABLE-'].update(values = NewINvalues)

    elif event == 'Tender Search':
        Theadings,Tvalues = experiment.showTenderTable('all')
        a = 0
        C_T_id =[]
        W_E_id=[]
        I_T_id=[]

        for i in AllCustomers:
            if i[1] == values['-Cust_Name-']:
                    
                C_T_id = AllCustomers[a][0]
                a+=1
            else:
                a+=1
            a=0

            for i in AllEmployees:
                if i[1] == values['-WEMP_Name-']:
                    
                    W_E_id = AllEmployees[a][0]
                    a+=1
                else:
                    a+=1

            a=0
            
            for i in AllItems:
                if i[1] == values['-Oitem_Name-']:
                    
                    I_T_id = AllItems[a][0]
                    a+=1
                else:
                    a+=1

        search_values = [values['tender_id'], values['tender_title'], values['-Oitem_Name-'], values['announced_in'], values['Submitted_in'],values['-Cust_Name-'],values['-WEMP_Name-']]
        
        new_search_values = list(filter(None, search_values))
        filtered_search_values=[]
        
        for i in new_search_values:
            a=0
            try:
                i = int(i)
            except:
                a=1
                #print ("a is not an integer")
            
            try:
                #print("maybe a date")
                i = datetime.strptime(i,'%Y-%m-%d').date()
            except:
                a=2
                #print("Not a date")
                
            if a==0:
                filtered_search_values.append(int(i))
            elif a==1:
                #print("date is",type(i))
                filtered_search_values.append(i)
            elif a==2:
                filtered_search_values.append(i)


        print(filtered_search_values)
        
        NewTvalues=[]
        
        for i in Tvalues:
            print(i)
            if (set(i) & set(filtered_search_values) == set(filtered_search_values)):
                NewTvalues.append(i)
                #print(NewTvalues)
            #else:
                #print(type(a))
                #print(type(i[0]))
        window['-T_TABLE-'].update(values = NewTvalues)

    elif event == 'Employee Search':
        Eheadings,Evalues = experiment.showEmployeeTable()

        search_values = [values['emp_id'],values['first_name'],values['last_name'],values['target']]
        
        new_search_values = list(filter(None, search_values))
        filtered_serch_values=[]
        for i in new_search_values:
            a=0
            try:
                i = int(i)
            except:
                a=1
                #print ("a is not an integer")
            if a==0:
                filtered_serch_values.append(int(i))
            elif a==1:
                filtered_serch_values.append(i)


        #print(filtered_serch_values)

        EEvalues=[]
        for i in Evalues:
            
            EEvalues.append(i[0:4])
            #print(EEvalues)

        NewEvalues=[]
        for i in Evalues:
            if (set(i[0:4]) & set(filtered_serch_values) == set(filtered_serch_values)):
                print("found")
                NewEvalues.append(i)
            else:
                print("not found")
        #NewEvalues = [value for value in new_search_values if value in EEvalues]
        #print(set(i))
        #print(set(filtered_serch_values))
        #for i in EEvalues:
         #   print(i)
          #  if list(set(i) & set(filtered_serch_values)) == filtered_serch_values:
           #     NewEvalues.append(i)
                #print(NewEvalues)
            #else:
                #sg.popup("empty")
                
        window['-E_TABLE-'].update(values = NewEvalues)

        

    elif event == 'Add Customer': 
        Cheadings,Cvalues = experiment.showCustomerTable()

        C = experiment.customer(values['customer_id'],values['customer_name'],values['customer_loc'])
        
        if C is None:
            Cvalues.append([values['customer_id'],values['customer_name'],values['customer_loc'],""])
            #AllCustomers.append(values['customer_id'],values['customer_name'])
            #AllCustomersID.append(values['customer_id'])
            #AllCustomersNames.append(values['customer_name'])
            window['-Cust_Name-'].update(values=experiment.get_CustomersList())
            window['-CTABLE-'].update(values =Cvalues)
            sg.popup('Customer added')
        else: 
            sg.popup(C)


    elif event == 'Add Managing Employee':
        
        MEheadings,MEvalues = experiment.showCustomerTable()
        a=0

        for i in AllEmployees:
            if i[1] == values['-MEMP_Name-']:
                #print(values['-MEMP_Name-'])
                m_emp_id = AllEmployees[a][0]
                a+=1
            else:
                a+=1
                continue

        a=0
        ME = experiment.managed_by(int(values['customer_id']),m_emp_id)

        if ME is None: 

            for i in MEvalues:
                if i[3] is None or i[3] == "":
                    MEvalues[a][3] =  values['-MEMP_Name-']
                    a+=1
                else:
                    a+=1
                    continue
                    

            window['-CTABLE-'].update(values=MEvalues)
            sg.popup('Added')
        else: 
            sg.popup(ME)
        

    elif event == 'Add Item': 

            ITheadings,ITvalues = experiment.showItemsTable()

            IT = experiment.item(values['item_id'],values['item_name'],values['item_price'])
            
            if IT is None:
                ITvalues.append([values['item_id'],values['item_name'],values['item_price']])
                window['-ITABLE-'].update(values =ITvalues)
                window['-Oitem_Name-'].update(values=experiment.get_ItemsList())
                sg.popup('Item added')
            else: 
                sg.popup(IT)


    elif event == 'Add as Won':
            Wheadings,Wvalues = experiment.showTenderTable('all') 

            a = 0
            
            for i in AllCustomers:
                if i[1] == values['-Cust_Name-']:
                    
                    C_T_id = AllCustomers[a][0]
                    a+=1
                else:
                    a+=1
                    continue

            a=0

            for i in AllEmployees:
                if i[1] == values['-WEMP_Name-']:
                    
                    W_E_id = AllEmployees[a][0]
                    a+=1
                else:
                    a+=1

            a=0
            
            for i in AllItems:
                if i[1] == values['-Oitem_Name-']:
                    
                    I_T_id = AllItems[a][0]
                    a+=1
                else:
                    a+=1

            if values['announced_in'] > values['Submitted_in']:
                sg.popup("Invalid Dates")           
            else:
                T = experiment.Tender(values['tender_id'], values['tender_title'], values['announced_in'], values['Submitted_in'], C_T_id, W_E_id)
                OI = experiment.Offered_in(values['tender_id'], I_T_id)
                W = experiment.Won(values['tender_id'])

                 
                if T is None and OI is None and W is None:
                    Wvalues.append([values['tender_id'], values['tender_title'], values['-Oitem_Name-'], values['announced_in'], values['Submitted_in'],values['-Cust_Name-'],values['-WEMP_Name-']])
                    window['-T_TABLE-'].update(values=Wvalues)
                    #AllTenders.append([values['tender_id'],values['tender_title']])
                    #AllTendersID.append(values['tender_id'])
                    #AllTendersNames.append(values['tender_title'])
                    window['-IN_Tend_Name-'].update(values=experiment.get_TendersList())
                    sg.popup('Won tender added')
                else: 
                    sg.popup(T,OI,W)
            

    elif event == 'Add as Lost': 

            Lheadings,Lvalues = experiment.showTenderTable('all') 

            a = 0
            
            for i in AllCustomers:
                if i[1] == values['-Cust_Name-']:
                    
                    C_T_id = AllCustomers[a][0]
                    a+=1
                else:
                    a+=1
                    continue

            a=0

            for i in AllEmployees:
                if i[1] == values['-WEMP_Name-']:
                    
                    W_E_id = AllEmployees[a][0]
                    a+=1
                else:
                    a+=1

            a=0
            
            for i in AllItems:
                if i[1] == values['-Oitem_Name-']:
                    
                    I_T_id = AllItems[a][0]
                    a+=1
                else:
                    a+=1
           
            if values['announced_in'] > values['Submitted_in']:
                sg.popup("Invalid Dates")
            else:

                T = experiment.Tender(values['tender_id'], values['tender_title'], values['announced_in'], values['Submitted_in'], C_T_id, W_E_id)
                OI = experiment.Offered_in(values['tender_id'], I_T_id)
                L = experiment.Lost(values['tender_id'],values['winning_company'])

                if T is None and OI is None and L is None:
                    Lvalues.append([values['tender_id'], values['tender_title'], values['-Oitem_Name-'], values['announced_in'], values['Submitted_in'],values['-Cust_Name-'],values['-WEMP_Name-']])
                    window['-T_TABLE-'].update(values=Lvalues)
                    sg.popup('Lost tender added')
                else: 
                    sg.popup(T,OI,L)
            

    elif event == 'Add Installation': 

            INheadings,INvalues = experiment.showInstallationTable() 

            a = 0
            
            for i in AllCustomers:
                if i[1] == values['-IN_Cust_Name-']:
                    
                    C_IN_id = AllCustomers[a][0]
                    a+=1
                else:
                    a+=1
                    continue

            a=0

            for i in AllTenders:
                if i[1] == values['-IN_Tend_Name-']:
                    
                    T_IN_id = AllTenders[a][0]
                    a+=1
                else:
                    a+=1

            a=0

            if values['delivery_date'] > values['installation_date']:
                sg.popup("invalid dates")
            else:
                
                I = experiment.Installation(values['serial_num'], values['model'], values['delivery_date'], values['installation_date'],
                                            values['warranty_duration'], values['installation_loc'], C_IN_id ,
                                            T_IN_id)

            
                if I is None:
                    INvalues.append([values['serial_num'], values['model'], values['delivery_date'], values['installation_date'],
                                                values['warranty_duration'], values['installation_loc'], values['-IN_Cust_Name-'],
                                                T_IN_id])
                    window['-INTABLE-'].update(values=INvalues)
                    sg.popup('New installation added')
                else: 
                    sg.popup(I)

    
    elif event == 'Add': #open insert window
        
        try:
          insertWindow = make_win2()
        except:
          sg.popup('No Data')

    elif event == 'Choose Delivery Date':
        date = sg.popup_get_date()
        if date:
            month, day, year = date
            #print(day,month,year)
            window['delivery_date'].update(f"{year}-{month:0>2d}-{day:0>2d}")

    elif event == 'Choose Installation Date':
        date = sg.popup_get_date()
        if date:
            month, day, year = date
            window['installation_date'].update(f"{year}-{month:0>2d}-{day:0>2d}")

    elif event == 'Choose Announcing Date':
        date = sg.popup_get_date()
        if date:
            month, day, year = date
            #print(day,month,year)
            window['announced_in'].update(f"{year}-{month:0>2d}-{day:0>2d}")

    elif event == 'Choose Submission Date':
        date = sg.popup_get_date()
        if date:
            month, day, year = date
            window['Submitted_in'].update(f"{year}-{month:0>2d}-{day:0>2d}")

    elif event == 'Delete': #open Delete window

        deleteWindow = make_win4()

    elif event =='Refresh':
        
        Eheadings,Evalues = experiment.showEmployeeTable()
        window['-E_TABLE-'].update(values=Evalues) 
        
        Cheadings,Cvalues = experiment.showCustomerTable()
        window['-CTABLE-'].update(values=Cvalues) 
        
        Iheadings,Ivalues = experiment.showItemsTable()
        window['-ITABLE-'].update(values=Ivalues) 
       
        Theadings,Tvalues = experiment.showTenderTable('all') 
        window['-T_TABLE-'].update(values=Tvalues)
        
        INheadings,INvalues = experiment.showInstallationTable()
        window['-INTABLE-'].update(values=INvalues) 
    
              
    elif event =='Delete Employee':
        
        try:
            E = experiment.deleteQuery('employees',values['-E_Att-'],values['-E_DATA-'])
        except:
            sg.popup(E)
        
    elif event =='Delete Customer':
        E = experiment.deleteQuery('customers',values['-C_Att-'],values['-C_DATA-'])
    elif event =='Delete Installation':
        E = experiment.deleteQuery('installations',values['-IN_Att-'],values['-IN_DATA-'])
    elif event =='Delete Item':
        E = experiment.deleteQuery('items',values['-IT_Att-'],values['-IT_DATA-'])
    elif event =='Delete Tender':
        E = experiment.deleteQuery('tenders',values['-T_Att-'],values['-T_DATA-'])

               
        

    elif event =='Clear Customer Manager Name':
        window['-MEMP_Name-'].update("")
    elif event =='Clear Customer Name (installation)':
        window['-IN_Cust_Name-'].update("")
    elif event =='Clear Customer Name':
        window['-Cust_Name-'].update("")
    
    elif event =='Clear Delivery Date':
        window['delivery_date'].update("")
    elif event =='Clear Installation Date':
        window['installation_date'].update("")
    elif event =='Clear Tender Name':
        window['-IN_Tend_Name-'].update("")

    elif event =='Clear Employee Name':
        window['-WEMP_Name-'].update("")
    elif event =='Clear Item Name':
        window['-Oitem_Name-'].update("")
    elif event =='Clear Announcing Date':
        window['announced_in'].update("")
    elif event =='Clear Submission Date':
        window['Submitted_in'].update("")



window.close()
