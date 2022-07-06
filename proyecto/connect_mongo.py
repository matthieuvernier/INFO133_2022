#pip install pymongo
from pymongo import MongoClient

client = MongoClient("localhost", port=27017)
db=client.info133_2022

news = {'url':'https://www.latercera.com/nacional/noticia/diputados-del-partido-de-la-gente-presentan-reforma-para-consagrar-en-la-constitucion-el-derecho-a-tener-armas/SL5KWXAG6FB4HBISUJXRWHT4HY/',
 'to_download':True}
result=db.urls.insert_one(news)
