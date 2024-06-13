import mysql.connector
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from close import Ui_close
from database_init import Database
import sys
import bggg
import random

UI = r"assets\ui\Modify_Account.ui"

startup = Database()
mydb = startup.create_table()

class Ui_Register(QtWidgets.QMainWindow):
    accountModified = QtCore.pyqtSignal()
    def __init__(self):
        super(Ui_Register, self).__init__()
        uic.loadUi(UI, self)
        self.Cancel.clicked.connect(self.closeWindow)
        self.Username.textChanged.connect(self.check_inputs)
        self.Password.textChanged.connect(self.check_inputs)
        self.Confirm_Pass.textChanged.connect(self.check_inputs)
        self.FirstName.textChanged.connect(self.check_inputs)
        self.LastName.textChanged.connect(self.check_inputs)
        self.Cancel.clicked.connect(self.open_login)
        self.Save.setShortcut(Qt.Key_Return)
        self.Cancel.setShortcut(Qt.Key_Escape)
        self.connect_db()
        self.check_inputs()  # Check inputs initially
        self.create_account_id()

    def closeWindow(self):
        self.close()

    def check_inputs(self): #checks if all line edits are filled up before enabling save button
        if self.Username.text() != "" and self.Password.text() != "" and self.Confirm_Pass.text() != "" and self.LastName.text() != "" and self.FirstName.text() != "":
            self.Save.setEnabled(True)
        else:
            self.Save.setEnabled(False)

    def modify_account(self):
        try:
            # Your existing code to modify the account

            # Emit the signal to indicate that an account has been modified
            self.accountModified.emit()
        except mysql.connector.Error as err:
            # Error handling
            pass
    def create_account(self):
        try:
            # Your existing code to create the account

            # Emit the signal to indicate that an account has been created
            self.accountModified.emit()
        except mysql.connector.Error as err:
            # Error handling
            pass   


    def connect_db(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="CPET8L",
                database="generaldatabase"
            )
            self.mycursor = self.mydb.cursor()
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def modify_account(self):
        try:
            first_name = self.FirstName.text()
            last_name = self.LastName.text()
            new_username = self.Username.text()
            initial_password = self.Password.text()            
            new_password = self.Confirm_Pass.text()
            if initial_password == new_password:
                update_query = "UPDATE accountmanagement SET user_id = %s, username = %s, password = %s, first_name = %s, last_name = %s WHERE username = 'admin' AND status = 'OWNER'"
                self.mycursor.execute(update_query, ("00000000",new_username, new_password, first_name, last_name))
                self.mydb.commit()
                self.Role.setCurrentIndex(0)
                self.Role.setEnabled(True)
                self.Message(f"Successfully changed default account to user {new_username}.", "Account Setup Success", 1)
                self.open_login()
            else:
                self.Message("Password does not match.", "Error")
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)

    def create_account_id(self):
        key = [str(random.randint(0,9)),
               str(random.randint(0,9)),
               str(random.randint(0,9)),
               str(random.randint(0,9)),
               str(random.randint(0,9)),
               str(random.randint(0,9)),
               str(random.randint(0,9)),
               str(random.randint(0,9)), 
               ]
        return (key[0]+key[1]+key[2]+key[3]+key[4]+key[5]+key[6]+key[7])

    def create_account(self):
        try:
            status = self.Role.currentText()
            first_name = self.FirstName.text()
            last_name = self.LastName.text()
            new_username = self.Username.text()
            initial_password = self.Password.text()            
            new_password = self.Confirm_Pass.text()
            key = self.create_account_id()
            if initial_password == new_password:
                syntax = f'SELECT * FROM accountmanagement WHERE username = "{new_username}"'
                self.mycursor.execute(syntax)
                check = self.mycursor.fetchall()
                print(check)
                if check == None or check == []:
                    syntax = f'SELECT * FROM accountmanagement WHERE user_id = "{key}"'
                    self.mycursor.execute(syntax)
                    check = self.mycursor.fetchall()
                    if check == None or check == []:
                        syntax = "INSERT INTO accountmanagement (user_id, username, password, status, first_name, last_name) VALUES (%s, %s, %s, %s, %s, %s)"
                        self.mycursor.execute(syntax, (key, new_username, new_password, status, first_name, last_name))
                        self.mydb.commit()
                        if status == "CASHIER":
                            #insert default permission assigned to this account
                            self.sql_query = "INSERT INTO Permissions (user_id, Can_search_products, Can_Void_Product, Can_Access_Account_Manager, Can_Access_Manager_Tools, Can_Access_masterlist, Can_Access_Void_list, Can_Access_history_purchase, Can_Access_create_accounts, Can_Access_delete_accounts, is_blacklisted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            self.value = (key ,1, 1, 0, 0, 0, 0, 0, 0, 0, 0)
                            self.mycursor.execute(self.sql_query, (self.value))
                            self.mydb.commit()

                        elif status == "MANAGER":
                            #insert default permission assigned to this account
                            self.sql_query = "INSERT INTO Permissions (user_id, Can_search_products, Can_Void_Product, Can_Access_Account_Manager, Can_Access_Manager_Tools, Can_Access_masterlist, Can_Access_Void_list, Can_Access_history_purchase, Can_Access_create_accounts, Can_Access_delete_accounts, is_blacklisted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            self.value = (key ,1, 1, 1, 1, 1, 1, 1, 0, 0, 0)
                            self.mycursor.execute(self.sql_query, (self.value))
                            self.mydb.commit()

                        self.clear_message()
                        self.Message("Account is successfully created.", "Account creation success", 1)
                        self.close()
                    else:
                        print("same Uid")
                        self.create_account()
                else:
                    self.Message("Username is already taken.", "Error")
            else:
                self.Message("Password does not match.", "Error")
        except mysql.connector.Error as err:
            self.errorDisplay(err.errno, err.sqlstate, err.msg)


    def Message(self, text, title, id = 0):
        if id == 0:
            QtWidgets.QMessageBox.critical(None, title, text)
        
        elif id == 1:
            msg_box = QMessageBox()
            msg_box.setStyleSheet("background-color: white; color: rgba(0, 0, 0, 255);") 
            msg_box.setText(text)
            msg_box.setWindowTitle(title)
            msg_box.exec_()

    def clear_message(self):
        self.LastName.clear()
        self.FirstName.clear()
        self.Username.clear()
        self.Password.clear()
        self.Confirm_Pass.clear()

    def setup(self, type):
        self.Role.clear()
        self.Role.setEnabled(True)
        if type == 0:
            self.Role.addItem("OWNER")
            self.Role.setEnabled(False)
            self.Save.clicked.connect(self.modify_account)
        elif type == 1:
            self.Role.addItems(("CASHIER", "MANAGER"))
            self.Save.clicked.connect(self.create_account)

    def open_login(self): 
        from login import Ui_login
        self.login = Ui_login()
        self.login.show()
        self.close()
    
    def errorDisplay(self, errorCode, sqlstate, text):
        error1 = "Error Code: " + str(errorCode)
        error2 = "SQL State: " + f"{sqlstate}"
        error3 = "Description: " + text
        QtWidgets.QMessageBox.critical(None, "Error", error1 + "\n" + error2 + "\n" + error3)

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Register()
    window.setup(1)
    window.show()
    
    sys.exit(app.exec_())