import requests
from bs4 import BeautifulSoup
import random

def film_ara(arama_kelimesi):
    url = f'https://www.imdb.com/find?q={arama_kelimesi}&s=tt&ttype=ft&ref_=fn_ft'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # İlk arama sonucunu bul
    ilk_sonuc = soup.find('td', class_='result_text')
    if not ilk_sonuc:
        print(f"{arama_kelimesi} için sonuç bulunamadı.")
        return None

    # Filmin adını ve bağlantısını al
    film_ad = ilk_sonuc.a.text.strip()
    film_link = 'https://www.imdb.com' + ilk_sonuc.a['href']

    return {'ad': film_ad, 'link': film_link}

def rastgele_film_öner():
    # Rastgele bir film önerisi almak için IMDb ana sayfasını kullanabiliriz
    url = 'https://www.imdb.com/chart/top'

    # Belirli bir sayıda deneme yapalım (örneğin, 10 deneme)
    for _ in range(10):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # IMDb Top 250 listesinden rastgele bir film seç
        film_listesi = soup.find_all('td', class_='titleColumn')

        if film_listesi:
            rastgele_film = random.choice(film_listesi)

            # Seçilen filmin adını ve bağlantısını al
            film_ad = rastgele_film.a.text.strip()
            film_link = 'https://www.imdb.com' + rastgele_film.a['href']

            return {'ad': film_ad, 'link': film_link}

    # Eğer 10 denemede bir film bulunamazsa hata mesajı gönder
    print("Rastgele bir film önerisi bulunamadı.")
    return None

def film_kategori_listesi():
    kategoriler = ['aksiyon', 'komedi', 'drama', 'korku', 'romantik']
    print("Film Kategorileri:")
    for i, kategori in enumerate(kategoriler, start=1):
        print(f"{i}. {kategori.capitalize()}")

    secim = int(input("Lütfen bir kategori seçin (1-5): "))
    return kategoriler[secim - 1]

def ana_menu():
    while True:
        print("\nAna Menü:")
        print("1. Film Ara")
        print("2. Film Öner")
        print("3. Çıkış")

        secim = input("Lütfen bir seçenek girin (1-3): ")

        if secim == '1':
            arama_kelimesi = input("Film arama terimi: ")
            bulunan_film = film_ara(arama_kelimesi)
            if bulunan_film:
                print(f"Bulunan film: {bulunan_film['ad']}")
                print(f"Film bağlantısı: {bulunan_film['link']}")
        elif secim == '2':
            print("Rastgele bir film önerisi:")
            bulunan_film = rastgele_film_öner()
            if bulunan_film:
                print(f"Bulunan film: {bulunan_film['ad']}")
                print(f"Film bağlantısı: {bulunan_film['link']}")
        elif secim == '3':
            print("Çıkış yapılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçenek. Lütfen 1, 2 veya 3 girin.")

if __name__ == "__main__":
    try:
        kategori = film_kategori_listesi()
        print(f"Seçilen kategori: {kategori.capitalize()}")
        ana_menu()
    except Exception as e:
        print(f"Hata oluştu: {e}")
