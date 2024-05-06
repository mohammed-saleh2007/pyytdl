import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, QStatusBar
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import requests
from pytube import YouTube


class InputDialog(QWidget):
    def __init__(self):
        super().__init__()

        # Window title
        self.setWindowTitle("Qt Python YouTube Videos Downloader")
        self.layout = QVBoxLayout(self)

        # URL input
        self.label = QLabel("URL:")
        self.layout.addWidget(self.label)

        self.url_edit = QLineEdit()
        self.layout.addWidget(self.url_edit)

        # Check button
        self.check = QPushButton("Check Video")
        self.layout.addWidget(self.check)

        self.check.clicked.connect(self.handle_submit)

        # Create status bar
        self.status_bar = QStatusBar()
        self.layout.addWidget(self.status_bar)

    def handle_submit(self):
        self.check.deleteLater()  # Remove the check button after clicking
        
        video_link = self.url_edit.text()
        yt = YouTube(video_link)
        thumb = yt.thumbnail_url
        streams = yt.streams.filter(file_extension='mp4', progressive=True).order_by("resolution")
        reso_list = {}
        
        for stream in streams:
            reso_list[f"{stream.resolution}@{stream.fps}"] = [stream.resolution, stream.fps]

        size = yt.streams.get_lowest_resolution().filesize_mb
        lable = QLabel(f"file size(Lowest resolution): {size} MB")
        self.layout.addWidget(lable)

        size = yt.streams.get_highest_resolution().filesize_mb
        lable = QLabel(f"file size(highest resolution): {size} MB")
        self.layout.addWidget(lable)

        # Add title label
        label = QLabel(yt.title)
        self.layout.addWidget(label)

        self.setWindowTitle(f"Qt Python YouTube Videos Downloader | {yt.title}")

        # Add thumbnail
        # Fetch image from the URL
        response = requests.get(thumb)
        image_data = response.content

        # Convert image data to QPixmap
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)

        # Resize image while maintaining aspect ratio
        scaled_pixmap = pixmap.scaledToWidth(600)

        # Create QLabel to display the image
        image_label = QLabel()
        image_label.setPixmap(scaled_pixmap)

        # Add QLabel to layout
        self.layout.addWidget(image_label)

        # Add a resolution label
        label = QLabel("Select resolution")
        self.layout.addWidget(label)

        # Add a dropdown menu
        self.selected_reso = QComboBox()
        for i in reso_list.keys():
            self.selected_reso.addItem(i)
        self.layout.addWidget(self.selected_reso)

        # Add Download Button
        self.download = QPushButton("Download")
        self.layout.addWidget(self.download)
        self.download.clicked.connect(self.dl)

        self.status_bar.showMessage("Data Fetched! Ready to download", 10000)

    def dl(self):
        video_link = self.url_edit.text()
        reso = self.selected_reso.currentText()
        yt = YouTube(video_link)
        
        streams = yt.streams.filter(file_extension='mp4', progressive=True).order_by("resolution")
        reso_list = {}
        
        for stream in streams:
            reso_list[f"{stream.resolution}@{stream.fps}"] = [stream.resolution, stream.fps]
        
        for i in reso_list.keys():
            if i == reso:
                video_dl = reso_list[i]

        label = QLabel(f"Downloading Video {yt.title}.mp4 ...")
        self.layout.addWidget(label)  

        yt.streams.filter(res=video_dl[0], fps=video_dl[1]).first().download()
        
        self.show_message("Downloaded!", f"Your Video {yt.title} Downloaded Without any errors")
        self.status_bar.showMessage(f"Your Video {yt.title} Downloaded Without any errors", 10000)
        label = QLabel(f"Video {yt.title}.mp4 Downloaded!\nRelunch the app to download more")
        self.layout.addWidget(label) 

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
