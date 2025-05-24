import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtCore import QFile, QTextStream
from utils.home_page import HomePage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # 初始化页面
        self.home_page = HomePage()
        self.stacked_widget.addWidget(self.home_page)
        
        # 设置窗口属性
        self.setWindowTitle("非遗文化数字体验系统")
        self.setMinimumSize(480, 320)  # 适配3.1寸屏幕
        
    def show_heritage_recognition_page(self):
        """显示非遗场景识别页面"""
        from utils.heritage_recognition_page import HeritageRecognitionPage
        if not hasattr(self, 'heritage_recognition_page'):
            self.heritage_recognition_page = HeritageRecognitionPage()
            self.stacked_widget.addWidget(self.heritage_recognition_page)
        self.stacked_widget.setCurrentWidget(self.heritage_recognition_page)

    def show_ai_dialogue_page(self):
        """显示语音对话页面"""
        from utils.ai_dialogue_page import AiDialoguePage
        if not hasattr(self, 'ai_dialogue_page'):
            self.ai_dialogue_page = AiDialoguePage()
            self.stacked_widget.addWidget(self.ai_dialogue_page)
        self.stacked_widget.setCurrentWidget(self.ai_dialogue_page)

    def show_intelligent_scoring_page(self):
        """显示智能评分页面"""
        from utils.intelligent_scoring_page import IntelligentScoringPage
        if not hasattr(self, 'intelligent_scoring_page'):
            self.intelligent_scoring_page = IntelligentScoringPage()
            self.stacked_widget.addWidget(self.intelligent_scoring_page)
        self.stacked_widget.setCurrentWidget(self.intelligent_scoring_page)

    def show_music_game_page(self):
        """显示音乐游戏页面"""
        from utils.music_game_page import MusicGamePage
        if not hasattr(self, 'music_game_page'):
            self.music_game_page = MusicGamePage()
            self.stacked_widget.addWidget(self.music_game_page)
        self.stacked_widget.setCurrentWidget(self.music_game_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 加载样式表
    style_file = QFile("STYLE.QSS")
    if style_file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(style_file)
        app.setStyleSheet(stream.readAll())
        style_file.close()
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())