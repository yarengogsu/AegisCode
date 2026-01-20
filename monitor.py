import time
import ollama
import ast
import datetime
import subprocess
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class AegisWatcher(FileSystemEventHandler):
    def __init__(self):
        # Kilit mekanizması: Kendi yazdığımızı onarmaya çalışmamak için
        self.last_action_time = 0
        self.target_file = "patient.py"
        self.log_file = "HEALING_LOG.md"
        self.temp_sandbox = "_aegis_sandbox_test.py"

    def on_modified(self, event):
        # Sandbox dosyası ve dizin değişikliklerini görmezden gel
        if event.is_directory or self.temp_sandbox in event.src_path:
            return

        # Sadece hedef dosyayı izle
        if event.src_path.endswith(self.target_file):
            current_time = time.time()

            # Yankı (Echo) engelleme: Son işlemden sonraki 10 saniye kritik
            if current_time - self.last_action_time < 10:
                return

            print(f"\n🛡️ [Aegis-Perception]: {self.target_file} üzerinde değişim doğrulandı.")
            self.analyze_and_fix()

    def validate_in_sandbox(self, code):
        """Sürekli çalışan kodlar için gelişmiş dinamik analiz testi."""
        try:
            # 1. Statik Analiz: Yazım hatası var mı?
            ast.parse(code)

            with open(self.temp_sandbox, "w", encoding="utf-8") as f:
                f.write(code)

            # 2. Dinamik Analiz: Kodu başlat
            process = subprocess.Popen(
                ["python", self.temp_sandbox],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="ignore"
            )

            try:
                # Koda 'yaşam kanıtı' sunması için 3 saniye veriyoruz
                # Eğer 3 saniye içinde çökerse stderr dolu gelir
                stdout, stderr = process.communicate(timeout=3)

                # Eğer 3 saniye dolmadan bittiyse ve hata kodu 0 değilse başarısızdır
                if process.returncode != 0:
                    print(f"⚠️ [Aegis-Shield]: Kod başlatılamadı veya çöktü: {stderr}")
                    return False
                return True

            except subprocess.TimeoutExpired:
                # Kod 3 saniye boyunca çökmeden çalışmaya devam ettiyse
                # bu bir 'while True' başarısıdır ve bizim için geçerlidir.
                process.kill()
                return True

        except Exception as e:
            print(f"⚠️ [Aegis-Shield]: Sandbox hatası: {e}")
            return False
        finally:
            if os.path.exists(self.temp_sandbox):
                os.remove(self.temp_sandbox)

    def save_log(self, old_code, new_code, duration):
        """Detaylı onarım raporunu dökümante eder."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"\n## 🛡️ Onarım Raporu - {timestamp}\n**Durum:** ✅ Sandbox Onaylı (Yaşam Testi Başarılı)\n**Süre:** {duration} sn\n\n### ❌ Eski Hatalı Kod\n```python\n{old_code}\n```\n\n### ✨ Yeni Onarılmış Kod\n```python\n{new_code}\n```\n---\n"
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry)
        print(f"📝 [Aegis-Log]: Rapor sisteme işlendi.")

    def analyze_and_fix(self):
        try:
            with open(self.target_file, "r", encoding="utf-8") as f:
                broken_code = f.read()

            if not broken_code.strip():
                return

            start_time = time.time()
            print("🧠 [Aegis-Cognition]: DeepSeek-Coder-V2 analiz ve onarım sürecinde...")

            prompt = f"""
            Sen AegisCode'un onarım modülüsün. Aşağıdaki Python kodunu onar:
            KOD:
            {broken_code}

            KESİN TALİMATLAR:
            1. SADECE mevcut değişken isimlerini kullan. 
            2. Markdown (```) kullanma.
            3. Asla açıklama yapma, sadece kodu döndür.
            4. Kodun sürekli çalışma (while True) yapısını bozma.
            """

            response = ollama.generate(model='deepseek-coder-v2:latest', prompt=prompt)
            fixed_code = response['response'].strip()

            # Markdown temizliği
            if "```" in fixed_code:
                lines = fixed_code.split("\n")
                filtered_lines = [line for line in lines if
                                  not (line.startswith("```") or line.strip().lower() == "python")]
                fixed_code = "\n".join(filtered_lines).strip()

            print("🛡️ [Aegis-Shield]: Sandbox Yaşam Testi başlatılıyor...")
            if self.validate_in_sandbox(fixed_code):

                with open(self.target_file, "w", encoding="utf-8") as f:
                    f.write(fixed_code)

                # Yazma biter bitmez kilidi tazele
                self.last_action_time = time.time()

                duration = round(self.last_action_time - start_time, 2)
                print(f"✨ [Aegis-Healer]: Homeostaz sağlandı. Süre: {duration}sn")
                self.save_log(broken_code, fixed_code, duration)
            else:
                print("🚨 [Aegis-Shield]: Onarılan kod yaşam testini geçemedi. Müdahale reddedildi.")
                self.last_action_time = time.time()

        except Exception as e:
            print(f"❌ Kritik Hata: {e}")
            self.last_action_time = time.time()


if __name__ == "__main__":
    observer = Observer()
    handler = AegisWatcher()
    observer.schedule(handler, path='.', recursive=False)

    print("=" * 50)
    print("🛡️ AegisCode v1.8.2 - Continuous Execution Support")
    print("🛡️ Anti-Echo & Live-Sandbox System Active")
    print("=" * 50)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛡️ AegisCode kapatıldı.")
    observer.join()