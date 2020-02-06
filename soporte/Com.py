from .models import unidad2

def migracion():

    from django.db import connections

    def my_custom_sql(self):
        with connections["mysqlBD1"].cursor() as cursor:
            cursor.execute("SELECT * FROM unidad")
            row = cursor.fetchall()
            print (row)

        return row
        """
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
        """
    x123=my_custom_sql("hola")
    print ("aplicando")
    for x in x123:
        """
        print (x123[x])
        """
        try:
            unidad2.objects.create(id=x[0],nom_unidad=x[1])
        except:
            pass
        """
        print (x123[x][0])
        """
