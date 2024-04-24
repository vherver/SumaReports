from django.db import models


class Product(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    producttypeid = models.ForeignKey('Producttype', models.DO_NOTHING, db_column='ProductTypeId')
    productname = models.CharField(db_column='ProductName', max_length=500)
    code = models.IntegerField(db_column='Code')
    cost = models.TextField(db_column='Cost')
    price = models.TextField(db_column='Price')
    wholesale = models.TextField(db_column='Wholesale')
    unitid = models.ForeignKey('Unit', models.DO_NOTHING, db_column='UnitId')
    profitpercentage = models.TextField(db_column='ProfitPercentage')
    applypercentage = models.TextField(db_column='ApplyPercentage')
    existence = models.TextField(db_column='Existence')
    userid = models.IntegerField(db_column='UserId')
    creationdate = models.DateTimeField(db_column='CreationDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')
    active = models.TextField(db_column='Active')

    class Meta:
        managed = False
        db_table = 'Product'


class Producttype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    producttypename = models.CharField(db_column='ProductTypeName', max_length=50)
    userid = models.IntegerField(db_column='UserId')
    creationdate = models.DateTimeField(db_column='CreationDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')
    active = models.TextField(db_column='Active')

    class Meta:
        managed = False
        db_table = 'ProductType'