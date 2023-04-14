# Acikhack2023
# TEKNOFEST 2023 Turkish Natural Language Processing

## Kullandığım Kütüphaneler ve Uygulamayı çalıştırmak için Gerekenler:
pandas -> dataframe işlemleri <br>
nltk -> ön işleme ve verinin temizlenmesi <br>
sklearn -> Verinin eğitilmesi ve model oluşturma <br> 
joblib -> modeli kullanılabilir hale getirme <br>
PyQt5 ve Tkinter -> Kullanıcı arayüzü tasarımı <br> <br>

Bu projede ilk olarak, bana verilen "teknofest_train_final.csv" verisetini aldım ve bu veriyi işleyerek daha temiz hale getirdim.     
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
    
# GUI Kısmı
GUI kısmında ise eğittiğim modeli kullandığım bir arayüz geliştirdim. GUI uygulamasını çalıştırmak için "Gui" klasörü içerisindeki "main.py" dosyasını çalıştırabilirsiniz. <br><br>
## GUI Ana Ekran:
Bu ekranda modelin kullanıldığı ve aşağılayıcı söyleme çözüm geliştiren çeşitli simülasyonlara yönlendiriliyorsunuz.
![image](https://user-images.githubusercontent.com/62249421/230186083-bbd00f22-7d76-4ebb-a239-1508bb3300b1.png)
<br>
Bu arayüzde e-mail atarken, sosyal medyada yorum yazarken ve müşteri hizmetleri ile konuşurken aşağılayıcı bir söylem kullanıldığı tespit edilirse. Söylemi kullanan kullanıcıyı bir forma yönlendiriyor ve bu formda hem daha sakin bir tavra yöneltiyor hem de aşağılayıcı söyleme başvurma sebebini, aşağılayıcı söylemden ne durumda vazgeçeceğini belirterek karşıdaki kişiye bilgi veriyor.
<br>

## E-mail Ekranı:
![image](https://user-images.githubusercontent.com/62249421/230186842-b6b50cc7-fbc9-49aa-96ab-4dcab1bd749a.png)
<br>
Herhangi bir aşağılayıcı söylem tespit edilmediği durumda mail sorunsuz iletilirken:
![image](https://user-images.githubusercontent.com/62249421/230186981-0bcdbc16-ee93-4810-a733-6e56433799c7.png)
<br>
Aşağılayıcı söylem tespiti durumunda kullanıcı uyarı ile karşılaşıyor ve maili iletilmiyor:
<br>
![image](https://user-images.githubusercontent.com/62249421/230187484-b603774d-ce05-46e0-9240-2f6bcfbea2f0.png)
<br>
Bir forma iletiliyor ve bu formda hem sakinleştirilmeye hem de daha nazik bir dil kullanmaya teşvik ediliyor.
![image](https://user-images.githubusercontent.com/62249421/230187835-21c03dd1-c245-4a64-a946-95ae9fab6b49.png)
<br>
Bu formdaki sorularla, kullandığı söylemin kaba olmasıyla yüzleşiyor ve daha nazik bir dile teşvik ediliyor. Karşıdaki kişi ise bu formun sonuçlarını kayıt olarak alabiliyor ve kendini geliştirmek için şikayeti, aşağılayıcı dile maruz kalmadan alıyor.
<br>
<br>
## Sosyal Medya Ekranı:
Bu ekranda ise aynı şekilde normal bir yorum yapmak istediğinde başarılı bir şekilde paylaşabiliyor:<br>
![image](https://user-images.githubusercontent.com/62249421/230190115-4eb3e8ec-e88f-42e2-8878-c772e229d670.png)
<br>
Fakat aşağılayıcı bir söylem kullandığında yeniden forma yönlendiriliyor:<br>
![image](https://user-images.githubusercontent.com/62249421/230190806-1527ec82-c314-4edd-952d-8595d00184ea.png)
<br>
<br>
## Müşteri Hizmetleri Ekranı:
Aynı şekilde burada da kullanıcı bir aşağılayıcı söylem filtrelemesinden geçiyor: <br>
![image](https://user-images.githubusercontent.com/62249421/230191600-bec967cf-c05f-42cf-a5f3-ada0eaefafa1.png)
<br>
<br>
Yönlendirmelerden sonraki formu doldurduktan sonra kaydet butonuyla kullanıcının cevapları kaydedilebilir: <br>
![image](https://user-images.githubusercontent.com/62249421/230193299-76be6423-70a3-4478-9aa7-b27c603a543a.png)
<br>
<br>
Kısacası aşağılayıcı söylemlerin arttığı günümüzde internette daha saygılı ve nazik bir ortamın oluşması için böyle bir uygulama geliştirdim. Formd, arada bir filtreleme ile köprü kurarak karşıdaki kişilerin aşağılayıcı söylemlere maruz kalmasını önlüyor. <br>
Bunun yanında, kullanıcının dilini nazik dile yöneltiyor. <br>
Ayrıca, söyleme maruz kalan kişiye rapor halinde, neden kullanıcıyı bu söyleme ittiğini ve kendini nasıl geliştirebileceğini bildiriyor.

Sunum:

[ERAI-TEKNOFEST2023-tddi-sunum.pptx](https://github.com/gncEray/Acikhack2023/files/11230742/ERAI-TEKNOFEST2023-tddi-sunum.pptx)








  
