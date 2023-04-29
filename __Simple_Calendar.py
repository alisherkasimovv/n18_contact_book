from PyQt6.QtWidgets import *
from sys import exit
from calendar import month


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v = QVBoxLayout()

        self.h = QHBoxLayout()
        self.year = QLineEdit()
        self.month = QLineEdit()
        self.h.addWidget(self.year)
        self.h.addWidget(self.month)

        self.btn = QPushButton("Print month")
        self.btn.clicked.connect(lambda: self.lbl.setText(month(int(self.year.text()), int(self.month.text()))))
        self.lbl = QLabel()
        self.lbl.setStyleSheet("font-family:'JetBrains Mono'; font-size:50px;")

        self.v.addLayout(self.h)
        self.v.addWidget(self.btn)
        self.v.addWidget(self.lbl)
        self.setLayout(self.v)


if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.show()
    exit(app.exec())
