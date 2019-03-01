# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Historicalquote(models.Model):
    hdate = models.DateTimeField(db_column='Hdate', primary_key=True)  # Field name made lowercase.
    open = models.DecimalField(db_column='Open', max_digits=8, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=8, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=8, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    close = models.DecimalField(db_column='Close', max_digits=8, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    volume = models.BigIntegerField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    symbol = models.ForeignKey('Stocks', models.DO_NOTHING, db_column='Symbol', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed =  False
        db_table = 'HistoricalQuote'


class Stocks(models.Model):
    symbol = models.CharField(db_column='Symbol', primary_key=True, max_length=10)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10)  # Field name made lowercase.
    industry = models.CharField(db_column='Industry', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stocks'


class Study(models.Model):
    classid = models.IntegerField(primary_key=True)
    classname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Study'


class Table(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pwd = models.CharField(db_column='PWD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=50, blank=True, null=True)  # Field name made lowercase.
    jointime = models.DateTimeField(db_column='JOINTIME', blank=True, null=True)  # Field name made lowercase.
    qustion = models.CharField(db_column='QUSTION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    answer = models.CharField(db_column='ANSWER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='PROFESSION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Table'


class TestmodelTest(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'TestModel_test'


class Accounts(models.Model):
    userid = models.CharField(primary_key=True, max_length=80)
    password = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    addr = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Orders(models.Model):
    orderid = models.ForeignKey('self', models.DO_NOTHING, db_column='orderid', primary_key=True)
    userid = models.CharField(max_length=80, blank=True, null=True)
    orderdate = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Ordersdetails(models.Model):
    orderid = models.BigIntegerField(primary_key=True)
    productid = models.CharField(max_length=10)
    quantity = models.IntegerField(blank=True, null=True)
    unicost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordersdetails'
        unique_together = (('orderid', 'productid'),)


class Products(models.Model):
    productid = models.CharField(primary_key=True, max_length=10)
    category = models.CharField(max_length=10, blank=True, null=True)
    cname = models.CharField(max_length=80, blank=True, null=True)
    ename = models.CharField(max_length=80, blank=True, null=True)
    image = models.CharField(max_length=20, blank=True, null=True)
    descn = models.CharField(max_length=255, blank=True, null=True)
    listprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unitcost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
