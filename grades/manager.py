from django.db import models,connection

class SQLManager(models.Manager):
    def sql(self,element,value,sql):
        cursor=connection.cursor()
        cursor.execute('"""'+sql+'"""',[element,value])
        return [row[0] for row in cursor.fetchone()]

