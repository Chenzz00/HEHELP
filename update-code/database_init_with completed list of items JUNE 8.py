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
(1990067,	"Mozzarella Cheese Arla Block 2.3kg", 1,420, "DAIRY"),
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
class database:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "CPET8L",
            port = 3306
        )
        self.mycursor = self.mydb.cursor()

    def create_db(self):
        try:
            self.mycursor.execute("CREATE DATABASE GeneralDatabase")
            self.mydb = mysql.connector.connect(database = "generaldatabase")
            return "Database is succesfully created"

        except mysql.connector.Error as err:
            return err

    def create_table(self, id = None):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "CPET8L",
            port = 3306,
            database = "generaldatabase"
        )
        self.mycursor = self.mydb.cursor()
        #accounts
        if id == 0:
            try:
                self.mycursor.execute("CREATE TABLE accountmanagement(username VARCHAR(255), password VARCHAR(255), status VARCHAR(255), last_updated TIMESTAMP, first_name VARCHAR(255), last_name VARCHAR(255))")
                self.sql_query = "INSERT INTO accountmanagement (username, password, status) VALUES (%s, %s, %s)"
                self.value = ("admin", "admin", "OWNER")
                self.mycursor.execute(self.sql_query, (self.value))
                self.mydb.commit()
                return "Table successfully created"
            except mysql.connector.Error as err:
                print(err)
        
        #masterlist
        elif id == 1:
            global items
            try:
                #table creation
                self.mycursor.execute("CREATE TABLE masterlist(barcode_number INT, product_name VARCHAR(255), price FLOAT, stock_left INT, stock INT, category VARCHAR(255), lastUpdated TIMESTAMP)")
                #data insert
                for i in items:
                    barcode = i[0]
                    name = i[1]
                    price = i[2]
                    category = i[3]
                    stock = 100

                    self.sql_query = "INSERT INTO masterlist (barcode_number, product_name, price, stock_left, stock, category) VALUES (%s, %s, %s, %s, %s, %s)"
                    self.value = (barcode, name, price, stock, stock, category)
                    self.mycursor.execute(self.sql_query, (self.value))
                    self.mydb.commit()
                return "Table successfully created"
            except mysql.connector.Error as err:
                print(err)

        else:
            return "TABLE ALREADY CREATED"

    def reset_db(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "CPET8L",
            port = 3306,
            database = "generaldatabase"
        )
        self.mycursor = self.mydb.cursor()
        try:
            self.mycursor.execute("DROP DATABASE generaldatabase")
            return "DATABASE SUCCESSFULLY DROPPED"
        
        except mysql.connector.Error as err:
            print(err)

    def reset_table(self, id):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "CPET8L",
            port = 3306,
            database = "generaldatabase"
        )
        self.mycursor = self.mydb.cursor()
        if id == 0:
            try:
                self.mycursor.execute("DROP TABLE accountmanagement")
                return "Table Successfully Dropped"

            except mysql.connector.Error as err:
                print(err)
            
        elif id == 1:
            try:
                self.mycursor.execute("DROP TABLE masterlist")
                return "Table Successfully Dropped"

            except mysql.connector.Error as err:
                print(err)

    def setup_items(self):
        pass


'''WARNING: 
RUNNING THIS SCRIPT WILL DEFINITELY OBLITERATE YOUR SAVE IN DATABASE. 
DO NOT RUN THIS SCRIPT AS MAIN IF YOU DONT WANT THAT'''
if __name__ == "__main__":
    DB = database()
    DB.reset_table(1)
    DB.create_table(1)
