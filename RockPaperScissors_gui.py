import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLabel, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QSound
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class RockPaperScissors(QWidget):
    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.computer_score = 0
        self.initUI()
    
    def initUI(self):
        # Create the buttons
        rock_button = QPushButton('Rock')
        paper_button = QPushButton('Paper')
        scissors_button = QPushButton('Scissors')

        # Create a layout and add the buttons
        layout = QVBoxLayout()
        layout.addWidget(rock_button)
        layout.addWidget(paper_button)
        layout.addWidget(scissors_button)
        self.setLayout(layout)

        # Create a label to display the scores
        self.scores_label = QLabel('Scores: User 0 - Computer 0')
        layout.addWidget(self.scores_label)

        # Load the default avatar image
        self.avatar = QPixmap('avatar.jpg')

        # Create a media player to play the sound effects
        self.media_player = QMediaPlayer()

        # Create a label to display the avatar
        self.avatar_label = QLabel()
        self.avatar_label.setPixmap(self.avatar)
        layout.addWidget(self.avatar_label)

        # Resize the avatar image to fit inside a box
        avatar_scaled = self.avatar.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Set the scaled avatar image as the label's pixmap
        self.avatar_label.setPixmap(avatar_scaled)
        layout.addWidget(self.avatar_label)

        # Create a button to allow the user to select an avatar image
        self.select_avatar_button = QPushButton('Select avatar')
        layout.addWidget(self.select_avatar_button)

        # Set the window properties
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Rock-Paper-Scissors')
        self.show()

        # Connect the buttons to the play function
        rock_button.clicked.connect(lambda: self.play('rock'))
        paper_button.clicked.connect(lambda: self.play('paper'))
        scissors_button.clicked.connect(lambda: self.play('scissors'))

        # Connect the select avatar button to the selectAvatar function
        self.select_avatar_button.clicked.connect(self.selectAvatar)

    def selectAvatar(self):
        # Open a file dialog to select an image file
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select Avatar', "", "Images (*.png *.jpg *.jpeg)")

        # Load the selected image file into a pixmap
        self.avatar = QPixmap(file_name)

        # Update the avatar label with the new avatar image
        self.avatar_label.setPixmap(self.avatar)

    def play(self, user_choice):
        # Generate a random choice for the computer
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)

        # Play an inbuilt sound
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile("sound.mp3")))
        self.media_player.play()

        # Determine the winner
        if user_choice == computer_choice:
            result = 'It is a tie'
        elif user_choice == 'rock' and computer_choice == 'scissors':
            result = 'You win!'
            setattr(self, 'user_score', self.user_score + 1)
        elif user_choice == 'paper' and computer_choice == 'rock':
            result = "You win!"
            setattr(self, 'user_score', self.user_score + 1)
        elif user_choice == 'scissors' and computer_choice == 'paper':
            result = "You win!"
            setattr(self, 'user_score', self.user_score + 1)
        else:
            result = "You lose!"
            setattr(self, 'computer_score', self.computer_score + 1)
        
        # Update the scores label
        self.scores_label.setText(f'Scores: User {self.user_score} - Computer {self.computer_score}')
        
        # Show the result in a message box
        QMessageBox.about(self, 'Result', f'You chose {user_choice}, the computer chose {computer_choice}.\n{result}')

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    rps = RockPaperScissors()
    sys.exit(app.exec_())