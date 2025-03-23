# Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)
Bu proje, Python dilinde geliştirilmiş bir metro simülasyonudur. Başlangıç ve hedef istasyonları arasındaki **en hızlı** ve **en az aktarmalı** rotayı hesaplar ve kullanıcıya sunar. Hesaplamada BFS ve A* algoritmalarından yararlanır.

---
## Kullanılan Teknolojiler ve Kütüphaneler
- Python 3.x
- collections (deque, defaultdict): Varsayılan sözlük ve kuyruk yapısı için kullanıldı.
- headq: A* algoritmasında öncelik kuyruğu oluşturmak için kullanıldı.
- typing: Kodun okunabilirliğini artırmak için kullanıldı.
---
## Algoritmaların Çalışma Mantığı
### BFS (Breadth-First Search)
- BFS, bir geçiş algoritmasıdır. Bir düğümün tüm komşularını ziyaret ederek ilerler. En yakın düğümleri önce ziyaret eder.
- Simülasyonda en az aktarmalı rotayı bulur.
- Başlangıç noktasından en az adımlı olan yolu döndürür.

### A* Algoritması
- A*, her düğümde süre hesaplaması yaparak hedefe en çabuk ulaşmayı sağlayan algoritmadır.
- Simülasyonda en kısa (düşük süreli) rotayı bulur.
- Tüm yolları araştırmak yerine öncelik kuyruğu ile en kısa sürelileri önceliklendirir.
---
## Örnek Kullanım
### Örnek Metro Ağı
| Hat            | İstasyonlar                                                     |
|----------------|-----------------------------------------------------------------|
| **Kırmızı Hat**| K1: Kızılay — K2: Ulus — K3: Demetevler — K4: OSB               |
| **Mavi Hat**   | M1: AŞTİ — M2: Kızılay — M3: Sıhhiye — M4: Gar                  |
| **Turuncu Hat**| T1: Batıkent — T2: Demetevler — T3: Gar — T4: Keçiören          |

### Bağlantı Süreleri
| Bağlantı                  | Süre | Bağlantı                  | Süre |
|---------------------------|------|---------------------------|------|
| Kızılay - Ulus            |   4  | Batıkent - Demetevler     |   7  |
| Ulus - Demetevler         |   6  | Demetevler - Gar          |   9  |
| Demetevler - OSB          |   8  | Gar - Keçiören            |   5  |
| AŞTİ - Kızılay            |   5  | Kızılay Aktarma           |   2  |
| Kızılay - Sıhhiye         |   3  | Demetevler Aktarma        |   3  |
| Sıhhiye - Gar             |   4  | Gar Aktarma               |   2  |

### Örnek Kullanım - Test Sonuçları
#### Senaryo 1 — AŞTİ'den OSB'ye:
- **En az aktarmalı rota:** AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB
- **En hızlı rota (25 dakika):** AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB

#### Senaryo 2 — Batıkent'ten Keçiören'e:
- **En az aktarmalı rota:** Batıkent -> Demetevler -> Gar -> Keçiören
- **En hızlı rota (21 dakika):** Batıkent -> Demetevler -> Gar -> Keçiören

#### Senaryo 3 — Keçiören'den AŞTİ'ye:
- **En az aktarmalı rota:** Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
- **En hızlı rota (19 dakika):** Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
---
## Kullanıcı Girişi Özelliği
- Kullanıcı girişli metro simülasyonu ile tanımlı metro ağındaki başlangıç ve hedef istasyonların ID'leri kullanıcıdan alınır.
- İnteraktif olarak rota hesaplanmasını sağlar.
- İşlemi sonlandırmak için 'C' kodu kullanılır.
---
## Geliştirme Fikirleri
- Arayüzü ve ağ yapısını görselleştirme
- Gerçek şehir haritası entegrasyonu
- Yoğunluk takibi ve aksamaların neden olduğu gecikmelerin hesaba katılması
- Tahmini varış süresi göstergesi
---

