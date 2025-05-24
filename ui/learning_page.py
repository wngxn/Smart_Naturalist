from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QScrollArea, QFrame
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QTextCursor
import requests
import json
import base64
import os
import configparser
import time

class LearningPage(QWidget):
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
        
        # 底部按钮
        bottom_layout = QHBoxLayout()
        
        self.back_btn = QPushButton("返回主页")
        self.back_btn.setStyleSheet("""
            background-color: #6c757d; 
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: bold;
        """)
        self.back_btn.clicked.connect(lambda: self.parent().parent().stacked_widget.setCurrentIndex(0))
        bottom_layout.addWidget(self.back_btn, alignment=Qt.AlignLeft | Qt.AlignBottom)
        
        main_layout.addLayout(bottom_layout)
        
        # 设置主布局
        self.setLayout(main_layout)
        
    def load_api_keys(self):
        """加载API密钥"""
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        
        # 读取DeepSeek API密钥
        self.deepseek_key = self.config.get('API', 'DeepSeekKey', fallback='')
        
        # 读取有道API密钥
        self.youdao_app_key = self.config.get('API', 'YoudaoAppKey', fallback='')
        self.youdao_app_secret = self.config.get('API', 'YoudaoAppSecret', fallback='')
        
    def start_listening(self):
        """开始监听语音输入"""
        self.voice_btn.setText("🛑")
        self.voice_btn.setStyleSheet("""
            background-color: #dc3545;
            color: white;
            border-radius: 20px;
            font-size: 18px;
            border: none;
        """)
        self.voice_btn.clicked.disconnect()
        self.voice_btn.clicked.connect(self.stop_listening)
        
        # 创建并启动语音录制线程
        self.record_thread = RecordThread()
        self.record_thread.finished.connect(self.process_audio)
        self.record_thread.start()
        
    def stop_listening(self):
        """停止监听语音输入"""
        self.voice_btn.setText("🎤")
        self.voice_btn.setStyleSheet("""
            background-color: #007bff;
            color: white;
            border-radius: 20px;
            font-size: 18px;
            border: none;
        """)
        self.voice_btn.clicked.disconnect()
        self.voice_btn.clicked.connect(self.start_listening)
        
        # 停止录音线程
        if hasattr(self, 'record_thread'):
            self.record_thread.stop()
            
    def process_audio(self, audio_data):
        """处理音频数据"""
        if audio_data:
            # 显示用户语音内容
            self.add_message("用户", audio_data)
            
            # 调用DeepSeek API
            self.query_deepseek(audio_data)
            
    def query_deepseek(self, question):
        """调用DeepSeek API进行问答"""
        # 构建请求头
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.deepseek_key}"
        }
        
        # 构建请求体
        data = {
            "model": "deepseek-chat",
            "messages": [
                {
                    "role": "system",
                    "content": "你是一个非遗文化助手，请回答关于非物质文化遗产的问题。你的回答应该准确、易懂，并且包含足够的细节来解释问题。"
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            "max_tokens": 2048,
            "temperature": 0.7,
            "top_p": 1.0
        }
        
        try:
            # 发送API请求
            response = requests.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                # 解析响应
                result = response.json()
                answer = result['choices'][0]['message']['content']
                
                # 显示回答
                self.add_message("非遗助手", answer)
                
                # 调用TTS播放语音
                self.play_tts(answer)
            else:
                raise Exception(f"API请求失败，状态码：{response.status_code}，响应：{response.text}")
                
        except Exception as e:
            # 错误处理
            self.add_message("系统提示", f"发生错误：{str(e)}")
        
    def play_tts(self, text):
        """调用有道TTS播放语音"""
        try:
            # 有道TTS API地址
            url = "https://openapi.youdao.com/ttsapi"
            
            # 生成请求参数
            params = {
                "appKey": self.youdao_app_key,
                "appSecret": self.youdao_app_secret,
                "text": text,
                "langType": "zh-CHS",
                "voiceName": "xiaoyan",
                "audioType": 1
            }
            
            # 发送POST请求
            response = requests.post(url, data=params)
            
            if response.status_code == 200:
                # 保存音频文件
                with open("temp_audio.mp3", "wb") as f:
                    f.write(response.content)
                
                # 模拟播放音频
                self.add_message("系统提示", "正在播放语音回答...")
                
            else:
                raise Exception(f"TTS请求失败，状态码：{response.status_code}，响应：{response.text}")
                
        except Exception as e:
            # 错误处理
            self.add_message("系统提示", f"语音播放出错：{str(e)}")
    
    def send_message(self):
        """发送消息"""
        text = self.input_field.toPlainText().strip()
        if text:
            # 添加到对话历史
            self.add_message("用户", text)
            
            # 清空输入框
            self.input_field.clear()
            
            # 调用DeepSeek API
            self.query_deepseek(text)
    
    def add_message(self, sender, message):
        """添加消息到对话历史"""
        cursor = self.chat_history.textCursor()
        
        # 添加发送者标签
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(f"{sender}:\n")
        cursor.insertText(f"{message}\n\n")
        
        # 滚动到底部
        self.chat_history.verticalScrollBar().setValue(
            self.chat_history.verticalScrollBar().maximum()
        )
    
    def add_tts_typing_indicator(self):
        """添加TTS加载状态"""
        self.tts_typing_label = QLabel("正在生成语音...")
        self.tts_typing_label.setStyleSheet("color: #666; margin: 5px;")
        
        # 直接添加到聊天历史的父容器
        if self.chat_history.parent():
            layout = self.chat_history.parent().layout()
            if layout:
                layout.addWidget(self.tts_typing_label)
            else:
                # 如果没有布局，创建一个新的垂直布局
                new_layout = QVBoxLayout()
                new_layout.addWidget(self.chat_history)
                new_layout.addWidget(self.tts_typing_label)
                self.chat_history.parent().setLayout(new_layout)
        else:
            # 如果聊天历史还没有父容器，创建一个新的垂直布局
            new_layout = QVBoxLayout()
            new_layout.addWidget(self.chat_history)
            new_layout.addWidget(self.tts_typing_label)
            self.chat_history.setLayout(new_layout)
    
    def remove_tts_typing_indicator(self):
        """移除TTS加载状态"""
        if hasattr(self, 'tts_typing_label'):
            self.tts_typing_label.setParent(None)
            self.tts_typing_label.deleteLater()
            del self.tts_typing_label


class RecordThread(QThread):
    """录音线程"""
    finished = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.running = True
        
    def run(self):
        """执行录音任务"""
        # 这里应该实现实际的录音功能
        # 示例代码模拟录音过程
        self.msleep(3000)  # 模拟录音3秒
        
        if not self.running:
            return
            
        # 模拟识别结果
        result = "京剧"
        self.finished.emit(result)
        
    def stop(self):
        """停止录音"""
        self.running = False
        self.quit()
        self.wait()