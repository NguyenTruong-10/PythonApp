from PyQt6.QtWidgets import QApplication, QMainWindow,QMessageBox
from PyQt6 import uic
import sys
temp_password = ""
temp_user = ""
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/login.ui", self)
        self.btn_login.clicked.connect(self.LoginToMain)
        self.lb_createAccount.mousePressEvent = self.CreateAccount # Ấn label
        print(temp_password)
        print(temp_user)
    def CreateAccount(self,event):
        self.close()
        register.show()
    def LoginToMain(self):
        username = self.edt_username.text()
        password = self.edt_password.text()
        if temp_user != "" and temp_password != "":
            if username == "" or password == "":
                msg_box.setText("Username và password không được để trống")
                msg_box.exec()
            elif username == temp_user and password == temp_password: #Điều kiện tài khoản đúng 
                self.edt_username.setText("")
                self.edt_password.setText("")
                self.close()
                main.show()
            elif username != temp_user: #Điều kiện tài khoản sai 
                msg_box.setText("Không tồn tại tài khoản")
                msg_box.exec()
            else:  # Điều kiện còn lại là username đúng nhưng password sai
                msg_box.setText("Mật khẩu không đúng")
                msg_box.exec()
        else:
            msg_box.setText("Không tồn tại tài khoản")
            msg_box.exec()

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/Regiter.ui", self)
        self.btn_back.clicked.connect(self.BacktoLogin)
    def BacktoLogin(self):
        global temp_user, temp_password # tạo hai biến toàn cục 
        user_name = self.edt_user.text()
        password = self.edt_pass.text()
        confirm_password = self.edt_confirn.text()
        phonenumber = self.edt_number.text()
        temp_user = user_name # gán biến từ lineEdit vào biến cục bộ
        temp_password = password
        if user_name != "" and password !="" and confirm_password !="" and phonenumber !="":
            if confirm_password == password :
                msg_box_confirm.setText("Tao tai khoan thanh cong")
                msg_box_confirm.exec()
                #Reset lai lineEdit
                self.edt_user.setText("")
                self.edt_confirn.setText("")
                self.edt_pass.setText("")
                self.edt_number.setText("")
                self.close()
                window.show()
            elif (confirm_password != password):
                msg_box.setText("Mat khau khong giong nhau")
                msg_box.exec()
        elif user_name == "" or password == "" or confirm_password =="" or phonenumber == "":
                msg_box.setText("Khong duoc de trong")
                msg_box.exec()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/main.ui", self)
        self.bnt_logout.clicked.connect(self.LogoutToLogin)
    def LogoutToLogin(self):
        print("Da mo file login")
        self.close()
        window.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    main = Main()
    register = Register()
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Lỗi")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
    #Mẫu sử dụng một message box khác
    msg_box_confirm = QMessageBox()
    msg_box_confirm.setWindowTitle("Xác nhận")
    msg_box_confirm.setIcon(QMessageBox.Icon.Information)
    msg_box_confirm.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
    window.show()
    app.exec()
