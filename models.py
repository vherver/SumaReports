from django.db import models


class Moneyentry(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    total = models.TextField(db_column='Total')  # Field name made lowercase. This field type is a guess.
    description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    active = models.TextField(db_column='Active')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'MoneyEntry'


class Moneyout(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    total = models.TextField(db_column='Total')  # Field name made lowercase. This field type is a guess.
    description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    active = models.TextField(db_column='Active')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'MoneyOut'



class Promotion(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    promotiontypeid = models.ForeignKey('Promotiontype', models.DO_NOTHING, db_column='PromotionTypeId')  # Field name made lowercase.
    promotionname = models.CharField(db_column='PromotionName', max_length=500)  # Field name made lowercase.
    validfrom = models.DateTimeField(db_column='ValidFrom')  # Field name made lowercase.
    validto = models.DateTimeField(db_column='ValidTo')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    active = models.TextField(db_column='Active')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Promotion'


class Promotionrel(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    promotionid = models.ForeignKey(Promotion, models.DO_NOTHING, db_column='PromotionId')  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductId')  # Field name made lowercase.
    quantity = models.TextField(db_column='Quantity')  # Field name made lowercase. This field type is a guess.
    promotionprice = models.TextField(db_column='PromotionPrice')  # Field name made lowercase. This field type is a guess.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PromotionRel'


class Promotiontype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    promotiontypename = models.CharField(db_column='PromotionTypeName', max_length=50)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PromotionType'


class Reeltype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    reeltypename = models.CharField(db_column='ReelTypeName', max_length=10)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    active = models.TextField(db_column='Active')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ReelType'


class Role(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=50)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    active = models.TextField(db_column='Active')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Role'







class Setting(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    printername = models.CharField(db_column='PrinterName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reeltypeid = models.ForeignKey(Reeltype, models.DO_NOTHING, db_column='ReelTypeId')  # Field name made lowercase.
    shifttypeid = models.ForeignKey('Shifttype', models.DO_NOTHING, db_column='ShiftTypeId')  # Field name made lowercase.
    useprinter = models.TextField(db_column='UsePrinter')  # Field name made lowercase. This field type is a guess.
    usescale = models.TextField(db_column='UseScale')  # Field name made lowercase. This field type is a guess.
    scaleport = models.CharField(db_column='ScalePort', max_length=10, blank=True, null=True)  # Field name made lowercase.
    scaleverified = models.TextField(db_column='ScaleVerified')  # Field name made lowercase. This field type is a guess.
    businessname = models.CharField(db_column='BusinessName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=50, blank=True, null=True)  # Field name made lowercase.
    suburb = models.CharField(db_column='Suburb', max_length=50, blank=True, null=True)  # Field name made lowercase.
    municipality = models.CharField(db_column='Municipality', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=20, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rfc = models.CharField(db_column='RFC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sloganmessage = models.CharField(db_column='SloganMessage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userkey = models.CharField(db_column='UserKey', max_length=50)  # Field name made lowercase.
    productregistration = models.CharField(db_column='ProductRegistration', max_length=500, blank=True, null=True)  # Field name made lowercase.
    refillkey = models.CharField(db_column='RefillKEY', max_length=150)  # Field name made lowercase.
    refillnip = models.CharField(db_column='RefillNIP', max_length=150)  # Field name made lowercase.
    refillactived = models.TextField(db_column='RefillActived')  # Field name made lowercase. This field type is a guess.
    refillpercentagebusinessprofit = models.TextField(db_column='RefillPercentageBusinessProfit')  # Field name made lowercase. This field type is a guess.
    refillextrabusinessprofit = models.TextField(db_column='RefillExtraBusinessProfit')  # Field name made lowercase. This field type is a guess.
    servicecommissionbusinessprofit = models.TextField(db_column='ServiceCommissionBusinessProfit')  # Field name made lowercase. This field type is a guess.
    showbalanceinservices = models.TextField(db_column='ShowBalanceInServices')  # Field name made lowercase. This field type is a guess.
    printticketautomatically = models.TextField(db_column='PrintTicketAutomatically')  # Field name made lowercase. This field type is a guess.
    showtax = models.TextField(db_column='ShowTax')  # Field name made lowercase. This field type is a guess.
    disablestockcontrol = models.TextField(db_column='DisableStockControl')  # Field name made lowercase. This field type is a guess.
    allowemployeeaddinvetory = models.TextField(db_column='AllowEmployeeAddInvetory')  # Field name made lowercase. This field type is a guess.
    ticketfileextension = models.CharField(db_column='TicketFileExtension', max_length=10)  # Field name made lowercase.
    applicationdbfolder = models.CharField(db_column='ApplicationDBFolder', max_length=2000)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    active = models.TextField(db_column='Active')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Setting'


class Shift(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    shifttypeid = models.ForeignKey('Shifttype', models.DO_NOTHING, db_column='ShiftTypeId')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime')  # Field name made lowercase.
    shiftnumber = models.IntegerField(db_column='ShiftNumber')  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shift'


class Shifttype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    shifttypename = models.CharField(db_column='ShiftTypeName', max_length=50)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShiftType'


class TaeBolsas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAE_Bolsas'


class TaeCampos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    carriersid = models.IntegerField(db_column='CarriersId')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=150)  # Field name made lowercase.
    campo = models.CharField(db_column='Campo', max_length=50)  # Field name made lowercase.
    min = models.IntegerField(db_column='Min')  # Field name made lowercase.
    max = models.IntegerField(db_column='Max')  # Field name made lowercase.
    formato = models.IntegerField(db_column='Formato')  # Field name made lowercase.
    confirmar = models.IntegerField(db_column='Confirmar')  # Field name made lowercase.
    obligatorio = models.IntegerField(db_column='Obligatorio')  # Field name made lowercase.
    inicero = models.IntegerField(db_column='iniCero')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAE_Campos'


class TaeCarriers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=150)  # Field name made lowercase.
    logotipo = models.CharField(db_column='Logotipo', max_length=500)  # Field name made lowercase.
    bolsaid = models.IntegerField(db_column='BolsaID')  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=50)  # Field name made lowercase.
    categoriaid = models.IntegerField(db_column='CategoriaID')  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo')  # Field name made lowercase.
    promos = models.CharField(db_column='Promos', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    getsaldo = models.IntegerField(db_column='getSaldo')  # Field name made lowercase.
    scanqrname = models.CharField(db_column='ScanQrName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    com_id = models.IntegerField(db_column='Com_ID')  # Field name made lowercase.
    com_cargotrans = models.TextField(db_column='Com_CargoTrans')  # Field name made lowercase. This field type is a guess.
    com_tipocargo = models.IntegerField(db_column='Com_TipoCargo')  # Field name made lowercase.
    com_abonotrans = models.TextField(db_column='Com_AbonoTrans')  # Field name made lowercase. This field type is a guess.
    com_tipoabono = models.IntegerField(db_column='Com_TipoAbono')  # Field name made lowercase.
    com_comisioncliente = models.TextField(db_column='Com_ComisionCliente')  # Field name made lowercase. This field type is a guess.
    com_def_cargotrans = models.TextField(db_column='Com_def_CargoTrans')  # Field name made lowercase. This field type is a guess.
    com_def_abonotrans = models.TextField(db_column='Com_def_AbonoTrans')  # Field name made lowercase. This field type is a guess.
    com_status = models.IntegerField(db_column='Com_Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAE_Carriers'


class TaeCarrierstipo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAE_CarriersTipo'


class TaeCategorias(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    icono = models.CharField(db_column='Icono', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAE_Categorias'


class TaeComisiontipo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAE_ComisionTipo'


class TaeFormatocampos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAE_FormatoCampos'


class TaeProductos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bolsa = models.CharField(db_column='Bolsa', max_length=50)  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=50)  # Field name made lowercase.
    categoriaid = models.IntegerField(db_column='CategoriaID')  # Field name made lowercase.
    bolsaid = models.IntegerField(db_column='BolsaID')  # Field name made lowercase.
    carrier = models.CharField(db_column='Carrier', max_length=150)  # Field name made lowercase.
    carrierid = models.IntegerField(db_column='CarrierID')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=50)  # Field name made lowercase.
    monto = models.TextField(db_column='Monto')  # Field name made lowercase. This field type is a guess.
    unidades = models.TextField(db_column='Unidades')  # Field name made lowercase. This field type is a guess.
    vigencia = models.CharField(db_column='Vigencia', max_length=2000)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=2000)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAE_Productos'


class TaeSales(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=150)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=150)  # Field name made lowercase.
    numberorreference = models.CharField(db_column='NumberOrReference', max_length=150)  # Field name made lowercase.
    amount = models.TextField(db_column='Amount')  # Field name made lowercase. This field type is a guess.
    fielddescription = models.CharField(db_column='FieldDescription', max_length=150)  # Field name made lowercase.
    endingbalance = models.CharField(db_column='EndingBalance', max_length=150, blank=True, null=True)  # Field name made lowercase.
    region = models.IntegerField(db_column='Region')  # Field name made lowercase.
    ip = models.CharField(db_column='Ip', max_length=20)  # Field name made lowercase.
    way = models.CharField(db_column='Way', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bag = models.CharField(db_column='Bag', max_length=50, blank=True, null=True)  # Field name made lowercase.
    folio = models.IntegerField(db_column='Folio')  # Field name made lowercase.
    transid = models.IntegerField(db_column='TransID')  # Field name made lowercase.
    refillpercentagebusinessprofit = models.TextField(db_column='RefillPercentageBusinessProfit')  # Field name made lowercase. This field type is a guess.
    refillextrabusinessprofit = models.TextField(db_column='RefillExtraBusinessProfit')  # Field name made lowercase. This field type is a guess.
    servicecommissionbusinessprofit = models.TextField(db_column='ServiceCommissionBusinessProfit')  # Field name made lowercase. This field type is a guess.
    businessprofitbound = models.TextField(db_column='BusinessProfitBound')  # Field name made lowercase. This field type is a guess.
    commissionsupplier = models.TextField(db_column='CommissionSupplier')  # Field name made lowercase. This field type is a guess.
    message = models.CharField(db_column='Message', max_length=2000)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAE_Sales'




class User(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=20)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    roleid = models.ForeignKey(Role, models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.
    wholesale = models.TextField(db_column='Wholesale')  # Field name made lowercase. This field type is a guess.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    active = models.TextField(db_column='Active')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'User'
