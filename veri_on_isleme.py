#  bu dosyadaki kod verilen veri setindeki cümleler üzerinde oynayarak daha temiz veriler elde ettiği yeni csv dosyası oluşturur.

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

# Bu fonksiyon, parametre olarak gönderilen metni 6 adımdan geçirerek daha temiz metin elde eder.
def preprocess_text(text):
    text = text.lower()  # textlerin tamamını küçük harflere çevirme

    text = text.translate(str.maketrans("", "", string.punctuation))  # noktalama işaretlerini kaldırma

    words = word_tokenize(text)  # metni kelimelerine ayırma ve bir liste olarak döndürme

    # internetten alıp üzerinde oynama yaptığım kelime listesini stopwords olarak kullanma
    with open('turkish.txt', 'r') as f:
        my_stopwords = set(f.read().splitlines())
    stopwords_set = set(stopwords.words('turkish'))
    stopwords_set.update(my_stopwords)
    words = [word for word in words if word not in stopwords_set]
    # yani Türkçe'de sık kullanılan ama ifade etmeyen (bu, mi, eğer, ancak gibi) kelimeleri metinlerden kaldırma

    lemmatizer = WordNetLemmatizer()  # kelimelerin eklerini çıkarmak ve köklerini bulmak için kullanılan nltk aracı
    words = [lemmatizer.lemmatize(word) for word in words]  # tüm kelimelerin köklerini bulma
    text = ' '.join(words)  # kelimelere ayırdığımız cümleyi tekrar birleştirme

    return text

# temizlenecek train verisini okuma
import pandas as pd
data = pd.read_csv("dataset/teknofest_train_final.csv", sep="|")
metinler = data["text"]

# DataFrame içindeki tüm satırdaki metinleri temizleme
i = 0
for metin in metinler:
    text = metin
    clean_text = preprocess_text(text)
    data['text'][i] = clean_text
    i = i + 1

# temizlenmiş verisetini yeni bir csv dosyası olarak kaydetme
data.to_csv('teknofest_cleaned_final.csv', sep="|", index=False)

print("Veri seti başarılı bir şekilde temizlendi ve .csv dosyası olarak kaydedildi.")