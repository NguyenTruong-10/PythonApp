# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
# import sys
# app = QApplication(sys.argv)
# window = QWidget()
# button = QPushButton('Click',window)
# button.setGeometry(100,100, 100,30)

# window.show()
# app.exec()
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, 
    QRadioButton, QHBoxLayout, QGridLayout, QButtonGroup
)
import sys

class InformationForm(QWidget):
    def __init__(self):
        super().__init__()

        # Tạo tiêu đề
        self.setWindowTitle("Personal Information Form")

        # Layout chính
        layout = QVBoxLayout()

        # Tạo GridLayout cho thông tin cá nhân
        grid_layout = QGridLayout()

        # Thêm các label và ô nhập văn bản cho thông tin cá nhân
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        grid_layout.addWidget(self.name_label, 0, 0)
        grid_layout.addWidget(self.name_input, 0, 1)

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        grid_layout.addWidget(self.email_label, 1, 0)
        grid_layout.addWidget(self.email_input, 1, 1)

        self.phone_label = QLabel("Phone Number:")
        self.phone_input = QLineEdit()
        grid_layout.addWidget(self.phone_label, 2, 0)
        grid_layout.addWidget(self.phone_input, 2, 1)

        self.address_label = QLabel("Address:")
        self.address_input = QLineEdit()
        grid_layout.addWidget(self.address_label, 3, 0)
        grid_layout.addWidget(self.address_input, 3, 1)

        self.school_label = QLabel("School:")
        self.school_input = QLineEdit()
        grid_layout.addWidget(self.school_label, 4, 0)
        grid_layout.addWidget(self.school_input, 4, 1)

        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()
        grid_layout.addWidget(self.age_label, 5, 0)
        grid_layout.addWidget(self.age_input, 5, 1)

        # Thêm GridLayout vào layout chính
        layout.addLayout(grid_layout)

        # Câu hỏi giới tính sử dụng RadioButton
        gender_label = QLabel("Gender:")
        layout.addWidget(gender_label)
        gender_layout = QHBoxLayout()

        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)

        layout.addLayout(gender_layout)

        # Các câu hỏi dạng Có hoặc Không
        self.create_yes_no_question(layout, "Do you have a driver's license?", "driver_license")
        self.create_yes_no_question(layout, "Do you like traveling?", "traveling")
        self.create_yes_no_question(layout, "Are you a student?", "student")

        # Button để gửi thông tin
        self.submit_button = QPushButton("Submit")
        layout.addWidget(self.submit_button)

        # Gắn layout vào widget
        self.setLayout(layout)

        # Sự kiện khi nhấn nút
        self.submit_button.clicked.connect(self.submit_info)

    def create_yes_no_question(self, layout, question_text, attribute_name):
        # Tạo câu hỏi dạng RadioButton cho Có/Không
        question_label = QLabel(question_text)
        layout.addWidget(question_label)
        
        question_layout = QHBoxLayout()
        
        yes_radio = QRadioButton("Yes")
        no_radio = QRadioButton("No")
        
        # Tạo nhóm nút radio để người dùng chỉ có thể chọn 1 trong 2
        radio_group = QButtonGroup(self)
        radio_group.addButton(yes_radio)
        radio_group.addButton(no_radio)
        
        # Thêm vào layout
        question_layout.addWidget(yes_radio)
        question_layout.addWidget(no_radio)
        layout.addLayout(question_layout)
        
        # Gán câu trả lời vào thuộc tính động của class
        setattr(self, f"{attribute_name}_yes_radio", yes_radio)
        setattr(self, f"{attribute_name}_no_radio", no_radio)

    def submit_info(self):
        # Lấy dữ liệu từ các trường nhập
        name = self.name_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()
        address = self.address_input.text()
        school = self.school_input.text()
        age = self.age_input.text()
        gender = "Male" if self.male_radio.isChecked() else "Female" if self.female_radio.isChecked() else "Not selected"

        # Lấy dữ liệu từ các câu hỏi Có/Không
        driver_license = "Yes" if self.driver_license_yes_radio.isChecked() else "No" if self.driver_license_no_radio.isChecked() else "Not answered"
        traveling = "Yes" if self.traveling_yes_radio.isChecked() else "No" if self.traveling_no_radio.isChecked() else "Not answered"
        student = "Yes" if self.student_yes_radio.isChecked() else "No" if self.student_no_radio.isChecked() else "Not answered"

        # Hiển thị thông tin
        print(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nAddress: {address}\nSchool: {school}\nAge: {age}\nGender: {gender}")
        print(f"Driver's License: {driver_license}\nLikes Traveling: {traveling}\nIs a Student: {student}")

# Chạy ứng dụng
app = QApplication(sys.argv)
window = InformationForm()
window.show()
app.exec()
