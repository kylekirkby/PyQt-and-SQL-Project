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

        self.results_layout = QVBoxLayout()
        self.results_layout.addWidget(self.results_table)

        self.results_widget = QWidget()
        self.results_widget.setLayout(self.results_layout)

        self.stacked_layout.addWidget(self.results_widget)

        

    def show_results(self,query):
        self.model = QSqlQueryModel()
        self.model.setQuery(query)
        self.results_table.setModel(self.model)
        self.results_table.show()
        print("working")
    

    def show_table(self):
        pass
