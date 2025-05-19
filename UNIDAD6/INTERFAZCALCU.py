import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout

class CalculadoraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora ")
        self.setGeometry(100, 100, 350, 250)
        
        self.initUI()

    def initUI(self):
        self.label1 = QLabel("Ingrese el primer número:", self)
        self.num1_input = QLineEdit(self)
        self.label2 = QLabel("Ingrese el segundo número:", self)
        self.num2_input = QLineEdit(self)
        
        self.result_label = QLabel("", self)

        # Crear botones para cada operación
        self.suma_button = QPushButton("Suma", self)
        self.resta_button = QPushButton("Resta", self)
        self.multi_button = QPushButton("Multiplicación", self)
        self.divi_button = QPushButton("División", self)

        # Conectar cada botón a la función correspondiente
        self.suma_button.clicked.connect(lambda: self.calcular("Suma"))
        self.resta_button.clicked.connect(lambda: self.calcular("Resta"))
        self.multi_button.clicked.connect(lambda: self.calcular("Multiplicación"))
        self.divi_button.clicked.connect(lambda: self.calcular("División"))

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.num1_input)
        layout.addWidget(self.label2)
        layout.addWidget(self.num2_input)
        
        # Layout para los botones
        botones_layout = QHBoxLayout()
        botones_layout.addWidget(self.suma_button)
        botones_layout.addWidget(self.resta_button)
        botones_layout.addWidget(self.multi_button)
        botones_layout.addWidget(self.divi_button)

        layout.addLayout(botones_layout)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calcular(self, operacion):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())

            resultado = ""
            if operacion == "Suma":
                resultado = num1 + num2
            elif operacion == "Resta":
                resultado = num1 - num2
            elif operacion == "Multiplicación":
                resultado = num1 * num2
            elif operacion == "División":
                resultado = num1 / num2 if num2 != 0 else "Error: División por cero"

            self.result_label.setText(f"Resultado: {resultado}")

        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor ingrese números válidos.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = CalculadoraApp()
    ventana.show()
    sys.exit(app.exec_())