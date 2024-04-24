from django.db import models

from products.models import Product


class Sale(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    salename = models.CharField(db_column='SaleName', max_length=50)
    total = models.TextField(db_column='Total')
    paycash = models.TextField(db_column='PayCash')
    paywith = models.TextField(db_column='PayWith')
    wholesale = models.TextField(db_column='Wholesale')
    completed = models.TextField(db_column='Completed')
    # userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserId')
    creationdate = models.DateTimeField(db_column='CreationDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')
    active = models.TextField(db_column='Active')

    class Meta:
        managed = False
        db_table = 'Sale'


class Saledetail(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    saleid = models.ForeignKey(Sale, models.DO_NOTHING, db_column='SaleId')
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductId')
    cost = models.TextField(db_column='Cost')
    price = models.TextField(db_column='Price')
    wholesale = models.TextField(db_column='WholeSale')
    quantity = models.TextField(db_column='Quantity')
    amount = models.TextField(db_column='Amount')
    unitid = models.ForeignKey('Unit', models.DO_NOTHING, db_column='UnitId')
    promotiondescription = models.CharField(db_column='PromotionDescription', max_length=500)
    markedasrefund = models.TextField(db_column='MarkedAsRefund')
    refund = models.TextField(db_column='Refund')
    ispromotion = models.TextField(db_column='IsPromotion')
    iswholesale = models.TextField(db_column='IsWholeSale')
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserId')
    creationdate = models.DateTimeField(db_column='CreationDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')
    active = models.TextField(db_column='Active')

    class Meta:
        managed = False
        db_table = 'SaleDetail'
