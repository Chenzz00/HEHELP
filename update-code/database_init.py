
import mysql.connector
from mysql.connector import errorcode

#pls put the items here :)
items = [(1906949,"Emperador Gold | Philippines Fruit Brandy 750ml",189,"ALCOHOL"),
(1131822,"Alfonso I Platinum - Spanish Brandy de Jerez 700ml", 399, "ALCOHOL"), (1410925,"Fundador Ultra Smooth - Spanish Brandy de Jerez 750ml", 479,"ALCOHOL"),
(1068737, "All Purpose Flour - Wooden Spoon 1kg" ,168,"BAKING"), (1172728, "Whole Wheat Flour - Philippine Foremost 1kg", 230, "BAKING"), (1543398,	"Dutche Dark Pure Alkalized Cocoa Powder 1kg", 430, "BAKING"),
(1777760, "Lotte Mandarin Orange Juice Drink 1L", 114, "BEVERAGE"),
(1351420,	"DEL Monte Pineapple Juice Drink 1L", 140,	"BEVERAGE"),
(1874545,	"Pepsi Cola Regular Drink 1.5L",	102,	"BEVERAGE"),
(1859644,	"Monde Wheat Bread 400g",	158,	"BREAD"),
(1194093,	"Gardenia Thick Sliced White Bread Classic Loaf 600g",	85,	"BREAD"),
(1527888,	"SariMonde Pinoy Tasty Bread 450g",	38,	"BREAD"),
(1366242,	"Quaker Oat Meal Cookies 27g",	24,	"BREAKFAST"),
(1926512,	"Koko Krunch Breakfast Cerel 15g Pack of 12",	83,	"BREAKFAST"),
(1648502,	"Gold Corn Flakes Cereal Breakfast 500g",	202,	"BREAKFAST"),
(1720900,	"Nerds Gummy Clusters Candy", 125,	"CANDY"),
(1792084,	"Sour Patch Kids Lollies 170g Original",	79,	"CANDY"),
(1354716,	"Vita Cubes Fruit Flavored Jelly Candy Singles 90g x 20pcs",	49,	"CANDY"),
(1599359,	"Hormel Spam Regular Luncheon Meat 340g",	262,	"CANNED"),
(1220053,	"Jolly Pieces Steams Mushroom 400g",	57,	"CANNED"),
(1753735,	"555 Sardines in Tomato Sauces 155g",	24,	"CANNED"),
(1856081,	"Silver Swan Soy Sauce 1L",	48,	"CONDIMENT"),
(1156695,	"Panda Oyster Sauce",	169,	"CONDIMENT"),
(1510347,	"McCornick Black Pepper Whole 29g",	102,	"CONDIMENT"),
(1441718,	"Creamcheese Anchor 1kg", 570,	"DAIRY"),
(1990067,	"Mozzarella Cheese Arla Block 2.3kg", 1420, "DAIRY"),
(1207403,	"Birch Tree Cream Milk Powder 300g",	145,	"DAIRY"),
(1563680,	"Purefoods Deli Beef Bacon 200g", 382, "DELI"),
(1185440,	"Purefoods Deli Angus Beef Franks 500g",	296,	"DELI"),
(1562974,	"Purefoods Deli Breakfast Sausage 240g",	242,	"DELI"),
(1852027,	"Bounty Fresh Sari Sarap Honey 500g",	139,	"FROZEN"),
(1883200,	"CDO Premium Cheesy Tonkatsu 450g",	172,	"FROZEN"),
(1439330,	"Frozen Shanghai Fish ball 1kg",	81,	"FROZEN"),
(1722714,	"Organic Vegan Rice Snack Gluten-Free Diet Quinoa",	399,	"GLUTEN-FREE FOOD"),
(1687845,	"KETO Seed Cookies 8g x 10pcs",	240,	"GLUTEN-FREE FOOD"),
(1528449,	"Bobs Red Mill Gluten Free Cornbread Crust 567g", 436	,"GLUTEN-FREE FOOD"),
(1283832,	"Pork Belly Menudo Cut 500g",	179,	"MEAT"),
(1638664,	"The Good Meat Belly Liempo Sliced 1kg",	409,	"MEAT"),
(1858587,	"Bounty Fresh Chicken Leg Quarters 860g",	220,	"MEAT"),
(1996940,	"DFP Galunggong Tinapa Smoked 250g", 	151,	"SEAFOOD"),
(1132337,	"Dried Squid Rings 100g",	180,	"SEAFOOD"),
(1604612,	"Frozen Bangus Belly by Dagupeno Catch 700g",	530,	"SEAFOOD"),
(1948067,	"Pacific Organic Beef Broth 946ml",	365,	"ORGANIC FOOD"), 
(1496438,	"Bahaghari Banana Chips 350g",	170,	"ORGANIC FOOD"), 
(1029393,	"Cebu Dried Mangoes 100g",	135,	"ORGANIC FOOD"),
(1659815,	"Office Warehouse Multi-Purpose Copy Paper 70gsm A4 500s",	230,	"PAPER PRODUCT"),
(1437734,	"Avia Colored Paper Assorted Vibrant Colors Short 80gsm 250 Sheets",	259,	"PAPER PRODUCT"),
(1646249,	"New Capri Specialty Paper 90gsm Short 10 Sheets per Pack", 32, "PAPER PRODUCT"),
(1772870,	"Nutriscience Pet Odor Away Organic Cleaner 500ml", 219, "CLEANING SUPPLY"),
(1184255,	"Zonrox Bleach Original 1 Gallon", 139,	"CLEANING SUPPLY"),
(1838857,	"Garbage Bag Medium 250pcs per Pack",	404,	"CLEANING SUPPLY"),
(1741046,	"pH Care Cool Wind Feminine Wash 250ml", 187, "PERSONAL CARE"),
(1514986,	"Sensodyne Gum Care Toothbrush (Twin Pack)", 147,	"PERSONAL CARE"),
(1236231,	"Personal Collection Alert Anticavity Fluoride Toothpaste 214g"	, 90, "PERSONAL CARE"),
(1698181,	"Lays Stax Potato Chips 105g",	70	,"SNACK"),
(1777002,	"Doritos Nacho Cheese Tortilla Chips Snack 190g", 120, "SNACK"),
(1962259,	"Stick-O Junior Wafer Stick Chocolate 380g", 81	,"SNACK"),
(1318373,	"Ideal Gourmet Rigatoni 100% Durum Wheat Semolina 500g", 97, "PASTA"),
(1306045,	"Del Monte Merienda Bundle - Filipino Spaghetti", 73, "PASTA"),
(1103672,	"DEL MONTE Spaghetti Pasta Italiana  400g", 90, "PASTA"
)]

    
#GENERAL DATABASE CREATOR
class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="CPET8L",
            port=3306
        )
        self.mycursor = self.mydb.cursor()

    def create_db(self):
        try:
            self.mycursor.execute("CREATE DATABASE GeneralDatabase")
            self.mydb = mysql.connector.connect(database="GeneralDatabase")
            return "Database is successfully created"
        except mysql.connector.Error as err:
            return err

    def create_table(self, id=None):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="CPET8L",
            port=3306,
            database="GeneralDatabase"
        )
        self.mycursor = self.mydb.cursor()

        if id == 0:
            try:
                self.mycursor.execute("CREATE TABLE accountmanagement(user_id VARCHAR(8) PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), status VARCHAR(255), last_updated TIMESTAMP, first_name VARCHAR(255), last_name VARCHAR(255), activity VARCHAR(8))")
                self.sql_query = "INSERT INTO accountmanagement (user_id, username, password, status, activity) VALUES (%s, %s, %s, %s, %s)"
                self.value = ("00000000" ,"admin", "admin", "OWNER", "OFFLINE")
                self.mycursor.execute(self.sql_query, (self.value))
                self.mydb.commit()
                return "Table successfully created"
            except mysql.connector.Error as err:
                print(err)

        elif id == 1:  # Creating masterlist table
            try:
                self.mycursor.execute("CREATE TABLE masterlist("
                                    "barcode_number INT PRIMARY KEY,"
                                    "product_name VARCHAR(255),"
                                    "price FLOAT,"
                                    "stock_left INT,"
                                    "stock INT,"
                                    "category VARCHAR(20),"
                                    "lastUpdated TIMESTAMP)")
                
               

                # Data insert
                for i in items:
                    barcode = i[0]
                    name = i[1]
                    price = i[2]
                    category = i[3]
                    stock = 100

                    self.sql_query = "INSERT INTO masterlist (barcode_number, product_name, price, stock_left, stock, category) VALUES (%s, %s, %s, %s, %s, %s)"
                    self.value = (barcode, name, price, stock, stock, category)
                    self.mycursor.execute(self.sql_query, self.value)
                    self.mydb.commit()
                return "Table successfully created"
            except mysql.connector.Error as err:
                print(err)

        elif id == 2:  # Creating Void_List table
            try:
                self.mycursor.execute("CREATE TABLE Void_List ("
                                    "Void_ID VARCHAR(10) PRIMARY KEY , "
                                    "user_id VARCHAR(8), "
                                    "item_list_id INT, "
                                    "Date_Voided VARCHAR(20), "
                                    "Time_Voided VARCHAR(20), "
                                    "FOREIGN KEY (user_id) REFERENCES accountmanagement(user_id), "
                                    "INDEX user_id_index (user_id)"
                                    ")")
                self.mydb.commit()
                return "Table successfully created"
            except mysql.connector.Error as err:
                print(err)

        elif id == 3:
            try:
                self.mycursor.execute("""
                    CREATE TABLE Discount_List (
                        Discount_ID INT PRIMARY KEY AUTO_INCREMENT,
                        Discount_Type VARCHAR(10),
                        Discount VARCHAR(20)
                    )
                """)
                # Insert initial discount values
                initial_discounts = [
                    (197582, "percentage", "No Discount"),
                    (232569, "percentage", "10%"),
                    (332953, "percentage", "25%"),
                    (403921, "percentage", "50%")
                ]
                insert_query = """
                    INSERT INTO Discount_List (Discount_ID, Discount_Type, Discount)
                    VALUES (%s, %s, %s)
                """
                self.mycursor.executemany(insert_query, initial_discounts)
                self.mydb.commit()
                return "Table successfully created"
            except mysql.connector.Error as err:
                print(err)


        elif id == 4: #creating HistoryOfPurchase Table
            try: 
                self.mycursor.execute("CREATE TABLE HistoryOfPurchase ("
                                      "Transaction_ID VARCHAR(20) , "
                                    "user_id VARCHAR(8),"
                                    "Discount_ID INT,"
                                    
                                    "Transaction_Sub_Total FLOAT, "
                                    "Transaction_Total FLOAT, "
                                    "Transaction_Total_Change FLOAT, "
                                    "Transaction_Date VARCHAR(20),"
                                    "Transaction_Time VARCHAR(20)"
                                    
                                    ""
                                    
                                    ")")
                self.mydb.commit()
                return "Table successfully created"
            except mysql.connector.Error as err:
                print(err)
        
        

        elif id == 5:  # Creating Item_List
            try:
                self.mycursor.execute("""
                    CREATE TABLE Item_List (
                        item_list_id VARCHAR(8) PRIMARY KEY,
                        user_id VARCHAR(8),
                        Barcode_Number INT,
                        product_quantity INT,
                        product_status VARCHAR(15),
                        FOREIGN KEY (user_id) REFERENCES accountmanagement(user_id),
                        FOREIGN KEY (Barcode_Number) REFERENCES masterlist(Barcode_Number)
                    )
                """)

                self.mydb.commit()
                return "Table successfully created"
            except mysql.connector.Error as err:
                print(err)

        elif id == 6: #creating HistoryOfPurchase Table
            try: 
                self.mycursor.execute("CREATE TABLE TemporaryTransaction ("
                                        "Transaction_ID VARCHAR(20) PRIMARY KEY , "
                                    "user_id VARCHAR(8),"
                                    "Discount_ID INT,"
                                    
                                    "Transaction_Sub_Total FLOAT, "
                                    "Transaction_Total FLOAT, "
                                    "Transaction_Total_Change FLOAT, "
                                    "Transaction_Date VARCHAR(20),"
                                    "Transaction_Time VARCHAR(20)"
                                    
                                    ""
                                    
                                    ")")
                self.mydb.commit()
                return "Table successfully created"
            except mysql.connector.Error as err:
                print(err)

        elif id == 7: #creating HistoryOfPurchase Table
            try: 
                self.mycursor.execute("CREATE TABLE Permissions ("
                                        "user_id VARCHAR(8) , "
                                    "Can_search_products BOOL,"
                                    "Can_Void_Product BOOL,"
                                    "Can_Access_Account_Manager BOOL, "
                                    "Can_Access_Manager_Tools BOOL, "
                                    "Can_Access_masterlist BOOL, "
                                    "Can_Access_Void_list BOOL,"
                                    "Can_Access_history_purchase BOOL,"
                                    "Can_Access_create_accounts BOOL,"
                                    "Can_Access_delete_accounts BOOL,"
                                    "is_blacklisted BOOL"

                                    ""
                                    
                                    ")")
                self.mydb.commit()

                self.sql_query = "INSERT INTO Permissions (user_id, Can_search_products, Can_Void_Product, Can_Access_Account_Manager, Can_Access_Manager_Tools, Can_Access_masterlist, Can_Access_Void_list, Can_Access_history_purchase, Can_Access_create_accounts, Can_Access_delete_accounts, is_blacklisted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                self.value = ("00000000" ,1, 1, 1, 1, 1, 1, 1, 1, 1, 0)
                self.mycursor.execute(self.sql_query, (self.value))
                self.mydb.commit()
                return "Table successfully created"
            except mysql.connector.Error as err:
                print(err)






   

        
           
      

    def reset_db(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="CPET8L",
            port=3306,
            database="GeneralDatabase"
        )
        self.mycursor = self.mydb.cursor()
        try:
            self.mycursor.execute("DROP DATABASE GeneralDatabase")
            return "DATABASE SUCCESSFULLY DROPPED"
        except mysql.connector.Error as err:
            print(err)

    


if __name__ == "__main__":
    
    DB = Database()
    DB.reset_db()
    DB.create_db()



    #CREATE TABLE
    DB.create_table(0)
    DB.create_table(1)
    DB.create_table(2)
    DB.create_table(3)
    DB.create_table(4)
    DB.create_table(5)
    DB.create_table(6)
    DB.create_table(7)
    
  
    
