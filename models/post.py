from db import DatabaseManager

class Post(object):
  def __init__(self):
    super(Post, self).__init__()

  def create(self, title, description):
    db = DatabaseManager()
    connection= db.get_connection()

    with connection.cursor() as cursor:
      sql = "INSERT INTO posts (title, description) VALUES ('"+title+"','"+description+"');"
      result = cursor.execute(sql)
      
      connection.commit()
      
      if result == 1 or result == '1':
        return True
      else:
        return False
  
  def update(self, id, title, description):
    return
    
  def destroy(self, id):
    db = DatabaseManager()
    connection= db.get_connection()

    with connection.cursor() as cursor:
      sql = "DELETE FROM posts WHERE id = "+id+" LIMIT 1;"
      result = cursor.execute(sql)
      
      connection.commit()
      
      if result == 1 or result == '1':
        return True
      else:
        return False
  
  def all(self):
    db = DatabaseManager()
    connection= db.get_connection()

    with connection.cursor() as cursor:
      sql = "SELECT id, title, description FROM posts"
      cursor.execute(sql)
      posts = cursor.fetchall()
      
      db.close()

      return posts
    
  def find(self, id):
    return