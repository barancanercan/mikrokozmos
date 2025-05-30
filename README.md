# 🏘️ Toplumsal Mikrokozmos - AI AGENTS VILLAGE

Türkiye'nin toplumsal ve siyasi dinamiklerini yapay zeka destekli karakterler aracılığıyla sanal bir köy ortamında simüle eden interaktif bir proje.

## 📋 Proje Hakkında

Toplumsal Mikrokozmos, farklı toplumsal kesimlerden ve siyasi görüşlerden gelen karakterlerin dijital ikizlerini oluşturarak, gerçek hayattaki etkileşimlerini, kararlarını ve toplumsal olaylara verdikleri tepkileri anlamayı amaçlayan bir simülasyon projesidir.

### 🎯 Temel Özellikler

- **Çeşitli Karakterler**: Farklı siyasi görüşlere ve toplumsal kesimlere mensup karakterler
- **Gerçekçi Etkileşimler**: Karakterlerin kendi kişiliklerine uygun tepkiler vermesi
- **Dinamik Gündem**: Güncel toplumsal olaylara karakterlerin tepkilerini gözlemleme
- **İnteraktif Arayüz**: Streamlit tabanlı kullanıcı dostu arayüz
- **Yapay Zeka Entegrasyonu**: Google Gemini AI modeli ile gerçekçi karakter tepkileri

## 🚀 Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/kullaniciadi/toplumsal-mikrokozmos.git
cd toplumsal-mikrokozmos
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac için
# veya
.\venv\Scripts\activate  # Windows için
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. `.env` dosyası oluşturun ve Gemini API anahtarınızı ekleyin:
```
GEMINI_API_KEY=your_api_key_here
```

## 💻 Kullanım

1. Uygulamayı başlatın:
```bash
streamlit run app.py
```

2. Tarayıcınızda `http://localhost:8501` adresine gidin

3. Arayüzden:
   - Karakterleri seçin
   - Gündemi girin
   - Aktiviteyi seçin
   - Simülasyonu başlatın/durdurun

## 👥 Karakterler

Projede şu karakterler bulunmaktadır:

- **Muhtar Halil**: Tarafsız, köy yöneticisi
- **Emekli Ahmet**: AKP yanlısı, geleneksel değerlere bağlı
- **Genç Elif**: CHP yanlısı, modern ve eleştirel
- **Fadime Teyze**: Küskün/Kararsız seçmen
- **Ali Dayı**: ZP yanlısı, teknoloji meraklısı
- **Cemil Hoca**: İslamcı, köy imamı
- **Ayşe Öğretmen**: HDP yanlısı, idealist
- **Mustafa Abi**: MHP yanlısı, eski asker
- **Aslı Hemşire**: Bağımsız, sağlık çalışanı
- **Hasan Usta**: Geçim odaklı, esnaf

## 🛠️ Teknik Detaylar

- **Dil**: Python 3.12
- **Framework**: Streamlit
- **AI Model**: Google Gemini 1.5 Flash
- **Veri Yapısı**: JSON formatında karakter tanımları
- **Mimari**: Modüler yapı (services, characters, utils)

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 🤝 Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📞 İletişim

Proje Sahibi - [@github_username](https://github.com/github_username)

Proje Linki: [https://github.com/github_username/toplumsal-mikrokozmos](https://github.com/github_username/toplumsal-mikrokozmos) 