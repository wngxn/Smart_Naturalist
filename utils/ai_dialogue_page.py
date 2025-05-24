from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QScrollArea, QFrame
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QTextCursor
import requests
import json
import base64
import os
import configparser
import time

class AiDialoguePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        self.load_api_keys()
        
    def init_ui(self):
        # 主布局
        main_layout = QVBoxLayout()
        
        # 标题栏
        title_label = QLabel("非遗语音对话")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            font-size: 20px; 
            font-weight: bold; 
            margin: 15px;
            color: #333;
        """)
        main_layout.addWidget(title_label)
        
        # 添加分隔线
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("margin: 0 20px;")
        main_layout.addWidget(separator)
        
        # 对话历史区域
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        self.chat_history.setStyleSheet("""
            border: none;
            background-color: transparent;
            font-size: 14px;
            padding: 10px;
        """)
        
        # 滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.chat_history)
        scroll_area.setStyleSheet("""
            border: 1px solid #ddd;
            border-radius: 8px;
            margin: 15px;
            background-color: white;
        """)
        main_layout.addWidget(scroll_area)
        
        # 输入区域
        input_layout = QVBoxLayout()
        
        # 输入框
        self.input_field = QTextEdit()
        self.input_field.setMaximumHeight(80)
        self.input_field.setPlaceholderText("输入问题或点击语音按钮进行提问...")
        self.input_field.setStyleSheet("""
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 10px;
            font-size: 14px;
            margin: 0 15px;
        """)
        input_layout.addWidget(self.input_field)
        
        # 按钮布局
        btn_layout = QHBoxLayout()
        
        # 语音按钮
        self.voice_btn = QPushButton("🎤")
        self.voice_btn.setFixedSize(40, 40)
        self.voice_btn.setStyleSheet("""
            QPushButton {
                background-color: #007bff;
                color: white;
                border-radius: 20px;
                font-size: 18px;
                border: none;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.voice_btn.clicked.connect(self.start_listening)
        btn_layout.addWidget(self.voice_btn)
        
        # 占位符
        btn_layout.addStretch()
        
        # 发送按钮
        self.send_btn = QPushButton("发送")
        self.send_btn.setStyleSheet("""
            background-color: #28a745; 
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: bold;
        """)
        self.send_btn.clicked.connect(self.send_message)
        btn_layout.addWidget(self.send_btn)
        
        input_layout.addLayout(btn_layout)
        main_layout.addLayout(input_layout)
        
        # 返回按钮
        self.back_btn = QPushButton("返回主页")
        self.back_btn.setStyleSheet("background-color: #6c757d; padding: 10px 20px;")
        self.back_btn.clicked.connect(lambda: self.parent().parent().stacked_widget.setCurrentIndex(0))
        main_layout.addWidget(self.back_btn)
        # 添加垂直间距
        main_layout.addSpacing(20)
        
        # 设置主布局
        self.setLayout(main_layout)
        
    def start_listening(self):
        """开始语音识别"""
        print("开始语音识别...")
        # 这里可以添加具体的语音识别逻辑
        
    def send_message(self):
        """发送消息"""
        print("发送消息:", self.input_field.toPlainText())
        # 这里可以添加具体的消息发送逻辑
        
    def load_api_keys(self):
        """加载API密钥"""
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.api_keys = {
            'deepseek': config.get('api_keys', 'deepseek'),
            'qwen': config.get('api_keys', 'qwen')
        }
        print("API密钥已加载")