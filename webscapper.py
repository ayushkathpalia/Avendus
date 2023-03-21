import requests
from bs4 import BeautifulSoup
from decouple import config

class Avendus:
    def __init__(self,url):
        self.url = url
    
    #iniializing db
    def _db_instance(self):
        try:
            import mysql.connector
            mydb = mysql.connector.connect(
            host=config('IP'),
            user=config('DB_USERNAME'),
            password=config('DB_PASSWORD')
            )
            mycursor = mydb.cursor()
            return mycursor,mydb
        except Exception as e:
            print(e)
    
    #scapping data from the website
    def scrapdata(self):
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                                "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                                "Version/15.4 Safari/605.1.15"}
        page = requests.get(self.url,headers=headers)
        soup = BeautifulSoup(page.text, 'lxml')
        table1 = soup.find('table',id='ContentPlaceHolder1_gvbulk_deals')
        headers = []
        for i in table1.find_all('th'):
            title = i.text
            headers.append(title)
        data = []
        for j in table1.find_all('tr')[1:]:
            row_data = j.find_all('td')
            row = [i.text for i in row_data]
            data.append(row)
        self.insert_data(data=data)
    
    #inserting data to the db
    def insert_data(self,data):
        cursor,db = self._db_instance()
        from datetime import datetime
        now = datetime.now()
        query = f"INSERT INTO bse.bulkdeals(deal_date,security_code,security_name,client_name,deal_type,quantity,price,created_on,updated_on) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for row in data:
            print(row)
            try:
                row.append(now)
                row.append(now)
                cursor.execute(query,row)
            except Exception as e:
                print(e)
                continue
        db.commit()

if __name__ == '__main__':
    url = 'https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx'
    obj = Avendus(url)
    obj.scrapdata()

