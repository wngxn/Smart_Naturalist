from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class ExperiencePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # 标题
        title = QLabel("非遗场景识别")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)
        
        # 摄像头预览区域
        self.camera_label = QLabel("摄像头预览")
        self.camera_label.setFixedSize(320, 240)
        self.camera_label.setStyleSheet("background-color: #333; color: white;")
        layout.addWidget(self.camera_label, 0, Qt.AlignCenter)
        
        # 控制按钮
        btn_layout = QHBoxLayout()
        self.capture_btn = QPushButton("拍照识别")
        self.capture_btn.setStyleSheet("background-color: #d73814; padding: 10px 20px;")
        btn_layout.addWidget(self.capture_btn)
        
        self.back_btn = QPushButton("返回主页")
        self.back_btn.setStyleSheet("background-color: #6c757d; padding: 10px 20px;")
        self.back_btn.clicked.connect(lambda: self.parent().parent().stacked_widget.setCurrentIndex(0))
        btn_layout.addWidget(self.back_btn)
        
        layout.addLayout(btn_layout)
        self.setLayout(layout)