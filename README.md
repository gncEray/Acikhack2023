# Acikhack2023
# TEKNOFEST 2023 Turkish Natural Language Processing

Bu projede bana verilen "teknofest_train_final.csv" verisetini aldım ve bu veriyi işleyerek daha temiz hale getirdim.     
Bu temizleme yani ön işleme adımlarını daha ayrıntılı bir şekide görmek için "veri_on_isleme.py" isimli dosyaya göz atabilirsiniz.    

## veri_on_isleme.py:
  Ön işleme sırasında dış kaynak olarak "turkish.txt" isimli text dosyasını kullandım. Bu dosyanın içerisinde Türkçe stop_words yani Türkçe'de bir şey anlam ifade etmeyen kelimeler yer alıyor.   
  Text dosyasını https://github.com/ahmetax/trstop/blob/master/dosyalar/turkce-stop-words adresinden indirip üzerine birkaç eklemeler yaparak kullandım.   
  Bu noktada ek bir kaynağa ihtiyaç duymamın sebebi nltk kütüphanesinin Türkçe modülünün zengin olmaması ve model eğitiminde aksaklıklara neden olması.   
  Veriler üzerinde ön işleme yaptıktan sonra "teknofest_cleaned_final.csv" isimli dosyaya kaydettim ve modeli eğitmek için bu temizlenmiş verisetini kullandım.   

Modeli eğittiğim kodlara "model_olusturma.py" dosyasından göz atabilirsiniz.

## "model_olusturma.py":
  Modeli eğitirken sklearn kütüphanesi modüllerini kullandım.  
  Kullandığım modüller:  
&nbsp;&nbsp;&nbsp;&nbsp; CountVectorizer(): CountVectorizer(), doğal dil işleme (NLP) uygulamalarında kullanılan bir özelliktir ve bir dizi metni içeren belgeleri sayısal bir matrise dönüştürmek için kullanılır. Bu matris, her bir metnin her bir kelimesinin sıklığını içeren bir kelime dağılım matrisidir.   <br>
&nbsp;&nbsp;&nbsp;&nbsp; TfidfTransformer(): TfidfTransformer(), doğal dil işleme (NLP) uygulamalarında kullanılan bir özelliktir ve CountVectorizer() ile oluşturulan kelime dağılım matrisini kullanarak, her kelimenin önem derecesini hesaplamak için kullanılır.   
&nbsp;&nbsp;&nbsp;&nbsp; LogisticRegression(): LogisticRegression(), makine öğrenimi ve istatistiksel modellemede kullanılan bir sınıflandırma algoritmasıdır. Bu algoritma, verilerin bağımlı değişkeni (hedef sınıf) ile bir veya daha fazla bağımsız değişkeni (özellikler) arasındaki ilişkiyi modellemek için kullanılır.   
  NLP uygulamalarının olmazsa olmazı CountVectorizer ve TfidfTransformer yanında verilerin tipine ve eğittiğim veriye göre en çok uygunluk seviyesine sahip olduğu için LogisticRegression algoritmasını kullanmayı tercih ettim.   
  En son ise fit ederek oluşturduğum modelimi joblib kütüphanesi kullanarak kaydettim.   
    joblib: Python programlama dili için bir hafıza yönetimi kütüphanesidir. Özellikle makine öğrenimi ve bilimsel hesaplama gibi yüksek hesaplama yükü gerektiren işlemlerde, verilerin bellekte tutulmasına ve işlenmesine yardımcı olur.   
  
