import requests
from bs4 import BeautifulSoup

# GitHub kullanıcı adınızı girin
kullanici_adi = input("GitHub kullanıcı adınızı girin: ")

# GitHub profil sayfasını çekme
profil_url = f"https://github.com/{kullanici_adi}?tab=repositories"
profil_cevap = requests.get(profil_url)

# Profil sayfasını ayrıştırma
soup = BeautifulSoup(profil_cevap.text, "html.parser")
projeler = []

# Projeleri bulma
proje_etiketleri = soup.find_all("a", itemprop="name codeRepository")
for proje_etiketi in proje_etiketleri:
    proje = proje_etiketi.text.strip()
    projeler.append(proje)

print("Projeler:")
for proje in projeler:
    print("-> " + proje)

# İndirilecek proje adını girin
secilen_proje = input("İndirmek istediğiniz proje adını girin: ")

# Proje indirme işlemi
indirme_url = f"https://github.com/{kullanici_adi}/{secilen_proje}/archive/refs/heads/main.zip"
indirme_cevap = requests.get(indirme_url)

if indirme_cevap.status_code == 200:
    dosya_adi = f"{secilen_proje}.zip"
    with open(dosya_adi, "wb") as dosya:
        dosya.write(indirme_cevap.content)
    print("Proje başarıyla indirildi!")
else:
    print("Proje indirme hatası.")
