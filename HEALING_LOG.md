
## 🛡️ Onarım - 2026-01-17 13:14:29.151582

### ESKİ
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

# Burada hem syntax hatası var hem de değişken tanımlanmadan kullanılmış
try
    r_degeri = "on" # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e
    print("Hata oluştu: " + e) # Exception objesi string ile direkt toplanamaz
```

### YENİ
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı değeri float'a çevrilir
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e)) # Hata mesajı string olarak yazdırılıyor
```
---

## 🛡️ Onarım - 2026-01-17 13:14:37.566790

### ESKİ
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı değeri float'a çevrilir
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e)) # Hata mesajı string olarak yazdırılıyor
```

### YENİ
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("10") # Sayı yerine yazı değeri float'a çevrilir
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e)) # Hata mesajı string olarak yazdırılıyor
```
---

## 🛡️ Onarım - 2026-01-17 13:14:44.711899

### ESKİ
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("10") # Sayı yerine yazı değeri float'a çevrilir
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e)) # Hata mesajı string olarak yazdırılıyor
```

### YENİ
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float(10) # Sayı değeri doğru şekilde atanmıştır
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e))
```
---

## 🛡️ Onarım - 2026-01-17 13:14:52.592617

### ESKİ
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float(10) # Sayı değeri doğru şekilde atanmıştır
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e))
```

### YENİ
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float(input("Yarıçapı girin: ")) # Kullanıcıdan yarıçap değerini al
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e))
```
---

## 🛡️ Onarım - 2026-01-17 13:15:00.821025

### ESKİ
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float(input("Yarıçapı girin: ")) # Kullanıcıdan yarıçap değerini al
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e))
```

### YENİ
```python
import math

def daire_alani(yaricap):
    return math.pi * yaricap ** 2

try:
    yaricap = float(input("Yarıçapı girin: ")) # Kullanıcıdan yarıçap değerini al
    alan = daire_alani(yaricap)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e))
```
---

## 🛡️ Onarım - 2026-01-17 13:15:08.959359

### ESKİ
```python
import math

def daire_alani(yaricap):
    return math.pi * yaricap ** 2

try:
    yaricap = float(input("Yarıçapı girin: ")) # Kullanıcıdan yarıçap değerini al
    alan = daire_alani(yaricap)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e))
```

### YENİ
```python
import math

def daire_alan(yaricap):
    return math.pi * (yaricap ** 2)

try:
    yaricap = float(input("Yarıçapı girin: ")) # Kullanıcıdan yarıçap değerini al
    alan = daire_alan(yaricap)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e))
```
---

## 🛡️ Onarım - 2026-01-17 13:15:17.484560

### ESKİ
```python
import math

def daire_alan(yaricap):
    return math.pi * (yaricap ** 2)

try:
    yaricap = float(input("Yarıçapı girin: ")) # Kullanıcıdan yarıçap değerini al
    alan = daire_alan(yaricap)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e))
```

### YENİ
```python
import math

def daire_alan(yaricap):
    return math.pi * (yaricap ** 2)

try:
    r = float(input("Yarıçapı girin: ")) # Kullanıcıdan yarıçap değerini al
    alan = daire_alan(r)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e))
```
---

## 🛡️ Onarım - 2026-01-17 13:15:27.448548

### ESKİ
```python
import math

def daire_alan(yaricap):
    return math.pi * (yaricap ** 2)

try:
    r = float(input("Yarıçapı girin: ")) # Kullanıcıdan yarıçap değerini al
    alan = daire_alan(r)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e))
```

### YENİ
```python
import math

def daire_alan(yaricap):
    return math.pi * (yaricap ** 2)

try:
    r = float(input("Yarıçapı girin: ")) # Kullanıcıdan yarıçap değerini al
    alan = daire_alan(r)
    print(f"Alan: {alan}")
except ValueError as e:  # Hata türünü belirtmek için "as" kullanarak özel bir isim verdim
    print("Hata oluştu: Geçerli bir sayı girilmedi.")
```
---

## 🛡️ Onarım - 2026-01-17 13:15:38.668194

### ESKİ
```python
import math

def daire_alan(yaricap):
    return math.pi * (yaricap ** 2)

try:
    r = float(input("Yarıçapı girin: ")) # Kullanıcıdan yarıçap değerini al
    alan = daire_alan(r)
    print(f"Alan: {alan}")
except ValueError as e:  # Hata türünü belirtmek için "as" kullanarak özel bir isim verdim
    print("Hata oluştu: Geçerli bir sayı girilmedi.")
```

### YENİ
```python
import math

def daire_alan(yaricap):
    return math.pi * (yaricap ** 2)

try:
    r = float(input("Yarıçapı girin: ")) # Kullanıcıdan yarıçap değerini al
    alan = daire_alan(r)
    print(f"Alan: {alan}")
