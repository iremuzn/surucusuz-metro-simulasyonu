# Kütüphaneler
from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

# İstasyon Sınıfı
class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

# Metro Ağı Sınıfı
class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur

        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. BFS algoritmasını kullanarak en az aktarmalı rotayı bulun
        3. Rota bulunamazsa None, bulunursa istasyon listesi döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın

        İpuçları:
        - collections.deque kullanarak bir kuyruk oluşturun, HINT: kuyruk = deque([(baslangic, [baslangic])])
        - Ziyaret edilen istasyonları takip edin
        - Her adımda komşu istasyonları keşfedin
        """
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar: #başlangıç ve hedef istasyonların varlığının kontrolü
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        kuyruk = deque([(baslangic, [baslangic])]) # kuyruk oluşturma
        ziyaret_edildi = set()

        while kuyruk:
            mevcut, yol = kuyruk.popleft() # kuyruktan ilk istasyonu alma
            if mevcut == hedef: # hedefe ulaşıldıysa yolun çıktısını alma
                return yol

            ziyaret_edildi.add(mevcut) # ziyaret edilen istasyonları ekleme

            for komsu, _ in mevcut.komsular: # komşu istasyonları keşfetme
                if komsu not in ziyaret_edildi and komsu not in yol: # ziyaret edilmeyen komşuların kuyruğa alınması
                    kuyruk.append((komsu, yol + [komsu]))

        return None


    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur

        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. A* algoritmasını kullanarak en hızlı rotayı bulun
        3. Rota bulunamazsa None, bulunursa (istasyon_listesi, toplam_sure) tuple'ı döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın

        İpuçları:
        - heapq modülünü kullanarak bir öncelik kuyruğu oluşturun, HINT: pq = [(0, id(baslangic), baslangic, [baslangic])]
        - Ziyaret edilen istasyonları takip edin
        - Her adımda toplam süreyi hesaplayın
        - En düşük süreye sahip rotayı seçin
        """
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar: #başlangıç ve hedef istasyonlarının kontrolü
          return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

      # (toplam_sure, mevcut_id, mevcut_istasyon, rota_listesi)
        pq = [(0, id(baslangic), baslangic, [baslangic])] # öncelik kuyruğu oluşturma
        ziyaret_edildi = set()

        while pq:
            toplam_sure, _, mevcut, yol = heapq.heappop(pq) # en düşük toplam süreli yolu seçme
            if mevcut == hedef:  # hedefe ulaşıldıysa yol ve sürenin çıktısını alma
                return yol, toplam_sure

            if mevcut in ziyaret_edildi:
                continue

            ziyaret_edildi.add(mevcut) # ziyaret edilen istasyonu ekleme

            for komsu, sure in mevcut.komsular: # istasyonun komşuları üzerinden yeni yollar hesaplama
                if komsu not in ziyaret_edildi:
                    yeni_toplam = toplam_sure + sure # ulaşım süresi hesaplama
                    heapq.heappush(pq, (yeni_toplam, id(komsu), komsu, yol + [komsu])) # yolun kuyruğa alınması

        return None

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()

    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB

    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar

    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören

    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma

    # Test senaryoları
    print("\n=== Test Senaryoları ===")

    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

# Bazı Geliştirmeler

# Başlangıç ve bitiş istasyonlarının kullanıcıdan alındığı fonksiyon
# Kullanıcı başlangıç ve hedef istasyonların ID bilgisini girer
# İki algoritmaya göre en az aktarmalı ve en hızlı rotalar bulunur

def kullanici_girisi(metro: MetroAgi):
    while True:
        print("\n=== Kullanıcı Girişli Metro Simülasyonu ===\n")
        print("❗ Simülasyondan çıkmak için hücreye 'C' yazınız ❗")
        print("🔴 Kırmızı Hat | K1: Kızılay K2: Ulus K3: Demetevler K4: OSB\n🔵 Mavi Hat    | M1: AŞTİ M2: Kızılay M3: Sıhhiye M4: Gar\n🟠 Turuncu Hat | T1: Batıkent T2: Demetevler T3: Gar T4: Keçiören\n")
        baslangic = input("Başlangıç istasyonunu girin (ör. M1, K2, T3): ").upper()
        if baslangic == 'C':
            print("Simülasyonu kullandığınız için teşekkürler!")
            break

        bitis = input("Hedef istasyonunu girin (ör. M4, K3, T2): ").upper()
        if bitis == 'C':
            print("Simülasyonu kullandığınız için teşekkürler!")
            break

        rota = metro.en_az_aktarma_bul(baslangic, bitis)
        def rota_temiz(rota):  # temiz ve açık bir görünüm için art arda tekrar eden istasyonları düzenleyen bir fonksiyon
          yol = []
          onceki = ""
          for ist in rota:
            if ist.ad != onceki:
              yol.append(ist.ad)
              onceki = ist.ad
          print(" -> ".join(yol))


        if rota:
            print("En az aktarmalı rota:")
            rota_temiz(rota)

        sonuc = metro.en_hizli_rota_bul(baslangic, bitis)
        if sonuc:
            rota, sure = sonuc
            print(f"En hızlı rota ({sure} dakika):")
            rota_temiz(rota)
kullanici_girisi(metro)