from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QProgressBar
from PyQt5.QtCore import Qt

class IntelligentScoringPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # 标题
        title = QLabel("非遗智能评分")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # 评分进度条
        self.score_bar = QProgressBar()
        self.score_bar.setRange(0, 100)
        self.score_bar.setValue(0)
        self.score_bar.setFormat("当前得分: %p%")
        layout.addWidget(self.score_bar)
        
        # 操作按钮
        self.record_btn = QPushButton("开始录音")
        self.record_btn.setStyleSheet("background-color: #007bff; padding: 10px 20px;")
        layout.addWidget(self.record_btn)
        
        # 返回按钮
        self.back_btn = QPushButton("返回主页")
        self.back_btn.setStyleSheet("background-color: #6c757d; padding: 10px 20px;")
        self.back_btn.clicked.connect(lambda: self.parent().parent().stacked_widget.setCurrentIndex(0))
        layout.addWidget(self.back_btn)
        
        self.setLayout(layout)