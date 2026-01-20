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