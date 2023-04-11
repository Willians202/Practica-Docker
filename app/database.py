from pymongo import MongoClient
import configuration as C

myclient = MongoClient(C.CON_STRING_CLOUD)
mydb = myclient[C.CON_CLIENT]

if __name__ == "__main__":
    dbname= mydb