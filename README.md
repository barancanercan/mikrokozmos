# Toplumsal Mikrokozmos

Bu proje, Türkiye'nin toplumsal ve siyasi dinamiklerini yapay zeka destekli karakterler aracılığıyla sanal bir köy ortamında simüle etmeyi amaçlamaktadır.

## Proje Hakkında

Toplumsal Mikrokozmos, farklı sosyal ve siyasi görüşlere sahip karakterlerin bir köy ortamında etkileşimlerini simüle eden bir yapay zeka projesidir. Karakterler, güncel gündem konularına tepki verir, birbirleriyle etkileşime girer ve toplumsal olaylara farklı perspektiflerden yaklaşır.

## Özellikler

- **Çeşitli Karakterler**: Farklı sosyal ve siyasi görüşlere sahip karakterler
- **Gerçekçi Etkileşimler**: Yapay zeka destekli doğal diyaloglar
- **Dinamik Gündem**: Güncel konulara göre tepkiler ve etkileşimler
- **İnteraktif Arayüz**: Streamlit tabanlı kullanıcı dostu arayüz
- **Yapay Zeka Entegrasyonu**: Google'ın Gemini 1.5 Flash modeli ile güçlendirilmiş

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/barancanercan/mikrokozmos.git
cd mikrokozmos
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac için
# veya
.venv\Scripts\activate  # Windows için
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. `.env` dosyası oluşturun ve Gemini API anahtarınızı ekleyin:
```
GEMINI_API_KEY=your_api_key_here
```

## Kullanım

1. Uygulamayı başlatın:
```bash
streamlit run app.py
```

2. Tarayıcınızda `http://localhost:8501` adresine gidin
3. Karakterleri seçin
4. Gündem konusunu girin
5. Aktivite seçin
6. Simülasyonu başlatın ve karakterlerin etkileşimlerini izleyin

## Karakterler

- **Fadime Teyze**: Muhafazakar görüşlü, köy yaşamına bağlı, gelenekçi
- **Aslı Hemşire**: Modern, eğitimli, sosyal demokrat görüşlü
- **Hasan Usta**: İşçi sınıfı, sendikacı, sol görüşlü
- **Mehmet Amca**: Emekli memur, milliyetçi görüşlü
- **Ayşe Hanım**: Ev hanımı, dindar, muhafazakar
- **Ali Bey**: İş adamı, liberal görüşlü
- **Zeynep Öğretmen**: Eğitimci, Atatürkçü, laik
- **Mustafa Dayı**: Çiftçi, köy muhtarı, geleneksel değerlere bağlı

## Teknik Detaylar

- **Programlama Dili**: Python 3.8+
- **Framework**: Streamlit
- **Yapay Zeka Modeli**: Google Gemini 1.5 Flash
- **Veri Yapısı**: JSON
- **Mimari**: Modüler servis tabanlı yapı

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Bir Pull Request oluşturun

## İletişim

Baran Can Ercan - [@barancanercan](https://twitter.com/barancanercan)

Proje Linki: [https://github.com/barancanercan/mikrokozmos](https://github.com/barancanercan/mikrokozmos)