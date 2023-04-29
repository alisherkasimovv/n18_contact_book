from PyQt6.QtWidgets import *
from sys import exit
from db_handler import DBHandler


class MainWindow (QWidget):
    def __init__(self):
        super().__init__()
        self.db = DBHandler()

        self.v = QVBoxLayout()
        self.setLayout(self.v)

        self.list = QListWidget()
        self.v.addWidget(self.list)

        self.h_box = QHBoxLayout()
        self.add = QPushButton("Add...")
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


class AddContact (QWidget):
    def __init__(self):
        super().__init__()

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

        self.setLayout(self.grid)


class ContactInfo:
    pass


if __name__ == "__main__":
    app = QApplication([])
    win = AddContact()
    win.show()
    exit(app.exec())
