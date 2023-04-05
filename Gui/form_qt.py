import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QCheckBox, QPushButton


class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sakin Dil Formu")

        # Başlık etiketi
        self.title_label = QLabel("Sakin Dil Formu", self)
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold")

        # Mesaj etiketi
        self.message_label = QLabel("Düşüncelerinizi yazın", self)

        # Mesaj kutusu
        self.message_box = QTextEdit(self)
        self.message_box.setPlaceholderText("Buraya yazın")
        self.message_box.setStyleSheet("font-size: 16px")

        # Onay kutusu
        self.confirm_box = QCheckBox("Bu formu doldururken sakin bir dil kullandım", self)
        self.confirm_box.setStyleSheet("font-size: 16px")

        # Kaydet butonu
        self.save_button = QPushButton("Kaydet", self)
        self.save_button.setStyleSheet("font-size: 16px")
        self.save_button.clicked.connect(self.on_save_button_clicked)

        # Yatay düzen
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.confirm_box)
        self.h_layout.addWidget(self.save_button)

        # Dikey düzen
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.title_label)
        self.v_layout.addWidget(self.message_label)
        self.v_layout.addWidget(self.message_box)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def on_save_button_clicked(self):
        if self.confirm_box.isChecked():
            message = self.message_box.toPlainText()
            print("Mesaj kaydedildi:", message)
        else:
            print("Lütfen onay kutusunu işaretleyin.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
