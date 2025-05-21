import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtCore import QFile, QTextStream
from ui.home_page import HomePage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # 初始化页面
        self.home_page = HomePage()
        self.stacked_widget.addWidget(self.home_page)
        
        # 设置窗口属性
        self.setWindowTitle("非遗文化体验站")
        self.setMinimumSize(480, 320)  # 适配3.1寸屏幕
        
    def show_experience_page(self):
        """显示非遗场景识别页面"""
        from ui.experience_page import ExperiencePage
        if not hasattr(self, 'experience_page'):
            self.experience_page = ExperiencePage()
            self.stacked_widget.addWidget(self.experience_page)
        self.stacked_widget.setCurrentWidget(self.experience_page)

    def show_learning_page(self):
        """显示AI对话页面"""
        from ui.learning_page import LearningPage
        if not hasattr(self, 'learning_page'):
            self.learning_page = LearningPage()
            self.stacked_widget.addWidget(self.learning_page)
        self.stacked_widget.setCurrentWidget(self.learning_page)

    def show_intelligent_scoring_page(self):
        """显示智能评分页面"""
        from ui.scoring_page import ScoringPage
        if not hasattr(self, 'scoring_page'):
            self.scoring_page = ScoringPage()
            self.stacked_widget.addWidget(self.scoring_page)
        self.stacked_widget.setCurrentWidget(self.scoring_page)

    def show_music_game_page(self):
        """显示音乐游戏页面"""
        from ui.music_game_page import MusicGamePage
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