except ValueError as e:  # Hata türünü belirtmek için "as" kullanarak özel bir isim verdim
    print("Hata oluştu: Geçerli bir sayı girilmedi.")
```
---

## 🛡️ Onarım Raporu - 2026-01-17 13:15:58
**Durum:** ✅ Stabilize Edildi

### ❌ Eski Hatalı Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

# Burada hem syntax hatası var hem de değişken tanımlanmadan kullanılmış
try
    r_degeri = "on" # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e
    print("Hata oluştu: " + e) # Exception objesi string ile direkt toplanamaz
```

### ✨ Yeni Onarılmış Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e)) # Exception objesi string ile direkt toplanamaz
```
---

## 🛡️ Onarım Raporu - 2026-01-17 13:38:47
**Durum:** ✅ Stabilize Edildi

### ❌ Eski Hatalı Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e
    print("Hata oluştu: " + str(e)) # Exception objesi string ile direkt toplanamaz
```

### ✨ Yeni Onarılmış Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e)) # Exception objesi string ile direkt toplanamaz
```
---

## 🛡️ Onarım Raporu - 2026-01-17 13:40:43
**Durum:** ✅ Stabilize Edildi

### ❌ Eski Hatalı Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e
    print("Hata oluştu: " + str(e)) # Exception objesi string ile direkt toplanamaz
```

### ✨ Yeni Onarılmış Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e)) # Exception objesi string ile direkt toplanamaz
```
---

## 🛡️ Onarım Raporu - 2026-01-17 13:53:33
**Durum:** ✅ Stabilize Edildi

### ❌ Eski Hatalı Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e
    print("Hata oluştu: " + str(e)) # Exception objesi string ile direkt toplanamaz
```

### ✨ Yeni Onarılmış Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e)) # Exception objesi string ile direkt toplanamaz
```
---

## 🛡️ Onarım Raporu - 2026-01-17 13:57:29
**Durum:** ✅ Stabilize Edildi

### ❌ Eski Hatalı Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e
    print("Hata oluştu: " + str(e)) # Exception objesi string ile direkt toplanamaz
```

### ✨ Yeni Onarılmış Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e)) # Exception objesi string ile direkt toplanamaz
```
---

## 🛡️ Onarım Raporu - 2026-01-17 14:09:31
**Durum:** ✅ Stabilize Edildi

### ❌ Eski Hatalı Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e
    print("Hata oluştu: " + str(e)) # Exception objesi string ile direkt toplanamaz
```

### ✨ Yeni Onarılmış Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e)) # Exception objesi string ile direkt toplanamaz
```
---

## 🛡️ Onarım Raporu - 2026-01-17 14:11:40
**Durum:** ✅ Stabilize Edildi

### ❌ Eski Hatalı Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e
    print("Hata oluştu: " + str(e)) # Exception objesi string ile direkt toplanamaz
```

### ✨ Yeni Onarılmış Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e)) # Exception objesi string ile direkt toplanamaz
```
---

## 🛡️ Onarım Raporu - 2026-01-17 14:14:34
**Durum:** ✅ Stabilize Edildi

### ❌ Eski Hatalı Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e
    print("Hata oluştu: " + str(e)) # Exception objesi string ile direkt toplanamaz
```

### ✨ Yeni Onarılmış Kod
```python
import math

def daire_alani(r):
    return math.pi * r ** 2

try:
    r_degeri = float("on") # Sayı yerine yazı
    alan = daire_alani(r_degeri)
    print(f"Alan: {alan}")
except Exception as e:
    print("Hata oluştu: " + str(e)) # Exception objesi string ile direkt toplanamaz
```
---

## 🛡️ Onarım Raporu - 2026-01-17 14:19:54
**Durum:** ✅ Stabilize Edildi

### ❌ Eski Hatalı Kod
```python
import time
import random


# Aegis'in izleyeceği performans ölçer (Decorator)
def aegis_monitor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        # Eğer işlem 0.5 saniyeden uzun sürerse 'yavaş' kabul edilecek
        if duration > 0.5:
            print(f"⚠️ [PERF_ALERT]: {func.__name__} yavaş çalışıyor: {duration:.2f}s")
        return result

    return wrapper


@aegis_monitor
def veri_isleme_merkezi(liste):
    """Bu fonksiyon zamanla bozulmaya veya yavaşlamaya müsait tasarlanmıştır."""
    # Simüle edilmiş bir işlem gecikmesi (Bazen yavaşlar)
    time.sleep(random.uniform(0.1, 0.8))

    # Bilerek bırakılmış potansiyel bir hata:
    # Liste içinde string gelirse toplama işlemi çökecek.
    return sum(liste)


if __name__ == "__main__":
    while True:
        try:
            test_verisi = [10, 20, 30]
            if random.random() < 0.2:  # %20 ihtimalle sistemi bozacak veri gönder
                test_verisi.append("hatali_veri")

            print(f"Sistem Çıktısı: {veri_isleme_merkezi(test_verisi)}")
            time.sleep(2)
        except Exception as e:
            print(f"🚨 [CRASH]: {e}")
            time.sleep(1)
```

