# AegisCode: Autonomous Software Homeostasis

AegisCode, yazılım ekosistemlerinde biyolojik homeostaz (iç denge) prensiplerini uygulayan, otonom hata teşhis ve Self-Healing (Kendi Kendini Onarma) ekosistemidir. Geleneksel hata yönetimi yaklaşımlarının ötesine geçerek, yazılımın otonom olarak hayatta kalmasını sağlayan bir dijital bağışıklık sistemi sunar.

## Proje Vizyonu
Yazılımlar doğası gereği statiktir ve beklenmedik durumlarda çökmeye meyillidir. AegisCode, bu statik yapıyı dinamik ve adaptif bir organizma modeline dönüştürür. Yerel LLM teknolojisi ile kodun anatomisini anlık izler, kararsızlık anında ilgili bloğu izole eder ve sistemi durdurmadan onarım yamaları üretir.

## Gelişmiş Mimari Katmanlar
Sistem, birbirine bağlı üç ana katman üzerinden homeostaz sağlar:

1. Perception (Algı Katmanı):
- Real-time Monitoring: watchdog ile dosya sistemi seviyesinde izleme.
- Performance Metrics: Python Decorator'ları aracılığıyla fonksiyonel gecikme ve çalışma zamanı verilerini toplar.

2. Cognition (Bilişsel Katman):
- Semantik Analiz: Yerel DeepSeek-Coder-V2 modeli ile hatanın kök nedenini belirler.
- Strict Logic: Hallucination (uydurma) korumalı, bağlama duyarlı kod üretimi.

3. Actuator (Eyleyici Katmanı):
- Validation Shield: Üretilen kodun syntax doğruluğunu AST (Abstract Syntax Tree) ile denetler.
- Hot-Patching: Sistemi yeniden başlatmaya gerek duymadan patient.py üzerindeki homeostazı sağlar.

## Aegis Dashboard (Command Center)
Geliştirilen PySide6 tabanlı kontrol paneli, sistemin tüm sinir uçlarını görselleştirir:
- Live Signals: Sistem sinyallerinin ve analiz süreçlerinin anlık takibi.
- Code Stabilization View: Onarılan kodun son halinin canlı önizlemesi.
- Latency Counter: AI onarım hızının milisaniye hassasiyetinde ölçümü.

## Teknik Yığın (Tech Stack)
- Dil: Python 3.10+
- Yapay Zeka: DeepSeek-Coder-V2 (Local)
- UI Framework: PySide6
- Gözlemci: Watchdog
- Güvenlik: AST Parsing

## Proje Gelişim Kronolojisi (Milestones)

### [17 Ocak 2026 - 14:00] - Komuta Merkezi v1.4 - v1.7
- Dashboard üzerinden canlı kod önizleme ve onarım süresi ölçümü başarıyla entegre edildi.
- Sistemin kendi yaptığı değişiklikleri döngüye sokmasını engelleyen Write Lock mekanizması eklendi.

### [16 Ocak 2026] - Güvenlik Katmanı
- AST Validation: Üretilen yamaların syntax hatalarından arındırılması için otomatik denetim sistemi kuruldu.

### [15 Ocak 2026] - MVP & Çekirdek Kurulum
- Watchdog ve Ollama entegrasyonu ile ilk Algı-Eylem döngüsü tamamlandı.

## Güvenlik ve Gizlilik Deklarasyonu
Bu proje %100 Yerel (Local) mimari prensiplerine dayanmaktadır. Hiçbir veri bulut servislerine aktarılmaz; tüm analiz ve onarım süreçleri kullanıcının kendi donanımı üzerinde gerçekleştirilir.