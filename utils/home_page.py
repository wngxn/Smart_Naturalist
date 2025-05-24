from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt5.QtCore import Qt

class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        # 主布局
        main_layout = QVBoxLayout()
        
        # 标题标签
        title_label = QLabel("非遗文化体验站")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px;")
        main_layout.addWidget(title_label)
        
        # 欢迎信息
        welcome_label = QLabel("探索中国丰富的非物质文化遗产，体验传统文化的魅力。")
        welcome_label.setWordWrap(True)
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet("font-size: 16px; margin: 10px;")
        main_layout.addWidget(welcome_label)
        
        # 功能区域
        features_layout = QVBoxLayout()
        
        # 创建功能按钮
        buttons_info = [
            {"text": "非遗场景识别\n识别各类非物质文化遗产", "color": "#d73814"},
            {"text": "非遗语音对话\n与非遗文化进行智能对话", "color": "#28a745"},
            {"text": "非遗智能评分\n对非遗技艺进行智能评估", "color": "#007bff"},
            {"text": "非遗音乐游戏\n体验非遗传统音乐魅力", "color": "#ffc107"}
        ]
        
        self.buttons = []
        for btn_info in buttons_info:
            button = QPushButton(btn_info["text"])
            button.setProperty("class", "function-button")
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {btn_info["color"]};
                    color: white;
                    border-radius: 8px;
                    padding: 20px;
                    font-size: 16px;
                    text-align: left;
                    height: 80px;
                }}
                QPushButton:hover {{
                    opacity: 0.9;
                }}
            """)
            
            # 根据按钮类型连接不同的事件处理函数
            if btn_info["text"].startswith("非遗场景识别"):
                button.clicked.connect(self.on_heritage_recognition_clicked)
            elif btn_info["text"].startswith("非遗语音对话"):
                button.clicked.connect(self.on_ai_dialogue_clicked)
            elif btn_info["text"].startswith("非遗智能评分"):
                button.clicked.connect(self.on_intelligent_scoring_clicked)
            else:  # 非遗音乐游戏
                button.clicked.connect(self.on_music_game_clicked)
            
            self.buttons.append(button)
            features_layout.addWidget(button)
        
        # 添加功能区域到主布局
        main_layout.addLayout(features_layout, 1)
        
        # 设置布局
        self.setLayout(main_layout)
    
    def on_heritage_recognition_clicked(self):
        """处理非遗场景识别按钮点击事件"""
        print("非遗场景识别按钮被点击")
        self.parent().parent().show_heritage_recognition_page()
    
    def on_ai_dialogue_clicked(self):
        """处理非遗语音对话按钮点击事件"""
        print("非遗语音对话按钮被点击")
        self.parent().parent().show_ai_dialogue_page()
    
    def on_intelligent_scoring_clicked(self):
        """处理非遗智能评分按钮点击事件"""
        print("非遗智能评分按钮被点击")
        self.parent().parent().show_intelligent_scoring_page()
    
    def on_music_game_clicked(self):
        """处理音乐游戏按钮点击事件"""
        print("音乐游戏按钮被点击")
        self.parent().parent().show_music_game_page()