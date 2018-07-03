from django.db import models

# Create your models here.
# Allow photos
photo = models.ImageField(upload_to="gallery")

# class DF1(models.Model):
# 	filer_id = models.CharField(max_length=16)
# 	FILER_NAME = models.TextField()
	
# 	def __str__(self):              # __unicode__ on Python 2
#         return self.FILER_NAME

class DataContributions(models.Model):
    filer_id = models.TextField(db_column='FILER_ID', blank=True, null=True)  # Field name made lowercase.
    freport_id = models.TextField(db_column='FREPORT_ID', blank=True, null=True)  # Field name made lowercase.
    transaction_code = models.TextField(db_column='TRANSACTION_CODE', blank=True, null=True)  # Field name made lowercase.
    e_year = models.IntegerField(db_column='E_YEAR', blank=True, null=True)  # Field name made lowercase.
    t3_trid = models.IntegerField(db_column='T3_TRID', blank=True, null=True)  # Field name made lowercase.
    date1_10 = models.TextField(db_column='DATE1_10', blank=True, null=True)  # Field name made lowercase.
    date2_12 = models.TextField(db_column='DATE2_12', blank=True, null=True)  # Field name made lowercase.
    contrib_code_20 = models.TextField(db_column='CONTRIB_CODE_20', blank=True, null=True)  # Field name made lowercase.
    contrib_type_code_25 = models.TextField(db_column='CONTRIB_TYPE_CODE_25', blank=True, null=True)  # Field name made lowercase.
    corp_30 = models.TextField(db_column='CORP_30', blank=True, null=True)  # Field name made lowercase.
    first_name_40 = models.TextField(db_column='FIRST_NAME_40', blank=True, null=True)  # Field name made lowercase.
    mid_init_42 = models.TextField(db_column='MID_INIT_42', blank=True, null=True)  # Field name made lowercase.
    last_name_44 = models.TextField(db_column='LAST_NAME_44', blank=True, null=True)  # Field name made lowercase.
    addr_1_50 = models.TextField(db_column='ADDR_1_50', blank=True, null=True)  # Field name made lowercase.
    city_52 = models.TextField(db_column='CITY_52', blank=True, null=True)  # Field name made lowercase.
    state_54 = models.TextField(db_column='STATE_54', blank=True, null=True)  # Field name made lowercase.
    zip_56 = models.IntegerField(db_column='ZIP_56', blank=True, null=True)  # Field name made lowercase.
    check_no_60 = models.TextField(db_column='CHECK_NO_60', blank=True, null=True)  # Field name made lowercase.
    check_date_62 = models.TextField(db_column='CHECK_DATE_62', blank=True, null=True)  # Field name made lowercase.
    amount_70 = models.IntegerField(db_column='AMOUNT_70', blank=True, null=True)  # Field name made lowercase.
    amount2_72 = models.TextField(db_column='AMOUNT2_72', blank=True, null=True)  # Field name made lowercase.
    description_80 = models.TextField(db_column='DESCRIPTION_80', blank=True, null=True)  # Field name made lowercase.
    other_recpt_code_90 = models.TextField(db_column='OTHER_RECPT_CODE_90', blank=True, null=True)  # Field name made lowercase.
    purpose_code1_100 = models.TextField(db_column='PURPOSE_CODE1_100', blank=True, null=True)  # Field name made lowercase.
    purpose_code2_102 = models.TextField(db_column='PURPOSE_CODE2_102', blank=True, null=True)  # Field name made lowercase.
    explanation_110 = models.TextField(db_column='EXPLANATION_110', blank=True, null=True)  # Field name made lowercase.
    xfer_type_120 = models.TextField(db_column='XFER_TYPE_120', blank=True, null=True)  # Field name made lowercase.
    chkbox_130 = models.TextField(db_column='CHKBOX_130', blank=True, null=True)  # Field name made lowercase.
    crerec_uid = models.TextField(db_column='CREREC_UID', blank=True, null=True)  # Field name made lowercase.
    crerec_date = models.TextField(db_column='CREREC_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATA_CONTRIBUTIONS'


class DataFilers(models.Model):
    #filer_id = models.TextField(db_column='FILER_ID', blank=True, null=True)  # Field name made lowercase.
    filer_id = models.CharField(db_column='FILER_ID', primary_key=True, max_length=16)  # Field name made lowercase.
    filer_name = models.TextField(db_column='FILER_NAME', blank=True, null=True)  # Field name made lowercase.
    filer_type = models.TextField(db_column='FILER_TYPE', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    committee_type = models.IntegerField(db_column='COMMITTEE_TYPE', blank=True, null=True)  # Field name made lowercase.
    office = models.IntegerField(db_column='OFFICE', blank=True, null=True)  # Field name made lowercase.
    district = models.IntegerField(db_column='DISTRICT', blank=True, null=True)  # Field name made lowercase.
    treas_first_name = models.TextField(db_column='TREAS_FIRST_NAME', blank=True, null=True)  # Field name made lowercase.
    treas_last_name = models.TextField(db_column='TREAS_LAST_NAME', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='ADDRESS', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='CITY', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    zip = models.IntegerField(db_column='ZIP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATA_FILERS'


class Dc1(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.
    filer_id = models.ForeignKey('Df1', models.DO_NOTHING, db_column='FILER_ID', blank=True, null=True)  # Field name made lowercase.
    freport_id = models.TextField(db_column='FREPORT_ID', blank=True, null=True)  # Field name made lowercase.
    transaction_code = models.TextField(db_column='TRANSACTION_CODE', blank=True, null=True)  # Field name made lowercase.
    e_year = models.IntegerField(db_column='E_YEAR', blank=True, null=True)  # Field name made lowercase.
    t3_trid = models.IntegerField(db_column='T3_TRID', blank=True, null=True)  # Field name made lowercase.
    date1_10 = models.TextField(db_column='DATE1_10', blank=True, null=True)  # Field name made lowercase.
    date2_12 = models.TextField(db_column='DATE2_12', blank=True, null=True)  # Field name made lowercase.
    contrib_code_20 = models.TextField(db_column='CONTRIB_CODE_20', blank=True, null=True)  # Field name made lowercase.
    contrib_type_code_25 = models.TextField(db_column='CONTRIB_TYPE_CODE_25', blank=True, null=True)  # Field name made lowercase.
    corp_30 = models.TextField(db_column='CORP_30', blank=True, null=True)  # Field name made lowercase.
    first_name_40 = models.TextField(db_column='FIRST_NAME_40', blank=True, null=True)  # Field name made lowercase.
    mid_init_42 = models.TextField(db_column='MID_INIT_42', blank=True, null=True)  # Field name made lowercase.
    last_name_44 = models.TextField(db_column='LAST_NAME_44', blank=True, null=True)  # Field name made lowercase.
    addr_1_50 = models.TextField(db_column='ADDR_1_50', blank=True, null=True)  # Field name made lowercase.
    city_52 = models.TextField(db_column='CITY_52', blank=True, null=True)  # Field name made lowercase.
    state_54 = models.TextField(db_column='STATE_54', blank=True, null=True)  # Field name made lowercase.
    zip_56 = models.IntegerField(db_column='ZIP_56', blank=True, null=True)  # Field name made lowercase.
    check_no_60 = models.TextField(db_column='CHECK_NO_60', blank=True, null=True)  # Field name made lowercase.
    check_date_62 = models.TextField(db_column='CHECK_DATE_62', blank=True, null=True)  # Field name made lowercase.
    amount_70 = models.IntegerField(db_column='AMOUNT_70', blank=True, null=True)  # Field name made lowercase.
    amount2_72 = models.TextField(db_column='AMOUNT2_72', blank=True, null=True)  # Field name made lowercase.
    description_80 = models.TextField(db_column='DESCRIPTION_80', blank=True, null=True)  # Field name made lowercase.
    other_recpt_code_90 = models.TextField(db_column='OTHER_RECPT_CODE_90', blank=True, null=True)  # Field name made lowercase.
    purpose_code1_100 = models.TextField(db_column='PURPOSE_CODE1_100', blank=True, null=True)  # Field name made lowercase.
    purpose_code2_102 = models.TextField(db_column='PURPOSE_CODE2_102', blank=True, null=True)  # Field name made lowercase.
    explanation_110 = models.TextField(db_column='EXPLANATION_110', blank=True, null=True)  # Field name made lowercase.
    xfer_type_120 = models.TextField(db_column='XFER_TYPE_120', blank=True, null=True)  # Field name made lowercase.
    chkbox_130 = models.TextField(db_column='CHKBOX_130', blank=True, null=True)  # Field name made lowercase.
    crerec_uid = models.TextField(db_column='CREREC_UID', blank=True, null=True)  # Field name made lowercase.
    crerec_date = models.TextField(db_column='CREREC_DATE', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'DC1'


class Df1(models.Model):
    filer_id = models.CharField(db_column='FILER_ID', primary_key=True, max_length=16)  # Field name made lowercase.
    filer_name = models.TextField(db_column='FILER_NAME', blank=True, null=True)  # Field name made lowercase.
    filer_type = models.TextField(db_column='FILER_TYPE', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    committee_type = models.IntegerField(db_column='COMMITTEE_TYPE', blank=True, null=True)  # Field name made lowercase.
    office = models.IntegerField(db_column='OFFICE', blank=True, null=True)  # Field name made lowercase.
    district = models.IntegerField(db_column='DISTRICT', blank=True, null=True)  # Field name made lowercase.
    treas_first_name = models.TextField(db_column='TREAS_FIRST_NAME', blank=True, null=True)  # Field name made lowercase.
    treas_last_name = models.TextField(db_column='TREAS_LAST_NAME', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='ADDRESS', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='CITY', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    zip = models.IntegerField(db_column='ZIP', blank=True, null=True)  # Field name made lowercase.



    def get_absolute_url(self):
        return reverse('filers_detail', args=[str(self.filer_id)])


    class Meta:
        managed = False
        db_table = 'DF1'

"""
class Df1Admin(admin.ModelAdmin):

    list_display = (filer_id, filer_name, filer_type, status)
"""
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


class HowdyDf1(models.Model):
    filer_id = models.CharField(max_length=16)
    filer_name = models.TextField(db_column='FILER_NAME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'howdy_df1'
