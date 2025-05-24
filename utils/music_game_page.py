from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class MusicGamePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # 标题
        title = QLabel("非遗音乐游戏")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # 游戏区域
        self.game_label = QLabel("音乐游戏界面开发中...")
        self.game_label.setAlignment(Qt.AlignCenter)
        self.game_label.setStyleSheet("font-size: 16px; color: #666;")
        layout.addWidget(self.game_label)
        
        # 返回按钮
        self.back_btn = QPushButton("返回主页")
        self.back_btn.setStyleSheet("background-color: #6c757d; padding: 10px 20px;")
        self.back_btn.clicked.connect(lambda: self.parent().parent().stacked_widget.setCurrentIndex(0))
        layout.addWidget(self.back_btn)
        
        self.setLayout(layout)