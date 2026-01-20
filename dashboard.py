import sys, time, datetime
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import monitor


# Motor kısmını senin son gönderdiğin stabil yapıya göre güncelledim
class AegisEngine(QThread):
    log_signal = Signal(str)
    code_signal = Signal(str)

    def run(self):
        from watchdog.observers import Observer
        # monitor.py içindeki AegisWatcher'ı miras alıyoruz
        class DashboardWatcher(monitor.AegisWatcher):
            def __init__(self, log_func, code_func):
                super().__init__()
                self.log_func = log_func
                self.code_func = code_func

            def analyze_and_fix(self):
                start = time.time()
                self.log_func("🔍 <span style='color: #00d4ff;'>Bilişsel tarama başlatıldı...</span>")
                super().analyze_and_fix()
                sure = round(time.time() - start, 2)
                self.log_func(f"⚡ <span style='color: #00ff00;'>Homeostaz sağlandı! Süre: {sure} sn</span>")
                with open("patient.py", "r", encoding="utf-8") as f:
                    self.code_func(f.read())

        observer = Observer()
        handler = DashboardWatcher(self.log_signal.emit, self.code_signal.emit)
        observer.schedule(handler, path='.', recursive=False)
        observer.start()
        while True: time.sleep(1)


class AegisDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.repair_count = 0
        self.init_ui()
        self.engine = AegisEngine()
        self.engine.log_signal.connect(self.add_log)
        self.engine.code_signal.connect(self.update_code_view)
        self.engine.start()

    def init_ui(self):
        self.setWindowTitle("🛡️ AegisCode Professional | v1.7")
        self.resize(1200, 800)
        # Arka planı biraz daha yumuşak bir lacivert-siyah yapalım
        self.setStyleSheet("background-color: #0b0e14; color: #d1d5db;")

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # --- MODERN HEADER ---
        header = QFrame()
        header.setStyleSheet("background-color: #151921; border-radius: 20px; border: 1px solid #232936;")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(25, 15, 25, 15)

        title_vbox = QVBoxLayout()
        title = QLabel("AEGISCODE")
        title.setFont(QFont("Segoe UI Black", 22))
        title.setStyleSheet("color: #ffffff; letter-spacing: 3px; border: none;")

        subtitle = QLabel("● AUTOMATED SOFTWARE HOMEOSTASIS UNIT")
        subtitle.setStyleSheet("color: #4ade80; font-size: 10px; font-weight: bold; border: none; letter-spacing: 1px;")

        title_vbox.addWidget(title)
        title_vbox.addWidget(subtitle)
        header_layout.addLayout(title_vbox)

        header_layout.addStretch()

        # Premium Repair Counter
        self.counter = QLabel(f"STABILIZED: {self.repair_count}")
        self.counter.setFixedSize(200, 60)
        self.counter.setAlignment(Qt.AlignCenter)
        self.counter.setStyleSheet("""
            background-color: #1e2530; 
            border: 2px solid #3b82f6; 
            border-radius: 15px; 
            color: #3b82f6; 
            font-family: 'Consolas';
            font-weight: bold; font-size: 16px;
        """)
        header_layout.addWidget(self.counter)
        layout.addWidget(header)

        # --- SPLITTER AREA ---
        splitter = QSplitter(Qt.Horizontal)
        splitter.setStyleSheet("QSplitter::handle { background-color: transparent; }")

        # Left: Logs
        log_widget = QWidget()
        log_layout = QVBoxLayout(log_widget)
        log_layout.setContentsMargins(0, 0, 10, 0)
        log_layout.addWidget(QLabel("SYSTEM SIGNALS", styleSheet="color: #6b7280; font-weight: bold; font-size: 10px;"))

        self.logs = QTextEdit()
        self.logs.setReadOnly(True)
        self.logs.setStyleSheet("""
            QTextEdit {
                background-color: #151921; 
                border: 1px solid #232936; 
                border-radius: 15px; 
                color: #9ca3af; 
                padding: 15px;
                font-family: 'Consolas';
                font-size: 13px;
            }
        """)
        log_layout.addWidget(self.logs)
        splitter.addWidget(log_widget)

        # Right: Code
        code_widget = QWidget()
        code_layout = QVBoxLayout(code_widget)
        code_layout.setContentsMargins(10, 0, 0, 0)
        code_layout.addWidget(
            QLabel("STABILIZED CORE VIEW", styleSheet="color: #6b7280; font-weight: bold; font-size: 10px;"))

        self.code_view = QTextEdit()
        self.code_view.setReadOnly(True)
        self.code_view.setStyleSheet("""
            QTextEdit {
                background-color: #05070a; 
                border: 1px solid #232936; 
                border-radius: 15px; 
                color: #60a5fa; 
                padding: 15px;
                font-family: 'Fira Code', 'Consolas';
                font-size: 13px;
            }
        """)
        code_layout.addWidget(self.code_view)
        splitter.addWidget(code_widget)

        splitter.setSizes([400, 800])
        layout.addWidget(splitter)

        # Footer
        footer = QLabel(f"ENGINE: DEEPSEEK-V2 | LOCALHOST | {datetime.date.today()}")
        footer.setStyleSheet("color: #374151; font-size: 10px; font-weight: bold;")
        layout.addWidget(footer, alignment=Qt.AlignCenter)

    def add_log(self, msg):
        t = datetime.datetime.now().strftime("%H:%M:%S")
        self.logs.append(f"<span style='color: #4b5563;'>[{t}]</span> {msg}")
        if "Homeostaz sağlandı" in msg:
            self.repair_count += 1
            self.counter.setText(f"STABILIZED: {self.repair_count}")

    def update_code_view(self, code):
        self.code_view.setText(code)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AegisDashboard()
    window.show()
    sys.exit(app.exec())