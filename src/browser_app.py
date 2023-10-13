import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class BrowserApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL and press Enter")
        self.url_input.returnPressed.connect(self.navigate_to_url)

        self.back_btn = QPushButton("Back")
        self.back_btn.clicked.connect(self.browser.back)

        self.forward_btn = QPushButton("Forward")
        self.forward_btn.clicked.connect(self.browser.forward)

        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(self.back_btn)
        navigation_layout.addWidget(self.url_input)
        navigation_layout.addWidget(self.forward_btn)

        main_layout = QVBoxLayout()
        main_layout.addLayout(navigation_layout)
        main_layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.show()

    def navigate_to_url(self):
        url = self.url_input.text()
        self.browser.setUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserApp()
    sys.exit(app.exec_())
