# ENetBrowser

> This repository is only used for 2020 Summer Research - Encyclopedia Net. 

### Description
- It is a website base on django to build Encyclopedia Net manually. 
- The folder _ENet_ contains code for building website.
- The folder _Mysql_ contains script for config mysql databases.

### Install

#### config mysql
```bash
git clone https://github.com/Little0o0/ENetBrowser.git
cd ENetBrowser/Mysql
#pwd
```

then we can config mysql
```bash
mysql -u root -p
# input your password
source #your_createTable.sql_path 
quit
```
and then you should add the password at the line 4 in insertData.py
```python
db = pymysql.connect("localhost","root","#password","ENetDB")
```
and type in terminal
```bash
python3 insertData.py
```

#### build website
```bash
cd ../ENet
vi ENet/views.py
```
you should add the password at the line 19,53 in views.py
```python
db = pymysql.connect("localhost","root","#password","ENetDB")
```

```bash
nohup python3 manage.py runserver 0.0.0.0:8000 >> out.log &
```
and you can view the website in __ip:8000/ENet__



### data
you can see the ENet data in mysql>ENetDB>ENetTable.




