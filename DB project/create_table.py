#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (

        """ 
        CREATE TABLE items (
                item_id INT PRIMARY KEY,
                item_name VARCHAR(255) NOT NULL,
                item_price INT NOT NULL


        );
        """,
        """
        CREATE TABLE employees (
                emp_id INT PRIMARY KEY,
                first_name VARCHAR (30) NOT NULL,
                last_name VARCHAR (30) NOT NULL,
                target INT DEFAULT 100000
                

        );
        """,
        """
        CREATE TABLE customers (
                customer_id INT PRIMARY KEY,
                customer_name VARCHAR (100) NOT NULL,
                customer_loc VARCHAR(100),
                UNIQUE (customer_name)
                
        );
        """,
        """
        CREATE TABLE tenders (
            tender_id INT PRIMARY KEY,
            tender_title VARCHAR(255) NOT NULL,
            announced_in DATE,
            submitted_in DATE,
            customer_id INT,
            emp_id INT, 


            UNIQUE (tender_title),

            FOREIGN KEY (customer_id)
            REFERENCES customers (customer_id)
            ON UPDATE CASCADE ON DELETE CASCADE,

            FOREIGN KEY (emp_id)
            REFERENCES employees (emp_id)
            ON UPDATE CASCADE ON DELETE CASCADE

        );
        """,
        """

        CREATE TABLE won (
                tender_id INT,
                
                PRIMARY KEY (tender_id),
                FOREIGN KEY (tender_id) REFERENCES tenders (tender_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        );
        """,
        """
        CREATE TABLE installations (
                serial_num VARCHAR(50) PRIMARY KEY,
                model VARCHAR(50) NOT NULL, 
                delivery_date DATE NOT NULL,
                installation_date DATE NOT NULL,
                warranty_duration INT DEFAULT 1,
                installation_loc VARCHAR (50),
                customer_id INT,
                tender_id INT,

                
                FOREIGN KEY (customer_id) REFERENCES customers (customer_id) 
                ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (tender_id) REFERENCES won (tender_id) 
                ON UPDATE CASCADE ON DELETE CASCADE
                

        );
        """,
        """
        CREATE TABLE offered_in (
                item_id INT,
                tender_id INT,

                PRIMARY KEY (item_id, tender_id),
                FOREIGN KEY (item_id) REFERENCES items (item_id) 
                ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (tender_id) REFERENCES tenders (tender_id) 
                ON UPDATE CASCADE ON DELETE CASCADE
        );
        """,
        """
        CREATE TABLE lost (
                tender_id INT,
                winning_company VARCHAR(25) NOT NULL,
                
                PRIMARY KEY (tender_id, winning_company),
                FOREIGN KEY (tender_id) REFERENCES tenders (tender_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        );
        """,
        """
        CREATE TABLE managed_by (
                customer_id INT,
                emp_id INT,

                PRIMARY KEY (customer_id,emp_id),
                FOREIGN KEY (customer_id) REFERENCES customers (customer_id) 
                ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (emp_id) REFERENCES employees (emp_id) 
                ON UPDATE CASCADE ON DELETE CASCADE

        );
        """

)


    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print("tables created")
            conn.close()


if __name__ == '__main__':
    create_tables()