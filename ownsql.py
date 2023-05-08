"""
@File    :   ownsql.py    
@Contact :   xwz3568@163.com

@Modify Time          @Author    @Version    @Description
------------          --------   --------    -----------
2023/4/3 0003 17:22  FuGui      1.0          mysql存储模块
"""
import pymysql


def save_mysql(sql, val, **dbinfo):
    """
    mysql数据库存储函数封装
    :param sql:insert语句
    :param val:列表或元组-sql语句中属性列的值
    :param dbinfo:字典-需要连接的数据库信息
    """
    connect = pymysql.connect(**dbinfo)  # 创建数据库连接
    cursor = connect.cursor()  # 获取游标对象
    # ‘Local variable 'connect' might be referenced before assignment’
    # 事务回滚和关闭游标处警告信息,pycharm中不影响功能
    # 关键句是executemany句，如果sql出错则try和except句段将不被执行，数据库处于未连接状态，不存在事务对象和游标对象
    try:

        cursor.executemany(sql, val)  # execute执行sql语句 many执行多条 带占位的sql语句填充value
        connect.commit()  # 提交事务，应用操作
        print("数据存储完毕！")
    except Exception as err:
        connect.rollback()  # 事务回滚
        print(f'运行时出错！\n{err}')
    finally:
        cursor.close()  # 关闭游标
        connect.close()  # 关闭连接


if __name__ == '__main__':
    '''
    create database hmwk403;
    use hmwk403;
    create table bookinfo(
        id int auto_increment primary key,    /*数值类型 1开始自增 主键*/
        bookname varchar(100) character set utf8mb4 not null ,	  /*表级约束书名不为空*/
        author varchar(100) character set utf8mb4,
        describ varchar(4000) character set utf8mb4,
        price varchar(20) character set utf8mb4
    )default character set utf8mb4;  /*设置表的字符集*/
    '''
    dbinfo_ = {
        'host': '127.0.0.1',
        'user': 'pythonSQL',
        'password': '123456wz',
        'database': 'hmwk403',  # 需要先创建.否则找不到数据库
        'charset': 'utf8'
    }
    sql_ = "insert into bookinfo(bookname,author,describ,price)" \
           "values(%s,%s,%s,%s)"
    val_ = [["test2", "author_test2", "这是一行特别的测试数据","￥999.00"]]  # execute many可以执行多条语句，需要变动值部分，二维列表类型，每行数据都是列表
    save_mysql(sql_, val_, **dbinfo_)
    # 完全同名会有语法格式警告：’Shadows name 'XXX' from outer scope‘ 在外部的相同名称的变量没有任何作用，加以区分或更改名称即可，无伤大雅
