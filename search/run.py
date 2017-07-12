# from scrapy import cmdline
#
# cmdline.execute("scrapy crawl search".split())
import MySQLdb

conn=MySQLdb.connect(user='scrub_ro',passwd='3k3Y73e!sZ',host='ci-poc-db.cdrn06pzpw23.us-east-1.rds.amazonaws.com',db='ci_scrub',use_unicode=True, charset='utf8')
cursor=conn.cursor()

sql="""
select ci_ssc_parent_all_scrub.domain, ci_ssc_parent_all_scrub.empl_count
from ci_ssc_parent_all_scrub
where ci_ssc_parent_all_scrub.domain=%s;
"""
with  open("C:\Users\jessica_zhu1\Desktop\lexa","r") as company:
    lines=company.readlines()

    for line in lines:
        a=line.rstrip()
        f=open('result','a+')
        cursor.execute(sql,(a,))
        #results=cursor.fetchall()
        for row in cursor:

            row=list(row)
            f.write(str(row[0])+' '+str(int(row[1]))+'\n')


        f.close()

conn.commit()
