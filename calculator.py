from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # 윈도우 속성 설정
        self.setWindowTitle('계산기')
        self.setGeometry(300, 300, 200, 200)
        self.setFixedSize(200, 200)

        # 레이아웃 설정
        layout = QVBoxLayout()
        self.setLayout(layout)

        # QLineEdit 위젯 추가
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        layout.addWidget(self.display)

        # 숫자 버튼 추가
        button_layout = QGridLayout()
        layout.addLayout(button_layout)

        # 숫자 버튼 추가
        for row in range(3):
            for col in range(3):
                button = QPushButton(str(row * 3 + col + 1))
                button.clicked.connect(self.button_clicked)
                button_layout.addWidget(button, row, col)

        # 0 버튼 추가
        zero_button = QPushButton('0')
        zero_button.clicked.connect(self.button_clicked)
        button_layout.addWidget(zero_button, 3, 0)

        # '.' 버튼 추가
        dot_button = QPushButton('.')
        dot_button.clicked.connect(self.button_clicked)
        button_layout.addWidget(dot_button, 3, 1)

        # '=' 버튼 추가
        equal_button = QPushButton('=')
        equal_button.clicked.connect(self.button_clicked)
        button_layout.addWidget(equal_button, 3, 2)

        # 연산자 버튼 추가
        operators = ['+', '-', '*', '/']
        for i, op in enumerate(operators):
            button = QPushButton(op)
            button.clicked.connect(self.button_clicked)
            button_layout.addWidget(button, i, 3)

    def button_clicked(self):
        sender = self.sender()
        if sender.text() == '=':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif sender.text() == 'C':
            self.display.clear()
        else:
            self.display.setText(self.display.text() + sender.text())

if __name__ == "__main__":
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec_()
