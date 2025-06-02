import psycopg2

from config import config

#we can use this directly to the database

#connection = psycopg2.connect( host = "localhost", port = "5432", database= "master"
# user= "postgres, password = "2Rv5w2463E")

#or this create an .ini file with a config file to read the .ini file and 
#do like the below code

def connect(): #will connect you to the postgresql server

	connection = None #no value 
	
	try:
		params = config()
		print ("connecting to the postgreSQL database ...")
		connection = psycopg2.connect(**params) 

		#create a cursor
		crsr = connection.cursor()
		print("postgreSQL database Version: ")
		crsr.execute('SELECT version()') #the command line in postgresql 
		db_version = crsr.fetchone() #fetches one output 
		print(db_version)
		crsr.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print (error)
	finally:
		if connection is not None:
			connection.close()
			print("Database connection is terminated.")




def insert_Customer(data):
    """ insert a new customer into the customers table """
    L = list(data)
    for i in L:
        if i[1] == "" or i[1] == 0 :
            L.remove(i)
    
    data = tuple(L)
    print(data)
    columns = ','.join([f'"{x[0]}"' for x in data])
    #print(columns)
    param_placeholders = ','.join(['%s' for x in range(len(data))])
    #print(param_placeholders)
    values = tuple(x[1] for x in data)
    print(values)
    sql = f"""INSERT INTO customers({columns})
             VALUES({param_placeholders});"""
    conn = None
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (values))
        
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            #print("new customer added")
            conn.close()

def insert_Item(data):
    """ insert a new item into the items table """
    L = list(data)
    for i in L:
        if i[1] == "" or i[1] == 0 :
            L.remove(i)

    data = tuple(L)
    print(data)
    columns = ','.join([f'"{x[0]}"' for x in data])
    #print(columns)
    param_placeholders = ','.join(['%s' for x in range(len(data))])
    #print(param_placeholders)
    values = tuple(x[1] for x in data)
    print(values)
    sql = f"""INSERT INTO items({columns})
             VALUES({param_placeholders});"""
    conn = None
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (values))
        
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            print("new item added")
            conn.close()
              

def insert_Tender(data):
    """ insert a new tender into the tenders table """
    L = list(data)
    
    for i in L:
        if i[1] == "" or i[1] == 0 :
            L.remove(i)

    data = tuple(L)
    print(data)
    columns = ','.join([f'"{x[0]}"' for x in data])
    #print(columns)
    param_placeholders = ','.join(['%s' for x in range(len(data))])
    #print(param_placeholders)
    values = tuple(x[1] for x in data)
    print(values)
    sql = f"""INSERT INTO tenders({columns})
             VALUES({param_placeholders});"""
    conn = None
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (values))
        
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            print("new tender added")
            conn.close()  


def insert_Employee(data):
    """ insert a new employee into the employees table """
    L = list(data)
    for i in L:
        if i[1] == "" or i[1] == 0 :
            L.remove(i)
    
    data = tuple(L)
    print(data)
    columns = ','.join([f'"{x[0]}"' for x in data])
    #print(columns)
    param_placeholders = ','.join(['%s' for x in range(len(data))])
    #print(param_placeholders)
    values = tuple(x[1] for x in data)
    print(values)
    sql = f"""INSERT INTO employees({columns})
             VALUES({param_placeholders});"""
    conn = None
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (values))
        
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            print("new employee added")
            conn.close()

def insert_Installation(data):
    """ insert a new installation into the installations table """
    L = list(data)

    for i in L:
        if i[1] == "" or i[1] == 0 :
            L.remove(i)

        
    
    data = tuple(L)
    print(data)
    columns = ','.join([f'"{x[0]}"' for x in data])
    #print(columns)
    param_placeholders = ','.join(['%s' for x in range(len(data))])
    #print(param_placeholders)
    values = tuple(x[1] for x in data)
    print(values)
    sql = f"""INSERT INTO installations({columns})
             VALUES({param_placeholders});"""
    conn = None
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (values))
        
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            print("new installation added")
            conn.close()

