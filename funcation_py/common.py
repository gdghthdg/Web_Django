import MySQLdb
from traceback import print_exc
from django.views.decorators import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response

#mysql的使用函数
def mysql_execute(sql_order):
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "123456", "test_database", charset='utf8' )

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # # 使用execute方法执行SQL语句
    # sql_order="SELECT VERSION()"
    # sql_order="select * from mysql_thing_lh"
    print("sql_oder",sql_order)
    cursor.execute(sql_order)

    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchall()

    print (data)

    # 关闭数据库连接
    db.close()



    return data


def sreen(valse):

    return valse

if __name__=="__main__":
    mysql_execute("select * from mysql_thing_lh")