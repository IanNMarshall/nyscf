from django.db import models

# Allow photos
photo = models.ImageField(upload_to="gallery")

class Dc1(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.
    filer_id = models.ForeignKey('Df1', models.DO_NOTHING, db_column='FILER_ID', blank=True, null=True)  # Field name made lowercase.
    freport_id = models.CharField(db_column='FREPORT_ID', max_length=1, blank=True, null=True)  # Field name made lowercase.
    transaction_code = models.CharField(db_column='TRANSACTION_CODE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_year = models.IntegerField(db_column='E_YEAR', blank=True, null=True)  # Field name made lowercase.
    t3_trid = models.CharField(db_column='T3_TRID', max_length=8, blank=True, null=True)  # Field name made lowercase.
    date1_10 = models.CharField(db_column='DATE1_10', max_length=12, blank=True, null=True)  # Field name made lowercase.
    date2_12 = models.CharField(db_column='DATE2_12', max_length=12, blank=True, null=True)  # Field name made lowercase.
    contrib_code_20 = models.CharField(db_column='CONTRIB_CODE_20', max_length=5, blank=True, null=True)  # Field name made lowercase.
    contrib_type_code_25 = models.CharField(db_column='CONTRIB_TYPE_CODE_25', max_length=1, blank=True, null=True)  # Field name made lowercase.
    corp_30 = models.CharField(db_column='CORP_30', max_length=128, blank=True, null=True)  # Field name made lowercase.
    first_name_40 = models.CharField(db_column='FIRST_NAME_40', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mid_init_42 = models.CharField(db_column='MID_INIT_42', max_length=16, blank=True, null=True)  # Field name made lowercase.
    last_name_44 = models.CharField(db_column='LAST_NAME_44', max_length=32, blank=True, null=True)  # Field name made lowercase.
    addr_1_50 = models.CharField(db_column='ADDR_1_50', max_length=128, blank=True, null=True)  # Field name made lowercase.
    city_52 = models.CharField(db_column='CITY_52', max_length=32, blank=True, null=True)  # Field name made lowercase.
    state_54 = models.CharField(db_column='STATE_54', max_length=2, blank=True, null=True)  # Field name made lowercase.
    zip_56 = models.CharField(db_column='ZIP_56', max_length=10, blank=True, null=True)  # Field name made lowercase.
    check_no_60 = models.CharField(db_column='CHECK_NO_60', max_length=10, blank=True, null=True)  # Field name made lowercase.
    check_date_62 = models.CharField(db_column='CHECK_DATE_62', max_length=12, blank=True, null=True)  # Field name made lowercase.
    amount_70 = models.DecimalField(db_column='AMOUNT_70', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amount2_72 = models.DecimalField(db_column='AMOUNT2_72', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    description_80 = models.CharField(db_column='DESCRIPTION_80', max_length=256, blank=True, null=True)  # Field name made lowercase.
    other_recpt_code_90 = models.CharField(db_column='OTHER_RECPT_CODE_90', max_length=32, blank=True, null=True)  # Field name made lowercase.
    purpose_code1_100 = models.CharField(db_column='PURPOSE_CODE1_100', max_length=32, blank=True, null=True)  # Field name made lowercase.
    purpose_code2_102 = models.CharField(db_column='PURPOSE_CODE2_102', max_length=32, blank=True, null=True)  # Field name made lowercase.
    explanation_110 = models.CharField(db_column='EXPLANATION_110', max_length=32, blank=True, null=True)  # Field name made lowercase.
    xfer_type_120 = models.CharField(db_column='XFER_TYPE_120', max_length=32, blank=True, null=True)  # Field name made lowercase.
    chkbox_130 = models.CharField(db_column='CHKBOX_130', max_length=32, blank=True, null=True)  # Field name made lowercase.
    crerec_uid = models.CharField(db_column='CREREC_UID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    crerec_date = models.CharField(db_column='CREREC_DATE', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DC1'


class Df1(models.Model):
    filer_id = models.CharField(db_column='FILER_ID', primary_key=True, max_length=8)  # Field name made lowercase.
    filer_name = models.CharField(db_column='FILER_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    filer_type = models.CharField(db_column='FILER_TYPE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=8, blank=True, null=True)  # Field name made lowercase.
    committee_type = models.CharField(db_column='COMMITTEE_TYPE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    office = models.IntegerField(db_column='OFFICE', blank=True, null=True)  # Field name made lowercase.
    district = models.IntegerField(db_column='DISTRICT', blank=True, null=True)  # Field name made lowercase.
    treas_first_name = models.CharField(db_column='TREAS_FIRST_NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    treas_last_name = models.CharField(db_column='TREAS_LAST_NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=64, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=32, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='ZIP', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DF1'


class Zip2Fips(models.Model):
    zip = models.CharField(db_column='ZIP', primary_key=True, max_length=5)  # Field name made lowercase.
    fips = models.CharField(db_column='FIPS', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZIP2FIPS'


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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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
    action_flag = models.PositiveSmallIntegerField()
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