def insert_Won(data):
    """ insert a new won tender into the won table """
    L = list(data)

    for i in L:
        if i[1] == "" or i[1] == 0 :
            L.remove(i)

    data = tuple(L)
    print(data)
    columns = ','.join([f'"{x[0]}"' for x in data])
    #print(columns)
    param_placeholders = ','.join(['%s' for x in range(len(data))])
    #print(param_placeholders)
    values = tuple(x[1] for x in data)
    print(values)
    sql = f"""INSERT INTO won({columns})
             VALUES({param_placeholders});"""
    conn = None
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (values))
        
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            print("Won tender added")
            conn.close()

def insert_OfferedIn(data):
    """ insert a new item and tender into the offered_in table """
    L = list(data)
    for i in L:
        if i[1] == "" or i[1] == 0 :
            L.remove(i)
    
    data = tuple(L)
    print(data)
    columns = ','.join([f'"{x[0]}"' for x in data])
    #print(columns)
    param_placeholders = ','.join(['%s' for x in range(len(data))])
    #print(param_placeholders)
    values = tuple(x[1] for x in data)
    print(values)
    sql = f"""INSERT INTO offered_in({columns})
             VALUES({param_placeholders});"""
    conn = None
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (values))
        
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            print("offered in relation added")
            conn.close()


def insert_ManagedBy(data):
    """ insert a new managed by relation between customers and employees into the managed_by table"""
    L = list(data)
    for i in L:
        if i[1] == "" or i[1] == 0 :
            L.remove(i)
    
    data = tuple(L)
    print(data)
    columns = ','.join([f'"{x[0]}"' for x in data])
    print(columns)
    param_placeholders = ','.join(['%s' for x in range(len(data))])
    print(param_placeholders)
    values = tuple(x[1] for x in data)
    print(values)
    sql = f"""INSERT INTO managed_by({columns})
             VALUES({param_placeholders});"""
    conn = None
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (values))
        
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            print("managed by relation added")
            conn.close()

def insert_Lost(data):
    """ insert a new lost tender """
    L = list(data)
    for i in L:
        if i[1] == "" or i[1] == 0 :
            L.remove(i)
    
    data = tuple(L)
    print(data)
    columns = ','.join([f'"{x[0]}"' for x in data])
    #print(columns)
    param_placeholders = ','.join(['%s' for x in range(len(data))])
    #print(param_placeholders)
    values = tuple(x[1] for x in data)
    print(values)
    sql = f"""INSERT INTO lost({columns})
             VALUES({param_placeholders});"""
    conn = None
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (values))
        
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            print("Lost tender added")
            conn.close()


