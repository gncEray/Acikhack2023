# Bu python dosyası ön işlenmiş veriyi okuyarak bu veriseti üzerinden bir model oluşturur.

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression  # logistic regression modeli için
from sklearn.metrics import accuracy_score, classification_report  # modelin doğruluğunu ölçmek için

# verisetini yükleme
data = pd.read_csv("dataset/teknofest_cleaned_final.csv", sep="|")
df = data.copy()


count_vect = CountVectorizer()  # CountVectorizer() bir sayma matrisi oluşturur
tfidf_transformer = TfidfTransformer()  # TfidfTransformer() ise sayma matrisi çıktısını TF-IDF matrisine dönüştürür

# Train the feature extraction pipeline on all available data
X_counts = count_vect.fit_transform(df['text'].values.astype('U'))  # fit_transform() yöntemi kullanılarak, her bir kelime için bir sütun oluşturur ve her satır, belgedeki o kelimenin sayısını içerir.
X_tfidf = tfidf_transformer.fit_transform(X_counts)  #TF-IDF, belgedeki her kelimenin önemini hesaplar ve bir skor atar.
# Düşük öneme sahip kelimelerin skoru düşüktür ve yüksek öneme sahip kelimelerin skoru yüksektir.

# logistic regression model tanımlama ve modeli tüm veri üzerinde eğitme
lr = LogisticRegression()
lr.fit(X_tfidf, df['target'])

# doğruluk oranı için predict etme
y_pred = lr.predict(X_tfidf)

# doğruluk (accuracy) oranları
print('Accuracy:', accuracy_score(df['target'], y_pred))
print(classification_report(df['target'], y_pred))

# modeli kaydetme
import joblib  # modeli kaydetmek için joblib kütüphanesi kullandım

try:
    joblib.dump(lr, 'model.joblib')
except:
    print("hata")

print("Model başarılı bir şekilde kaydedildi.")

