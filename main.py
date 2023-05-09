
import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLabel


class FileSorter(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "File Sorter"
        self.left = 50
        self.top = 50
        self.width = 600
        self.height = 400
        self.folder_path = ''
        self.pdf_count = 0
        self.movie_count = 0
        self.music_count = 0
        self.book_count = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.btn_folder = QPushButton('Select Folder', self)
        self.btn_folder.move(50, 50)
        self.btn_folder.clicked.connect(self.select_folder)

        self.lbl_folder = QLabel('No folder selected', self)
        self.lbl_folder.move(200, 55)

        self.btn_sort = QPushButton('Sort Files', self)
        self.btn_sort.move(50, 100)
        self.btn_sort.clicked.connect(self.sort_files)

        self.lbl_pdf = QLabel('PDF files: 0', self)
        self.lbl_pdf.move(200, 105)

        self.lbl_movie = QLabel('Movie files: 0', self)
        self.lbl_movie.move(200, 125)

        self.lbl_music = QLabel('Music files: 0', self)
        self.lbl_music.move(200, 145)

        self.lbl_book = QLabel('Book files: 0', self)
        self.lbl_book.move(200, 165)

    def select_folder(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.lbl_folder.setText(self.folder_path)

    def sort_files(self):
        if self.folder_path:
            for file in os.listdir(self.folder_path):
                if file.endswith('.pdf'):
                    self.pdf_count += 1
                    pdf_dir = os.path.join(self.folder_path, 'PDF')
                    if not os.path.exists(pdf_dir):
                        os.makedirs(pdf_dir)
                    os.rename(os.path.join(self.folder_path, file), os.path.join(pdf_dir, file))

                elif file.endswith(('.mov', '.mp4', '.avi', '.wmv')):
                    self.movie_count += 1
                    movie_dir = os.path.join(self.folder_path, 'Movies')
                    if not os.path.exists(movie_dir):
                        os.makedirs(movie_dir)
                    os.rename(os.path.join(self.folder_path, file), os.path.join(movie_dir, file))

                elif file.endswith(('.mp3', '.wav', '.ogg')):
                    self.music_count += 1
                    music_dir = os.path.join(self.folder_path, 'Music')
                    if not os.path.exists(music_dir):
                        os.makedirs(music_dir)
                    os.rename(os.path.join(self.folder_path, file), os.path.join(music_dir, file))

                elif file.endswith(('.epub', '.mobi')):
                    self.book_count += 1
                    book_dir = os.path.join(self.folder_path, 'Books')
                    if not os.path.exists(book_dir):
                        os.makedirs(book_dir)
                    os.rename(os.path.join(self.folder_path, file), os.path.join(book_dir, file))

            self.lbl_pdf.setText('PDF files: ' + str(self.pdf_count))
            self.lbl_movie.setText('Movie files: ' + str(self.movie_count))
            self.lbl_music.setText('Music files: ' + str(self.music_count))
            self.lbl_book.setText('Book files: ' + str(self.book_count))




if __name__ == "__main__":
    # Create the application and show the window
    app = QApplication([])
    window = FileSorter()
    window.show()
    app.exec_()