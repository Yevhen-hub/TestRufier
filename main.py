from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt


class RuffierTestApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Налаштування вікна
        self.setWindowTitle("Тест Руф'є")
        self.resize(400, 300)

        # Головний вертикальний layout
        layout = QVBoxLayout()

        # Поля для введення R1
        self.label_r1 = QLabel("Введіть пульс у спокійному стані (R1):")
        self.input_r1 = QLineEdit()
        self.input_r1.setPlaceholderText("Пульс за 15 секунд")

        # Поля для введення R2
        self.label_r2 = QLabel("Введіть пульс після присідань (R2):")
        self.input_r2 = QLineEdit()
        self.input_r2.setPlaceholderText("Пульс за перші 15 секунд")

        # Поля для введення R3
        self.label_r3 = QLabel("Введіть пульс після присідань (R3):")
        self.input_r3 = QLineEdit()
        self.input_r3.setPlaceholderText("Пульс за останні 15 секунд")

        # Кнопка для розрахунку
        self.calculate_button = QPushButton("Розрахувати індекс")
        self.calculate_button.clicked.connect(self.calculate_ruffier_index)

        # Додавання віджетів до layout
        layout.addWidget(self.label_r1)
        layout.addWidget(self.input_r1)
        layout.addWidget(self.label_r2)
        layout.addWidget(self.input_r2)
        layout.addWidget(self.label_r3)
        layout.addWidget(self.input_r3)
        layout.addWidget(self.calculate_button)

        # Налаштування layout для вікна
        self.setLayout(layout)

    def calculate_ruffier_index(self):
        # Отримання даних
        try:
            r1 = int(self.input_r1.text())
            r2 = int(self.input_r2.text())
            r3 = int(self.input_r3.text())
        except ValueError:
            QMessageBox.warning(self, "Помилка вводу", "Будь ласка, введіть числові значення.")
            return

        # Розрахунок індексу
        index = ((4 * (r1 + r2 + r3)) - 200) / 10

        # Оцінка результату
        if index <= 0:
            result = "Висока фізична підготовленість"
        elif 0 < index <= 5:
            result = "Добра фізична підготовленість"
        elif 5 < index <= 10:
            result = "Середня фізична підготовленість"
        elif 10 < index <= 15:
            result = "Задовільна фізична підготовленість"
        else:
            result = "Низька фізична підготовленість"

        # Виведення результату у вікні повідомлення
        QMessageBox.information(
            self,
            "Результат",
            f"Індекс Руф'є: {index:.2f}\nОцінка: {result}"
        )


if __name__ == "__main__":
    app = QApplication([])
    window = RuffierTestApp()
    window.show()
    app.exec_()