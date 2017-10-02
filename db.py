import pymysql.cursors

class DatabaseManager(object):
  def __init__(self):
    super(DatabaseManager, self).__init__()
    self.connection = pymysql.connect(host='localhost', port=8889, user='ayudante', password='holamundo', db='ayudantia_5', cursorclass=pymysql.cursors.DictCursor)

  def get_connection(self):
    return self.connection

  def close(self):
    self.connection.close()