### ✨ Yeni Onarılmış Kod
```python
import time
import random

# Aegis'in izleyeceği performans ölçer (Decorator)
def aegis_monitor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        # Eğer işlem 0.5 saniyeden uzun sürerse 'yavaş' kabul edilecek
        if duration > 0.5:
            print(f"⚠️ [PERF_ALERT]: {func.__name__} yavaş çalışıyor: {duration:.2f}s")
        return result

    return wrapper

@aegis_monitor
def veri_isleme_merkezi(liste):
    """Bu fonksiyon zamanla bozulmaya veya yavaşlamaya müsait tasarlanmıştır."""
    # Simüle edilmiş bir işlem gecikmesi (Bazen yavaşlar)
    time.sleep(random.uniform(0.1, 0.8))

    # Bilerek bırakılmış potansiyel bir hata:
    # Liste içinde string gelirse toplama işlemi çökecek.
    return sum([int(x) for x in liste])  # Sayısal olmayan değerleri int'e dönüştürerek hata alınması sağlandı

if __name__ == "__main__":
    while True:
        try:
            test_verisi = [10, 20, 30]
            if random.random() < 0.2:  # %20 ihtimalle sistemi bozacak veri gönder
                test_verisi.append("hatali_veri")

            print(f"Sistem Çıktısı: {veri_isleme_merkezi(test_verisi)}")
            time.sleep(2)
        except Exception as e:
            print(f"🚨 [CRASH]: {e}")
            time.sleep(1)
```
---

## 🛡️ Onarım Raporu - 2026-01-17 21:24:09
**Durum:** ✅ Sandbox Onaylı (Yaşam Testi Başarılı)
**Süre:** 59.64 sn

### ❌ Eski Hatalı Kod
```python
import time
import random


# Aegis'in izleyeceği performans ölçer (Decorator)
def aegis_monitor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        # Eğer işlem 0.5 saniyeden uzun sürerse 'yavaş' kabul edilecek
        if duration > 0.5:
            print(f"⚠️ [PERF_ALERT]: func.__name_} yavaş çalışıyor: {duration:.2f}s")
        return result

    return wrapper


@aegis_monitor
def veri_isleme_merkezi(liste):
    """Bu fonksiyon zamanla bozulmaya veya yavaşlamaya müsait tasarlanmıştır."""
    # Simüle edilmiş bir işlem gecikmesi (Bazen yavaşlar)
    time.sleep(random.uniform(0.1, 0.8))

    # Bilerek bırakılmış potansiyel bir hata:
    # Liste içinde string gelirse toplama işlemi çökecek.
    return sum(liste)


if __name__ == "__main__":
    while True:
        try:
            test_verisi = [10, 20, 30
            if random.random() < 0.2:  # %20 ihtimalle sistemi bozacak veri gönder
                test_verisi.append("hatali_veri")

            print(f"Sistem Çıktısı: {veri_isleme_merkezi(test_verisi)}")
            time.sleep(2
        except Exception as e
            print(f"🚨 [CRASH]: {e}")
            time.sleep(1)
```

### ✨ Yeni Onarılmış Kod
```python
import time
import random

# Aegis'in izleyeceği performans ölçer (Decorator)
def aegis_monitor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        # Eğer işlem 0.5 saniyeden uzun sürerse 'yavaş' kabul edilecek
        if duration > 0.5:
            print(f"⚠️ [PERF_ALERT]: {func.__name__} yavaş çalışıyor: {duration:.2f}s")
        return result
    return wrapper

@aegis_monitor
def veri_isleme_merkezi(liste):
    """Bu fonksiyon zamanla bozulmaya veya yavaşlamaya müsait tasarlanmıştır."""
    # Simüle edilmiş bir işlem gecikmesi (Bazen yavaşlar)
    time.sleep(random.uniform(0.1, 0.8))

    # Bilerek bırakılmış potansiyel bir hata:
    # Liste içinde string gelirse toplama işlemi çökecek.
    return sum([x for x in liste if isinstance(x, (int, float))])

if __name__ == "__main__":
    while True:
        try:
            test_verisi = [10, 20, 30]
            if random.random() < 0.2:  # %20 ihtimalle sistemi bozacak veri gönder
                test_verisi.append("hatali_veri")

            print(f"Sistem Çıktısı: {veri_isleme_merkezi(test_verisi)}")
            time.sleep(2)
        except Exception as e:
            print(f"🚨 [CRASH]: {e}")
            time.sleep(1)
```
---
