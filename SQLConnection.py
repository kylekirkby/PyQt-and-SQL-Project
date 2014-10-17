
from PyQt4.QtSql import *

class SQLConnection:
    
    """Handles the conncetion to the SQL database"""
    
    def __init__(self,path):

        self.path = path

        self.db = None

    def open_database(self):
        
        if self.db:
            self.close_database()

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)

        opened_ok = self.db.open()

        return opened_ok
    
    def close_database(self):

        if self.db:
            if self.db.isOpen() == True:
                self.db.close()
                #remove the database from the QSqlDatabase object - "conn" is the default
                #database name
                QSqlDatabase.removeDatabase("conn")
                closed = self.db.open()
                print("closed con")
            else:
                print("No connection open")
        else:
            print("No connection to close!")

    def closeEvent(self,event):
        self.close_database()

    def show_all_products(self):
        query = QSqlQuery()
        query.prepare(""" SELECT * FROM Product""")
        query.exec_()
        return query

    def find_products_by_number(self,values):
        
        query = QSqlQuery()
        query.prepare(""" SELECT * FROM Product WHERE ProductID =? """)
        query.addBindValue(values[0])
        query.exec_()
        return query
