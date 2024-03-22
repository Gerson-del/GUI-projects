# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mp3_project1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QFileInfo

5
class Ui_play_button(object):
    def setupUi(self, play_button):
        play_button.setObjectName("play_button")
        play_button.resize(530, 303)
        play_button.setFixedSize(530, 303)
        self.centralwidget = QtWidgets.QWidget(play_button)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        #play_button
        self.play_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.play_button_2.setGeometry(QtCore.QRect(110, 190, 62, 58))
        self.play_button_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"C:\Users\gerso\Desktop\Nueva carpeta\GUI\mp3_images\play_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_button_2.setIcon(icon)
        self.play_button_2.setIconSize(QtCore.QSize(50, 50))
        self.play_button_2.setAutoDefault(False)
        self.play_button_2.setDefault(False)
        self.play_button_2.setFlat(True)
        self.play_button_2.setObjectName("play_button_2")
        #pause_button
        self.pause_button = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button.setGeometry(QtCore.QRect(20, 190, 52, 48))
        self.pause_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(r"C:\Users\gerso\Desktop\Nueva carpeta\GUI\mp3_images\Pause-Button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_button.setIcon(icon1)
        self.pause_button.setIconSize(QtCore.QSize(40, 40))
        self.pause_button.setAutoDefault(False)
        self.pause_button.setDefault(False)
        self.pause_button.setFlat(True)
        self.pause_button.setObjectName("pause_button")
        #stop_button
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(200, 190, 52, 48))
        self.stop_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(r"C:\Users\gerso\Desktop\Nueva carpeta\GUI\mp3_images\4029084.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_button.setIcon(icon2)
        self.stop_button.setIconSize(QtCore.QSize(40, 40))
        self.stop_button.setAutoDefault(False)
        self.stop_button.setDefault(False)
        self.stop_button.setFlat(True)
        self.stop_button.setObjectName("stop_button")
        #horizontalSlider
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(340, 210, 160, 22))
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(30, 30, 30, 255), stop:1 rgba(150, 150, 150, 255));")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        #background_button
        self.background_buttons = QtWidgets.QLabel(self.centralwidget)
        self.background_buttons.setEnabled(True)
        self.background_buttons.setGeometry(QtCore.QRect(0, 180, 271, 71))
        self.background_buttons.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(90, 90, 90, 255), stop:1 rgba(190, 190, 190, 255));")
        self.background_buttons.setText("")
        self.background_buttons.setScaledContents(True)
        self.background_buttons.setObjectName("background_buttons")
        #add song button
        self.add_song = QtWidgets.QPushButton(self.centralwidget)
        self.add_song.setGeometry(QtCore.QRect(10, 30, 75, 24))
        self.add_song.setObjectName("addsong")
        self.add_directory = QtWidgets.QPushButton(self.centralwidget)
        #add directory button
        self.add_directory.setGeometry(QtCore.QRect(100, 30, 111, 24))
        self.add_directory.setObjectName("adddirectory")
        #label time
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(240, 20, 231, 51))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.time.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        self.time.setFont(font)
        self.time.setStyleSheet("color: white;")
        self.time.setObjectName("time")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 531, 261))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(r"C:\Users\gerso\Desktop\Nueva carpeta\GUI\mp3_images\spider.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        #rewind button
        self.rewind = QtWidgets.QPushButton(self.centralwidget)
        self.rewind.setGeometry(QtCore.QRect(30, 70, 51, 51))
        self.rewind.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(r"C:\Users\gerso\Desktop\Nueva carpeta\GUI\mp3_images\go_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rewind.setIcon(icon3)
        self.rewind.setIconSize(QtCore.QSize(50, 50))
        self.rewind.setAutoDefault(False)
        self.rewind.setDefault(False)
        self.rewind.setFlat(True)
        self.rewind.setObjectName("rewind")
        #fast forward button
        self.ahead = QtWidgets.QPushButton(self.centralwidget)
        self.ahead.setGeometry(QtCore.QRect(120, 70, 51, 51))
        self.ahead.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(r"C:\Users\gerso\Desktop\Nueva carpeta\GUI\mp3_images\forward_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ahead.setIcon(icon4)
        self.ahead.setIconSize(QtCore.QSize(50, 50))
        self.ahead.setAutoDefault(False)
        self.ahead.setDefault(False)
        self.ahead.setFlat(True)
        self.ahead.setObjectName("ahead")
        #progressBar
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 140, 271, 23))
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.background.raise_()
        self.background_buttons.raise_()
        self.play_button_2.raise_()
        self.pause_button.raise_()
        self.stop_button.raise_()
        self.horizontalSlider.raise_()
        self.add_song.raise_()
        self.add_directory.raise_()
        self.time.raise_()
        self.rewind.raise_()
        self.ahead.raise_()
        self.progressBar.raise_()
        play_button.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(play_button)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 22))
        self.menubar.setObjectName("menubar")
        play_button.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(play_button)
        self.statusbar.setObjectName("statusbar")
        play_button.setStatusBar(self.statusbar)

        #First let's connects the buttons play, pause and stop

        #connecting the play botton :
        self.play_button_2.clicked.connect(self.play_music)
        #connecting the pause botton :
        self.pause_button.clicked.connect(self.pause_music)
        #connecting the stop botton :
        self.stop_button.clicked.connect(self.stop_music)

        #connecting the rewind botton :
        self.rewind.clicked.connect(self.rewind_music)
            
        #connecting the fast forward botton :
        self.ahead.clicked.connect(self.fast_forward_music)

        #This shows the name of the song in the main window:
        self.song_label = QtWidgets.QLabel(self.centralwidget)
        self.song_label.setGeometry(QtCore.QRect(10, 120, 250, 20))
        self.song_label.setObjectName("song_label")

        self.retranslateUi(play_button)
        QtCore.QMetaObject.connectSlotsByName(play_button)

        # Connect the slider's valueChanged signal to a function in your program
        self.horizontalSlider.valueChanged.connect(self.change_volume)
        
        #We connect the clicked button
        self.add_song.clicked.connect(self.add_song_func)
        self.add_directory.clicked.connect(self.add_directory_func)
        self.media_player = QMediaPlayer()
        
        #We set the value of horizontal slider to 50, so it looks better
        self.horizontalSlider.setValue(50)

        self.media_player.positionChanged.connect(self.progress_bar_funct)

        #Update the label time, so it show's you how much of the song is left

        self.media_player.positionChanged.connect(self.remaining_time)
        self.media_player.durationChanged.connect(self.remaining_time)



    def retranslateUi(self, play_button):
        _translate = QtCore.QCoreApplication.translate
        play_button.setWindowTitle(_translate("play_button", "MainWindow"))
        self.add_song.setText(_translate("play_button", "add song"))
        self.add_directory.setText(_translate("play_button", "add directory"))
        self.time.setText(_translate("play_button", "remaining time:"))

    def add_song_func(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("MP3 files (*.mp3)")
        file_dialog.setViewMode(QFileDialog.List)
        file_dialog.setDirectory(QDir.homePath())
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file_path in selected_files:
                # Set the media content and play the selected song
                media_content = QMediaContent(QUrl.fromLocalFile(file_path))
                self.media_player.setMedia(media_content)
                self.media_player.play()
                
                # Extract the filename from the file path
                file_name = QFileInfo(file_path).fileName()
                
                # Update the QLabel with the name of the song
                self.song_label.setText("Now Playing: " + file_name)
                self.song_label.adjustSize()



                
    def add_directory_func(self):
        # Function to handle adding a directory of songs
        directory_dialog = QFileDialog()
        directory_dialog.setFileMode(QFileDialog.Directory)
        directory_dialog.setViewMode(QFileDialog.List)
        directory_dialog.setDirectory(QDir.homePath())
        if directory_dialog.exec_():
            selected_directory = directory_dialog.selectedFiles()
            # Process selected_directory, e.g., add all MP3 files in the directory to the playlist

    # Define the function to change the volume
    def change_volume(self, value):
        
        #Set the volume of your media player
        self.media_player.setVolume(int(value)) 

    def progress_bar_funct(self):
        # total duration of the song
        total_duration = self.media_player.duration()

        if total_duration == 0:
            return
        # Convert durations to seconds for easier calculation
        total_duration_seconds = total_duration / 1000
        current_position_seconds = self.media_player.position() / 1000  


        total_progress = (current_position_seconds / total_duration_seconds) * 100

        self.progressBar.setValue(int(total_progress))

    def remaining_time(self):
        # Retrieve the total duration of the media being played in seconds.
        total_duration_seconds = self.media_player.duration() / 1000
        
        # Retrieve the current playback position in seconds.
        current_position_seconds = self.media_player.position() / 1000 
        
        # Calculate the remaining time in seconds.
        remaining_time_seconds = total_duration_seconds - current_position_seconds
        
        # Check if the remaining time is negative or zero (indicating playback has finished).
        if remaining_time_seconds < 0:
            # If playback has finished or is negative, reset the display to indicate no remaining time.
            self.time.setText("Playback Finished")
        else:
            # Calculate minutes and seconds from remaining time.
            remaining_minutes = int(remaining_time_seconds // 60)
            remaining_seconds = int(remaining_time_seconds % 60)
            
            # Format the remaining time as a string with leading zeros for single-digit minutes and seconds.
            remaining_time_formatted = f"{remaining_minutes:02d}:{remaining_seconds:02d}"
            
            # Update the display with the remaining time.
            self.time.setText(f"Remaining Time: {remaining_time_formatted}")   
    
    #rewind function
    def rewind_music(self):
        """
        Rewind the media playback by 10 seconds.
        """
        # Get the current playback position in milliseconds
        current_position_milliseconds = self.media_player.position()
        
        # Convert the current position to seconds
        current_position_seconds = current_position_milliseconds / 1000

        # Calculate the new position after rewinding by 10 seconds
        new_position_seconds = current_position_seconds - 10

        # Ensure the new position is not negative
        if new_position_seconds < 0:
            new_position_seconds = 0

        # Convert the new position back to milliseconds
        new_position_milliseconds = new_position_seconds * 1000

        # Set the new playback position
        self.media_player.setPosition(int(new_position_milliseconds))

    def fast_forward_music(self):
        """
        Fast forward the media playback by 10 seconds.
        """
        # Get the current playback position in milliseconds
        current_position_milliseconds = self.media_player.position()
        
        # Convert the current position to seconds
        current_position_seconds = current_position_milliseconds / 1000

        # Calculate the new position after rewinding by 10 seconds
        new_position_seconds = current_position_seconds + 10

        # Ensure the new position is not negative
        if new_position_seconds < 0:
            new_position_seconds = 0

        # Convert the new position back to milliseconds
        new_position_milliseconds = new_position_seconds * 1000

        # Set the new playback position
        self.media_player.setPosition(int(new_position_milliseconds))



    #function play button
    def play_music(self):
        if self.media_player.state() != QMediaPlayer.PlayingState:
            self.media_player.play()
    #function pause button
    def pause_music(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
    #function stop button
    def stop_music(self):
        if self.media_player.state() != QMediaPlayer.StoppedState:
            self.media_player.stop()
    


        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    play_button = QtWidgets.QMainWindow()
    ui = Ui_play_button()
    ui.setupUi(play_button)
    play_button.show()
    sys.exit(app.exec_())