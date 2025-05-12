import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QComboBox

class CalculadoraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora ")
        self.setGeometry(100, 100, 350, 200)
        
        self.initUI()

    def initUI(self):
    
        self.label1 = QLabel("Ingrese el primer número:", self)
        self.num1_input = QLineEdit(self)
        self.label2 = QLabel("Ingrese el segundo número:", self)
        self.num2_input = QLineEdit(self)

        self.operacion_label = QLabel("Seleccione la operación:", self)
        self.operacion_combo = QComboBox(self)
        self.operacion_combo.addItems(["Suma", "Resta", "Multiplicación", "División"])

        self.calcular_button = QPushButton("Calcular", self)
        self.result_label = QLabel("", self)

        # Conectar el botón al método
        self.calcular_button.clicked.connect(self.calcular)

      
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.num1_input)
        layout.addWidget(self.label2)
        layout.addWidget(self.num2_input)
        layout.addWidget(self.operacion_label)
        layout.addWidget(self.operacion_combo)
        layout.addWidget(self.calcular_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calcular(self):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
            operacion = self.operacion_combo.currentText()

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