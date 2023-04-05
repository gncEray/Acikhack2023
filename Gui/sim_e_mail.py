from PyQt5.QtWidgets import *
from ui_e_mail import Ui_Form
import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pandas as pd
import subprocess

count_vect = CountVectorizer()  # CountVectorizer metni sayısal verilere dönüştürmek için kullanılır
tfidf_transformer = TfidfTransformer()

train = pd.read_csv("dataset/teknofest_cleaned_final.csv", sep="|")
X_sayi = count_vect.fit_transform(train['text'].values.astype('U'))
X_tfidf = tfidf_transformer.fit_transform(X_sayi)

# hazır modeli yükleme
lr = joblib.load('model.joblib')

class Email(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.email = Ui_Form()
        self.email.setupUi(self)

        self.email.gonder.mousePressEvent = self.send

    def send(self, checked):
        mail = self.email.text_mail.toPlainText()
        print(mail)

        X_new_counts = count_vect.transform([mail])
        X_new_tfidf = tfidf_transformer.transform(X_new_counts)
        y_new_pred = lr.predict(X_new_tfidf)

        print(y_new_pred)

        if y_new_pred[0] == 'OTHER':
            print("Mail gönderildi")

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Mail başarıyla iletildi.")
            msg.setWindowTitle("Gönderildi!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

            self.email.lineEdit.clear()
            self.email.lineEdit_2.clear()
            self.email.text_mail.clear()
        else:
            print("Mail gönderilmedi!")

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"İletmek istediğiniz mailde {y_new_pred[0]} içeren bir ifade kullandığınız tespit edildi. Forma yönlendiriliyorsunuz.")
            msg.setWindowTitle("AŞAĞILAYICI SÖYLEM!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

            subprocess.Popen(["python", "uyari_formu.py"])
            # burada yönlendirme gelecek