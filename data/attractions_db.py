# 利用 python 程式自動將 taipei-attractions.json 中的資料加進 mySQL 資料表中

import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='mysqlpassword',
    database='taipei_day_trip'
)

# 新增表格景點表格 (taipei_attractions)
cursor = db.cursor()
# cursor.execute('''
#   CREATE TABLE taipei_attractions(
#     id BIGINT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(255) UNIQUE,
#     category VARCHAR(255),
#     description TEXT,
#     address VARCHAR(255),
#     transport TEXT,
#     mrt VARCHAR(255),
#     latitude VARCHAR(20),
#     longitude VARCHAR(20));
# ''')

# 圖片url單獨放置一個表格 (attraction_imgs)，attraction_id 對應到 taipei_attractions 表格的 id
# cursor.execute('''
#   CREATE TABLE attraction_imgs(
#     id BIGINT PRIMARY KEY AUTO_INCREMENT,
#     attraction_id BIGINT NOT NULL,
#     url TEXT,
#     FOREIGN KEY(attraction_id) REFERENCES taipei_attractions(id) ON DELETE CASCADE);
# ''')


# import json
# with open('taipei-attractions.json', mode='r', encoding='utf-8') as file:
#   data = json.load(file)

# attractions = data['result']['results']
# for attraction in attractions:
#   name = attraction['stitle']
#   category = attraction['CAT2']
#   description = attraction['xbody']
#   address = attraction['address'].replace(' ',  '')
#   transport = attraction['info']
#   mrt = attraction['MRT']
#   latitude = attraction['latitude']
#   longitude = attraction['longitude']
#   cursor.execute('''
#     INSERT INTO taipei_attractions(name, category, description, address, transport, mrt, latitude, longitude)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s);''', (name, category, description, address, transport, mrt, latitude, longitude)
#   )

# for index, value in enumerate(attractions):
#   images = value['file'].replace('https', ' https').split()   # 取得網址列表
#   for url in images:
#     url = url.lower()
#     if 'jpg' in url or 'png' in url:
#       cursor.execute('''
#         INSERT INTO attraction_imgs(attraction_id, url)
#         VALUES (%s, %s);''', (index+1, url)
#       )


# 新增會員資料表格 (member)
# cursor.execute('''
#   CREATE TABLE member(
#     id BIGINT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(255) NOT NULL,
#     email VARCHAR(255) NOT NULL UNIQUE,
#     password VARCHAR(255) NOT NULL
# )''')

# 新增紀錄購物車商品表格 (booking)
# order_status = 1 表尚未結帳，0 表已結帳
# cursor.execute('''
#   CREATE TABLE booking(
#     id BIGINT PRIMARY KEY AUTO_INCREMENT,
#     member_id BIGINT NOT NULL,
#     attraction_id BIGINT NOT NULL,
#     date DATE NOT NULL,
#     time VARCHAR(20) NOT NULL,
#     price INT NOT NULL,
#     order_status SMALLINT NOT NULL DEFAULT 1,
#     FOREIGN KEY (member_id) REFERENCES member(id),
#     FOREIGN KEY (attraction_id) REFERENCES taipei_attractions(id),
#     INDEX (member_id)
#   );
# ''')

# 新增紀錄使用者付款訂單的表格 (order)
cursor.execute('''
  CREATE TABLE `order`(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    order_id VARCHAR(255) NOT NULL,
    member_id BIGINT NOT NULL,
    contact_name VARCHAR(255) NOT NULL,
    contact_email VARCHAR(255) NOT NULL,
    contact_phone VARCHAR(255) NOT NULL,
    booking_id BIGINT NOT NULL,
    attraction_id BIGINT NOT NULL,
    date DATE NOT NULL,
    time VARCHAR(20) NOT NULL,
    price INT NOT NULL,
    total_price INT NOT NULL,
    status SMALLINT NOT NULL DEFAULT 1,
    order_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES member(id),
    INDEX (order_id),
    INDEX (member_id)
  );
''')

cursor.close()
db.commit()
db.close()
