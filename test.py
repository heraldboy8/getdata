import urllib
import re
import MySQLdb


try:
    #charset参数必须填写，否则会乱码,使用Localhost时无法连接
    conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='lsfx',connect_timeout=10,charset='utf8')
except Exception,e:
    print "无法连接的数据库"
    print e
cursor=conn.cursor()
    
#from urllib.request import urlopen
from bs4 import BeautifulSoup

for page in range(6174):
    url="http://furhr.com/?page=" + str(page)
    print url
    html = urllib.urlopen(url)
    bsObj= BeautifulSoup(html.read(),"html.parser")
    #print(bsObj.body.form.table)

    for sibling in bsObj.find("table",{"bgcolor":"#FFFFFF"}).tr.next_siblings:
        rows=re.findall('<td>(.+?)</td>',str(sibling))
        #print rows
        if len(rows)>=5:
            sql="insert into yh(xh,hh,wdmc,dh,dz) values('"+rows[0]+"'"
            sql=sql + ",'"+rows[1]+"'"
            sql=sql + ",'"+rows[2]+"'"
            sql=sql + ",'"+rows[3]+"'"
            sql=sql + ",'"+rows[4]+"'"
            sql=sql + ")"
            #print sql
            ra=cursor.execute(sql)
            #print "execute:" + str(ra)
    conn.commit()

cursor.close()
conn.commit()
conn.close
