from .models import bie_gob_bienes, bienes_gob_categoria, unidad2
from django.shortcuts import render, redirect, get_object_or_404, resolve_url

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

def migracion_bienes_gobs():

    from django.db import connections

    def my_custom_sql(self):
        with connections["mysqlBD1"].cursor() as cursor:
            cursor.execute("SELECT * FROM bie_categoria")
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
            bienes_gob_categoria.objects.create(id=x[0],codigo=x[1],nombre=x[2])
        except:
            pass
        """
        print (x123[x][0])
        """
def migracion_bienes_g_bienes():

    from django.db import connections

    def my_custom_sql(self):
        with connections["mysqlBD1"].cursor() as cursor:
            cursor.execute("SELECT * FROM bie_bienes")
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
        #trabj1
        """
        print (x123[x])
        """
        try:
            bie_gob_bienes.objects.create(id=x[0],codigo_e=x[1],cantidad=x[2],nombre=x[3],idunidad=get_object_or_404(unidad2, pk=x[4]),idcategoria=get_object_or_404(bienes_gob_categoria, pk=x[5]))
        except:
            pass 
        
        """
        print (x123[x][0])
        """

def test_velocidad():

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
        print (x)

        """
        try:
            unidad2.objects.create(id=x[0],nom_unidad=x[1])
        except:
            pass
        """
        """
        print (x123[x][0])
        """
