import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QSlider
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl


class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Music Player")
        self.setGeometry(100, 100, 300, 200)

        self.player = QMediaPlayer()
        self.player.stateChanged.connect(self.update_state)

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play)

        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop)

        self.volume_label = QLabel("Volume:")
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.valueChanged.connect(self.change_volume)

        self.song_label = QLabel("No song selected")

        layout = QVBoxLayout()
        layout.addWidget(self.play_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.volume_label)
        layout.addWidget(self.volume_slider)
        layout.addWidget(self.song_label)

        self.setLayout(layout)

    def play(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Audio Files (*.mp3 *.ogg *.wav)")
        if filename:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.player.play()
            self.song_label.setText(f"Now playing: {filename}")

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()
        self.song_label.setText("No song selected")

    def change_volume(self, value):
        self.player.setVolume(value)

    def update_state(self, state):
        if state == QMediaPlayer.StoppedState:
            self.song_label.setText("No song selected")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())