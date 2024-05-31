from PyQt6.QtWidgets import QApplication, QGridLayout, \
    QVBoxLayout, QLabel, QWidget, QLineEdit, QPushButton, QComboBox
import sys
from datetime import datetime

class DistanceCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create Widgets

        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time: ")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_distance)
        self.output_label = QLabel("")

        self.combo = QComboBox()
        self.combo.addItems(['Kilometers', 'Miles'])

        # Add widgets to grid
        grid.addWidget(distance_label,0,0)
        grid.addWidget(self.distance_line_edit,0,1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(time_label,1,0)
        grid.addWidget(self.time_line_edit,1,1)
        grid.addWidget(calculate_button,2,0,1,2)
        grid.addWidget(self.output_label,3,0,1,2)

        self.setLayout(grid)

    def calculate_distance(self):
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())
        speed = round(distance / time,2)
        if self.combo.currentText() == 'Kilometers':
            metric = "kilometers"
        elif self.combo.currentText() == 'Miles':
            metric = "miles"

        self.output_label.setText(f"Your speed is {speed} {metric} per hour.")

app = QApplication(sys.argv)
distance_calculator = DistanceCalculator()
distance_calculator.show()
sys.exit(app.exec())
