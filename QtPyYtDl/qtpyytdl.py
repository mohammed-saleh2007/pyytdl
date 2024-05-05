import sys
from PySide6.QtWidgets import  QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from pytube import YouTube

class InputDialog(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Qt Python YouTube Videos Downloader")
        layout = QVBoxLayout(self)

        # Create a label
        self.label = QLabel("URL:")
        layout.addWidget(self.label)

        # Create a line edit widget
        self.url_edit = QLineEdit()
        layout.addWidget(self.url_edit)

        # Create a label
        self.label = QLabel("Quality:")
        layout.addWidget(self.label)

        # Create a line edit widget
        self.reso_edit = QLineEdit()
        layout.addWidget(self.reso_edit)

        # Create a button
        self.button = QPushButton("Download Video")
        layout.addWidget(self.button)

        # Connect button clicked signal to a slot
        self.button.clicked.connect(self.handle_submit)

    def handle_submit(self):
        # Get the text entered by the user
        video_url = self.url_edit.text()
        video_quality = self.reso_edit.text()
        yt = YouTube(video_url)
        video = yt.streams.filter(only_video=True, resolution=video_quality).first()
        audio_stream = yt.streams.filter(only_audio=True).first()
        video_with_sound = video.includes_audio_track(audio_stream)
        video_with_sound.download()
        self.show_message("Success!", "Your Video Downloaded Successfully on Quality:" + video_quality)

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()


def main():
    app = QApplication(sys.argv)
    dialog = InputDialog()
    dialog.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
