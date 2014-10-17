from PyQt4.QtGui import *
from PyQt4.QtSql import *


class DisplayWidget(QWidget):
    
    """ Display Widget module for the """
    
    def __init__(self):
        super().__init__()

        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.model = None
        self.results_table = None
        self.results_layout = None
        self.results_widget = None

        self.display_results()

    def display_results(self):

        self.results_table = QTableView()

        #create buttons
        self.searchButton = QPushButton("Search")
        self.orderButton = QPushButton("Order")
        self.newButton1 = QPushButton("New Button")
        self.newButton2 = QPushButton("New Button2")

        #create the button layout
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.searchButton)
        self.buttonLayout.addWidget(self.orderButton)
        self.buttonLayout.addWidget(self.newButton1)
        self.buttonLayout.addWidget(self.newButton2)

        #create the button widget
        self.buttonWidget = QWidget()
        self.buttonWidget.setLayout(self.buttonLayout)


        #create the main results layout - Vertical         
        self.results_layout = QVBoxLayout()
        self.results_layout.addWidget(self.results_table)
        self.results_layout.addWidget(self.buttonWidget)

        #create the main results widget
        self.results_widget = QWidget()
        self.results_widget.setLayout(self.results_layout)


        #add the results widget to the stacked layout
        self.stacked_layout.addWidget(self.results_widget)
        self.newButton2.clicked.connect(self.testMessageBox)
    def testMessageBox(self):
        displayText = """
The New Button has been pressed!
"""
        QMessageBox.information(self,"Information Window Title",displayText)

    def show_results(self,query):
        self.model = QSqlQueryModel()
        self.model.setQuery(query)
        self.results_table.setModel(self.model)
        self.results_table.show()
        print("working")
    

    def show_table(self):
        pass
