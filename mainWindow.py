from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

from SQLConnection import *
from DisplayWidget import *


class Window(QMainWindow):
    """simple window layout"""
    def __init__(self):
        
        super().__init__()
        #palette = QPalette()
        #palette.setColor(QPalette.Background,QColor(0, 0, 255, 127))

        #self.setPalette(palette)
        
        self.setWindowTitle("Coffee Database PyQt4 SQL")
        self.resize(350,400)
        self.icon = QIcon(QPixmap("./images/coffeeIcon.png"))
        self.setWindowIcon(self.icon)

        #connection
        self.connection = None

        #create the initial layout
        self.initial_layout()
        
    def initial_layout(self):
        
        #create actions
        self.open_database = QAction("Open Database",self)
        self.close_database = QAction("Close Database",self)
        self.show_products = QAction("Show Products",self)
        self.find_products = QAction("Find Products",self)

        self.menu = QMenuBar()
               
        self.database_toolbar = QToolBar()

        self.database_menu = self.menu.addMenu("Database")
        self.products_menu = self.menu.addMenu("Products")

        self.database_menu.addAction(self.open_database)
        self.database_menu.addAction(self.close_database)

        self.products_menu.addAction(self.show_products)
        self.products_menu.addAction(self.find_products)

        self.database_toolbar.addAction(self.open_database)
        self.database_toolbar.addAction(self.close_database)

        self.addToolBar(self.database_toolbar)

        self.setMenuBar(self.menu)

        self.open_database.triggered.connect(self.open_connection)
        self.close_database.triggered.connect(self.close_connection)

        self.show_products.triggered.connect(self.show_products_layout)
        self.find_products.triggered.connect(self.find_products_layout)

    def show_products_layout(self):
        
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
            
        self.setCentralWidget(self.display_widget)
        if self.connection != None:
            query = self.connection.show_all_products()
            print(query)
            self.display_widget.show_results(query)
        else:
            print("A DB Connection must be opened")

    def find_products_layout(self):
        if not hasattr(self,"display_widget"):
            self.display_widget = DisplayWidget()
        self.setCentralWidget(self.display_widget)

        if self.connection != None:
            query = self.connection.find_products_by_number((1,))
            print(query)
            self.display_widget.show_results(query)
        else:
            print("A DB connection must be opened!")
        
    def open_connection(self):
        path = QFileDialog.getOpenFileName()

        self.connection = SQLConnection(path)

        opened = self.connection.open_database()

        print(opened)
    def close_connection(self):
        if self.connection:
            self.connection.close_database()
            print("closed")
        else:
            print("no db to close")
        
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = Window()
    window.show()
    window.raise_()
    application.exec_()
    
