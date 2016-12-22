#!/usr/bin/env python
# coding: utf-8
import web
from config import settings
import MySQLdb
import datetime
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

render = settings.render

conn = MySQLdb.connect(user='root', passwd='123456', host='127.0.0.1', port=3306)


class Query:
    def GET(self):
        return render.index([], [], '')

    def POST(self):
        form = web.input()
        isql = form['sql']

        if not isql:
            return render.index([], [], '')

        try:
            sql = isql.encode("utf-8");

            conn.select_db('mysql')
            cursor = conn.cursor()
            cursor.execute("SET NAMES 'utf8'")
            cursor.execute(sql)

            # 全部结果放在一个大的list
            columnNames = []

            # 查询SQL的返回值属性list
            for field in cursor.description:
                columnNames.append(field[0])

            allResults = [];
            # 查询数据结果集
            res = cursor.fetchall()
            for row in res:
                tempRes = []
                for r in row:
                    tmp = r
                    if r is not None and type(r) is datetime.datetime:
                        tmp = datetime.datetime.strftime(r, '%Y-%m-%d %H:%M:%S')
                    tempRes.append(tmp)

                allResults.append(tempRes)

            conn.commit()
            cursor.close()

            return render.index(columnNames, allResults, sql)
        except:
            return render.index([], [], '')


class Index:
    def GET(self):
        return render.index([], [], '')