def update(Tname,data,rdata):
    
    table = Tname

    
    
    sql = f"""UPDATE {table} SET {data[0]} = {data[1]} 
             WHERE {rdata[0]} = {rdata[1]};"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql)
        # get the number of updated rows
        updated_rows = cur.rowcount
        print(updated_rows)
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    

def get_allEmployees():
    """ Query all employees information """
    conn = None
    r=[]
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
        # another way to call a function
        cur.execute(""" SELECT emp_id,first_name,last_name, target
            FROM employees
            ORDER BY emp_id; """)
        
        # process the result set
        row = cur.fetchone()
        
        while row is not None:
            #print(row)
            r.extend(row)
            row = cur.fetchone()
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return r

def get_allTenders(Q):
    """ Query all tenders information """
    conn = None
    r=[]
   
    try:

        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
       
        if Q == "all":
            cur.execute(""" SELECT T.tender_id,T.tender_title,I.item_name AS offered_item,T.announced_in,T.submitted_in, C.customer_name, EMP.first_name AS worked_by
                FROM tenders T
                LEFT JOIN employees EMP
                ON EMP.emp_id = T.emp_id
                LEFT JOIN customers C
                ON C.customer_id = T.customer_id
                LEFT JOIN offered_in OI 
                ON OI.tender_id = T.tender_id
                LEFT JOIN items I
                ON I.item_id = OI.item_id
                ORDER BY T.tender_id;""")
            
            # process the result set
            row = cur.fetchone()
           

        if Q == "lost":
            cur.execute(""" SELECT L.tender_id,T.tender_title,I.item_name AS offered_item,T.announced_in,T.submitted_in, C.customer_name, EMP.first_name AS worked_by, L.winning_company
                FROM lost L
                JOIN tenders T
                ON L.tender_id = T.tender_id
                JOIN customers C
                ON C.customer_id = T.customer_id
                JOIN employees EMP
                ON EMP.emp_id=T.emp_id
                LEFT JOIN offered_in OI 
                ON OI.tender_id = T.tender_id
                LEFT JOIN items I
                ON I.item_id = OI.item_id
                ORDER BY L.tender_id; """)
            
            # process the result set
            row = cur.fetchone()

        if Q == "won":
            cur.execute(""" SELECT W.tender_id,T.tender_title,IT.item_name AS offered_item,T.announced_in,T.submitted_in, C.customer_name, EMP.first_name AS worked_by,IT.item_price AS tender_value
                FROM won W
                JOIN tenders T
                ON T.tender_id = W.tender_id
                JOIN employees EMP
                ON EMP.emp_id = T.emp_id
                JOIN customers C
                ON C.customer_id = T.customer_id
                JOIN offered_in OI
                ON OI.tender_id = T.tender_id
                JOIN items IT
                ON IT.item_id=OI.item_id
                ORDER BY W.tender_id; """)
            
            # process the result set
            row = cur.fetchone()

        while row is not None:
            
            
            r.extend(row)
            
            row = cur.fetchone()
        #print(r)
            

        # close the communication with the PostgreSQL database server
        #print("END")
        
        cur.close()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return r

def get_allItems():
    """ Query all items information """
    conn = None
    r=[]
    try:

        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
       
        cur.execute(""" SELECT *
            FROM items
            ORDER BY item_id; """)
            
        # process the result set
        row = cur.fetchone()
            
            
        while row is not None:
            #print(row)
            r.extend(row)
            row = cur.fetchone()
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return r



def get_allInstallations():
    """ Query all installation information """
    conn = None
    r=[]
    try:

        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
       
        cur.execute(""" SELECT I.serial_num,I.model,I.delivery_date,I.installation_date,I.warranty_duration,I.installation_loc,C.customer_name,I.tender_id
            FROM installations I
            LEFT JOIN customers C
            ON C.customer_id=I.customer_id; """)
            
        # process the result set
        row = cur.fetchone()
            
            
        while row is not None:
            #print(row)
            r.extend(row)
            row = cur.fetchone()
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            conn.close()
            return r
def get_allCustomers():
    """ Query all customers information """
    conn = None
    r=[]
    try:

        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
       
        cur.execute(""" SELECT C.customer_id,C.customer_name,C.customer_loc,E.first_name AS Managing_Employee
            FROM customers C
            LEFT JOIN managed_by MB
            ON MB.customer_id = C.customer_id
            LEFT JOIN employees E
            ON E.emp_id = MB.emp_id
            ORDER BY C.customer_id; """)
            
        # process the result set
        row = cur.fetchone()
            
            
        while row is not None:
            #print(row)
            r.extend(row)
            row = cur.fetchone()
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            conn.close()
            return r

def get_employeeNames():
    """ Query all employees names and id """
    conn = None
    r=[]
    try:

        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
       
        cur.execute(""" SELECT first_name
            FROM employees; """)
            
        # process the result set
        row = cur.fetchone()
            
            
        while row is not None:
            #print(row)
            r.extend(row)
            row = cur.fetchone()
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            conn.close()
            return r

def get_tendersNames():
    """ Query all customers information """
    conn = None
    r=[]
    try:

        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
       
        cur.execute(""" SELECT T.tender_title
            FROM tenders T
            JOIN won W
            ON T.tender_id = W.tender_id; """)
            
        # process the result set
        row = cur.fetchone()
            
            
        while row is not None:
            #print(row)
            r.extend(row)
            row = cur.fetchone()
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            conn.close()
            return r

def get_ItemsNames():
    """ Query all customers information """
    conn = None
    r=[]
    try:

        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
       
        cur.execute(""" SELECT item_name
            FROM items; """)
            
        # process the result set
        row = cur.fetchone()
            
            
        while row is not None:
            #print(row)
            r.extend(row)
            row = cur.fetchone()
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            conn.close()
            return r


def get_CustomersNames():
    """ Query all customers information """
    conn = None
    r=[]
    try:

        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
       
        cur.execute(""" SELECT customer_name
            FROM customers; """)
            
        # process the result set
        row = cur.fetchone()
            
            
        while row is not None:
            #print(row)
            r.extend(row)
            row = cur.fetchone()
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            conn.close()
            return r

def delete(Tname,data,a):
    """ delete """
    table = Tname
    
    if a==0:
        sql = f"""DELETE FROM {table} WHERE {data[0]} = {data[1]};"""
    elif a==1:
        sql = f"""DELETE FROM {table} WHERE {data[0]} = '{data[1]}';"""

    conn = None
    rows_deleted = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql)
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            conn.close()
            print("deleted")

    return rows_deleted

def EmployeesYearlyPerformance():
    """ Query all customers information """
    conn = None
    r=[]
    try:

        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
       
        cur.execute(""" SELECT EMP.emp_id, EMP.first_name, DATE_PART('year',T.submitted_in) AS year ,EMP.target, SUM(IT.item_price) AS acheived_target, COUNT(W.tender_id) AS Won_Tenders,COUNT(L.tender_id) AS Lost_Tenders
                    FROM employees EMP
                    LEFT JOIN tenders T
                    ON T.emp_id = EMP.emp_id
                    LEFT JOIN won W
                    ON W.tender_id = T.tender_id
                    LEFT JOIN lost L
                    ON L.tender_id = T.tender_id
                    LEFT JOIN offered_in OI
                    ON OI.tender_id = T.tender_id
                    LEFT JOIN items IT
                    ON IT.item_id = OI.item_id
                    GROUP BY EMP.emp_id, DATE_PART('year',T.submitted_in)
                    ORDER BY EMP.emp_id; """)
            
        # process the result set
        row = cur.fetchone()
            
            
        while row is not None:
            #print(row)
            r.extend(row)
            row = cur.fetchone()
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            conn.close()
            return r

def TendersYearlyReport():
    """ Query all customers information """
    conn = None
    r=[]
    try:

        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
       
        cur.execute(""" SELECT DATE_PART('year',T.submitted_in) AS year ,COUNT(W.tender_id) AS Won_Tenders,COUNT(L.tender_id) AS Lost_Tenders
                    FROM tenders T
                    LEFT JOIN won W
                    ON W.tender_id = T.tender_id
                    LEFT JOIN lost L
                    ON L.tender_id = T.tender_id
                    GROUP BY DATE_PART('year',T.submitted_in); """)
            
        # process the result set
        row = cur.fetchone()
            
            
        while row is not None:
            #print(row)
            r.extend(row)
            row = cur.fetchone()
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            conn.close()
            return r

def InstallationsReport():
    """ Query all customers information """
    conn = None
    r=[]
    try:

        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
       
        cur.execute(""" SELECT DATE_PART('year',installation_date) AS year ,COUNT(serial_num) AS Installations_count
                    FROM installations 
                    GROUP BY DATE_PART('year',installation_date); """)
            
        # process the result set
        row = cur.fetchone()
            
            
        while row is not None:
            #print(row)
            r.extend(row)
            row = cur.fetchone()
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return error
    finally:
        if conn is not None:
            conn.close()
            return r
if __name__ == '__main__':
    connect()
  	
