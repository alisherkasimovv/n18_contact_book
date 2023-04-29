from PyQt6.QtWidgets import *
from sys import exit
from db_handler import DBHandler
from contact import Contact


class AddContact (QWidget):
    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window

        self.overall = QLabel("Umumiy ma'lumotlar")
        self.first_name = QLineEdit()
        self.first_name.setPlaceholderText("Ism")
        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText("Familiya")
        self.company = QLineEdit()
        self.company.setPlaceholderText("Ish joyi")
        self.gender = QComboBox()
        self.gender.addItems(['Erkak', 'Ayol'])
        self.day = QComboBox()
        self.day.addItems([str(i) for i in range(1, 32)])
        self.month = QComboBox()
        self.month.addItems(["January", "February",
                             "March", "April", "May",
                             "June", "July", "August",
                             "September", "October", "November",
                             "December"])
        self.year = QComboBox()
        self.year.addItems([str(i) for i in range(1990, 2020)])
        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")
        self.phone = QLineEdit()
        self.phone.setPlaceholderText("Phone")

        self.grid = QVBoxLayout()
        self.grid.addWidget(self.overall)
        self.grid.addWidget(self.first_name)
        self.grid.addWidget(self.last_name)
        self.grid.addWidget(self.company)
        self.grid.addWidget(self.gender)

        date = QHBoxLayout()
        date.addWidget(self.day)
        date.addWidget(self.month)
        date.addWidget(self.year)
        self.grid.addLayout(date)

        self.grid.addWidget(QLabel("Qo'shimcha ma'lumotlar"))
        self.grid.addWidget(self.email)
        self.grid.addWidget(self.phone)

        self.cancel = QPushButton("Cancel")
        self.cancel.clicked.connect(lambda: self.close())
        self.clear = QPushButton("Clear")
        self.clear.clicked.connect(self.clear_all)
        self.save = QPushButton("Save")
        self.save.clicked.connect(self.save_data)
        buttonGroup = QHBoxLayout()
        buttonGroup.addWidget(self.cancel)
        buttonGroup.addWidget(self.clear)
        buttonGroup.addWidget(self.save)
        self.grid.addLayout(buttonGroup)

        self.setLayout(self.grid)
    
    def clear_all(self):
        self.first_name.clear()
        self.last_name.clear()
        self.company.clear()
        self.email.clear()
        self.phone.clear()
        self.day.setCurrentIndex(0)
        self.month.setCurrentIndex(0)
        self.year.setCurrentIndex(0)
    
    def save_data(self):
        f = self.first_name.text()
        l = self.last_name.text()
        c = self.company.text()
        e = self.email.text()
        p = self.phone.text()
        g = self.gender.currentIndex()
        d = self.day.currentIndex() + 1
        m = self.month.currentIndex() + 1
        y = self.year.currentText()

        cnt = Contact(f, l, "Male" if g == 0 else "Female", d, m, y, c)
        cnt.add_email(e)
        cnt.add_phone(p)
        self.parent_window.db.create_contact(cnt)
        self.close()