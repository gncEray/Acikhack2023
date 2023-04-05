import tkinter as tk
import tkinter.messagebox as messagebox


class SakinDilFormu:
    def __init__(self, master):
        self.master = master
        master.title("Sakin Dil Formu")

        # Form Label'ı
        self.label = tk.Label(master,
                              text="Kullandığınız dilde nefret ve aşağılayıcı söylem tespit edilmiştir. \nDaha sakin bir dil kullanarak fikirlerinizi ifade etmenizi teşvik etmek için bu forma yönlendirildiniz. \nAşağıdaki sorulara verdiğiniz yanıtlar, düşüncelerinizi açıkça ifade etmenize yardımcı olacaktır.")
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Soru 1 Label'ı
        self.label1 = tk.Label(master,
                               text="1. Düşüncelerinizi ve görüşlerinizi net bir şekilde ifade edebileceğiniz bir alana hoş geldiniz. Lütfen, sizi nefret söylemi kullanmaya iten nedeni aşağıda nazik bir dil ile belirtiniz.")
        self.label1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Soru 1 Text Alanı
        self.text1 = tk.Text(master, height=5, width=50)
        self.text1.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Soru 2 Label'ı
        self.label2 = tk.Label(master,
                               text="2. Aşağıdaki soruları cevaplayarak, bu konular hakkında ne düşündüğünüzü bize söyleyin. Lütfen, sakin ve saygılı bir dil kullanın.")
        self.label2.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Soru 2-1 Label'ı
        self.label2_1 = tk.Label(master,
                                 text="a. Sizce sizin öfkelenmenize neden olan şahıs/topluluk/kurum ne yaparak öfkenizi dindirebilir?")
        self.label2_1.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        # Soru 2-1 Text Alanı
        self.text2_1 = tk.Text(master, height=5, width=50)
        self.text2_1.grid(row=5, column=0, padx=10, pady=10)

        # Soru 2-2 Label'ı
        self.label2_2 = tk.Label(master,
                                 text="b. Sizce başka bir kişi sizi bu dili kullanmaya yönelten durumda olsaydı, aynı şekilde nefret söylemi kullanır mıydı?")
        self.label2_2.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Soru 2-2 Text Alanı
        self.text2_2 = tk.Text(master, height=5, width=50)
        self.text2_2.grid(row=5, column=1, padx=10, pady=10)

        # Soru 3-1 Label'ı
        self.label3_1 = tk.Label(master,
                                 text="3. Son olarak, lütfen yazmak istediğiniz mesajı saygı çerçevesi içinde daha nazik bir dille yeniden yazınız.")
        self.label3_1.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Soru 3-1 Text Alanı
        self.text3_1 = tk.Text(master, height=5, width=50)
        self.text3_1.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Kaydet Butonu
        self.button = tk.Button(master, text="Kaydet", command=self.kaydet)
        self.button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def kaydet(self):
        # Kullanıcının verilerini dosyaya yazma işlemi
        with open("sakin_dil_formu.txt", "a") as f:
            f.write("Soru 1:\n" + self.text1.get("1.0", "end-1c") + "\n")
            f.write("Soru 2-1:\n" + self.text2_1.get("1.0", "end-1c") + "\n")
            f.write("Soru 2-2:\n" + self.text2_2.get("1.0", "end-1c") + "\n")
            f.write("Soru 2-3:\n" + self.text3_1.get("1.0", "end-1c") + "\n")
        # Veri kaydedildikten sonra, kullanıcıya bilgi mesajı verme işlemi
        messagebox.showinfo("Kaydedildi", "Cevaplarınız başarıyla kaydedildi.")


root = tk.Tk()
form = SakinDilFormu(root)
root.mainloop()
