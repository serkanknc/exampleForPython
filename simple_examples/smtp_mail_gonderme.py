import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj =MIMEMultipart() # Mail yapımızı oluşturuyoruz.

mesaj["From"] =  "hunterdiablo07@gmail.com" # Kimden Göndereceğimiz
mesaj["To"] = "hunterdiablo07@gmail.com" # Kime Göndereceğimiz
mesaj["Subject"] = "Smtp Mail Gönderme"  # Mailimizin Konusu

yazi ="""
Python SMTP maili gönderme yazısıdır umarım çalışır tşk bol şans...
-AVCI
"""

mesaj_govde = MIMEText(yazi,"plain") # Mailimizin gövdesini bu sınıftan oluşturuyoruz.
mesaj.attach(mesaj_govde) # Mailimizin gövdesini mail yapımıza ekliyoruz.

try:
    mail =smtplib.SMTP("smtp.gmail.com",587) # SMTP objemizi oluşturuyoruz ve gmail smtp server'ına bağlanıyoruz.
    mail.ehlo()# SMTP serverına kendimizi tanıtıyoruz.
    mail.starttls()# Adresimizin ve Parolamızın şifrelenmesi için gerekli

    mail.login("hunterdiablo07@gmail.com","") # SMTP server'ına giriş yapıyoruz. Kendi mail adresimizi ve parolamızı yapıyoruz
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())# Mailimizi gönderiyoruz.

    print("Mail başarıyla gönderildi...")
    mail.close()# Smtp serverımızın bağlantısını koparıyoz.
except:
    sys.stderr.write("Mail göndermesi başarısız oldu...") # Herhangi bir bağlanma sorunu veya mail gönderme sorunu olursa
    sys.stderr.flush()