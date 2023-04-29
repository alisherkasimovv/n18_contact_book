from PyQt6.QtWidgets import *
from sys import exit
from db_handler import DBHandler
from ui_add_window import AddContact


class MainWindow (QWidget):
    def __init__(self):
        self.create_window = None
        super().__init__()
        self.db = DBHandler()

        self.v = QVBoxLayout()
        self.setLayout(self.v)

        self.list = QListWidget()
        self.v.addWidget(self.list)

        self.h_box = QHBoxLayout()
        self.add = QPushButton("Add...")
        self.add.clicked.connect(self.open_add_window)
        self.delete = QPushButton("Delete")

        self.h_box.addWidget(self.add)
        self.h_box.addWidget(self.delete)
        self.v.addLayout(self.h_box)
        self.update_screen()

    def update_screen(self):
        data = self.db.get_contact_names()
        self.list.clear()
        for line in data:
            self.list.addItem(line[0])
    
    def open_add_window(self):
        if self.create_window is None:
            self.create_window = AddContact(self)
            self.create_window.show()
        else:
            self.create_window.close()
            self.create_window = None
        
        self.update_screen()


class ContactInfo:
    pass
