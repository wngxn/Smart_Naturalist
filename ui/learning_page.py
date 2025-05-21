from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit
from PyQt5.QtCore import Qt

class LearningPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # 标题
        title = QLabel("非遗语音对话")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # 对话记录
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        layout.addWidget(self.chat_history)
        
        # 输入区域
        self.input_field = QTextEdit()
        self.input_field.setMaximumHeight(100)
        layout.addWidget(self.input_field)
        
        # 按钮布局
        btn_layout = QHBoxLayout()
        self.send_btn = QPushButton("发送")
        self.send_btn.setStyleSheet("background-color: #28a745; padding: 8px 16px;")
        btn_layout.addWidget(self.send_btn)
        
        self.back_btn = QPushButton("返回主页")
        self.back_btn.setStyleSheet("background-color: #6c757d; padding: 8px 16px;")
        self.back_btn.clicked.connect(lambda: self.parent().parent().stacked_widget.setCurrentIndex(0))
        btn_layout.addWidget(self.back_btn)
        
        layout.addLayout(btn_layout)
        self.setLayout(layout)