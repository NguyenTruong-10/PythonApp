from PyQt6.QtWidgets import QApplication, QMainWindow,QMessageBox
from PyQt6 import uic
import sys

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)
        self.btn_login.clicked.connect(self.LoginToMain)
        self.lb_createAccount.mousePressEvent = self.CreateAccount # Ấn label
    def CreateAccount(self,event):
        self.close()
        register.show()
    def LoginToMain(self):
        print("Da mo file main")
        username = self.edt_username.text()
        password = self.edt_password.text()
        if username != "" and password != "":
            self.close()
            main.show()
        elif username == "" or password == "":
            msg_box.setText("Username và password không được để trống")
            msg_box.exec()
            #Mẫu sử dụng một message box khác
            # msg_box_confirm.setText("Username và password không được để trống")
            # msg_box_confirm.exec()
class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Regiter.ui", self)
        self.btn_back.clicked.connect(self.BacktoLogin)
    def BacktoLogin(self):
        user_name = self.edt_user.text()
        password = self.edt_pass.text()
        confirm_password = self.edt_confirn.text()
        phonenumber = self.edt_number.text()
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
        uic.loadUi("main.ui", self)
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
