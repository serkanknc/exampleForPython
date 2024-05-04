from doviz_arayuz import *
import sys
from PyQt5.QtWidgets import *
import requests 
from bs4 import BeautifulSoup


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.doviz = self.findChild(QLineEdit,"lineDoviz")
        self.usd = self.findChild(QRadioButton,"radioUSD")
        self.euro = self.findChild(QRadioButton,"radioEuro")
        self.sterlin = self.findChild(QRadioButton,"radioSterlin")
        self.dovizSonuc = self.findChild(QLabel,"labelDovizSonuc")
        self.altin = self.findChild(QLabel,"labelAltin")

        url = "https://www.doviz.com"
        response = requests.get(url)
        html_ierik = response.text

        soup = BeautifulSoup(html_ierik, "html.parser")

        self.dolar_kuru = soup.find("span", {"data-socket-key": "USD"})
        self.euro_kuru = soup.find("span", {"data-socket-key": "EUR"})
        self.sterlin_kuru = soup.find("span", {"data-socket-key": "GBP"})
        self.gram_altin = soup.find("span", {"data-socket-key": "gram-altin"})

        self.ui.pushHesapla.clicked.connect(self.doviz_hesapla)
        self.ui.pushAltinBilgi.clicked.connect(self.altinGetir)
    

    def doviz_hesapla(self):
        
        if(self.usd.isChecked()):
            sayi_dolar = float(self.dolar_kuru.text.replace(",","."))
            lineDolar =float(self.doviz.text())
            sonuc = round((sayi_dolar*lineDolar),2)
            self.dovizSonuc.setText(f"{lineDolar} Dolar {str(sonuc)} TL")
        elif(self.euro.isChecked()):
            sayi_euro = float(self.euro_kuru.text.replace(",","."))
            lineEuro = float(self.doviz.text())
            sonuc = round((sayi_euro * lineEuro),2)
            self.dovizSonuc.setText(f"{lineEuro} Euro {str(sonuc)} TL")
        elif(self.sterlin.isChecked()):
            sayi_sterlin= float(self.sterlin_kuru.text.replace(",","."))
            lineSterlin = float(self.doviz.text())
            sonuc = round((sayi_sterlin * lineSterlin),2)
            self.dovizSonuc.setText(f"{lineSterlin} Sterlin {str(sonuc)} TL")

    def altinGetir(self):
        self.altin.setText(f"Güncel gram altın: {str(self.gram_altin.text)}")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = MyApp()
    pencere.show()
    sys.exit(app.exec_())




