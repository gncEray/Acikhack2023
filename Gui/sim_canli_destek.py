from PyQt5.QtWidgets import *
from ui_canli_destek import Ui_Form
import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pandas as pd
import subprocess

count_vect = CountVectorizer()  # CountVectorizer metni sayısal verilere dönüştürmek için kullanılır
tfidf_transformer = TfidfTransformer()

train = pd.read_csv("dataset/teknofest_cleaned_final.csv", sep="|")
X_sayi = count_vect.fit_transform(train['text'].values.astype('U'))
X_tfidf = tfidf_transformer.fit_transform(X_sayi)

lr = joblib.load('model.joblib')

class Operator(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.operator = Ui_Form()
        self.operator.setupUi(self)

        self.operator.btn_send.mousePressEvent = self.send

    def send(self, checked):
        mesaj = self.operator.textEdit.toPlainText()
        print(mesaj)

        X_new_counts = count_vect.transform([mesaj])
        X_new_tfidf = tfidf_transformer.transform(X_new_counts)
        y_new_pred = lr.predict(X_new_tfidf)

        print(y_new_pred)

        if y_new_pred[0] == 'OTHER':
            print("Mesaj gönderildi")

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Mesaj başarıyla iletildi.")
            msg.setWindowTitle("Gönderildi!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

            self.operator.textEdit.clear()
        else:
            print("Mesaj gönderilmedi!")

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Göndermek istediğiniz mesajda {y_new_pred[0]} içeren bir ifade kullandığınız tespit edildi. Forma yönlendiriliyorsunuz.")
            msg.setWindowTitle("AŞAĞILAYICI SÖYLEM!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

            subprocess.Popen(["python", "uyari_formu.py"]) # forma yönlendirme