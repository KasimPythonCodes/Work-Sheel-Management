# Generated by Django 4.0.4 on 2022-11-01 12:58

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('1', 'Super-Admin'), ('2', 'Manager'), ('3', 'Supervizor')], max_length=150)),
                ('profile_pic', models.ImageField(upload_to='SuperAdmin/profile_pic')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Supervizor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(upload_to='Supervizor/Staff_profile_pic')),
                ('designation', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Staff_TL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Line_No', models.CharField(max_length=15)),
                ('Manpowers', models.CharField(blank=True, max_length=10, null=True)),
                ('Target', models.CharField(blank=True, max_length=10, null=True)),
                ('nine_to_ten_in', models.CharField(blank=True, max_length=10, null=True)),
                ('ten_to_eleven_in', models.CharField(blank=True, max_length=10, null=True)),
                ('eleven_to_twelve_in', models.CharField(blank=True, max_length=10, null=True)),
                ('twelve_to_one_in', models.CharField(blank=True, max_length=10, null=True)),
                ('one_to_two_in', models.CharField(blank=True, max_length=10, null=True)),
                ('two_to_three_in', models.CharField(blank=True, max_length=10, null=True)),
                ('three_to_four_in', models.CharField(blank=True, max_length=10, null=True)),
                ('four_to_five_in', models.CharField(blank=True, max_length=10, null=True)),
                ('nine_to_ten_out', models.CharField(blank=True, max_length=10, null=True)),
                ('ten_to_eleven_out', models.CharField(blank=True, max_length=10, null=True)),
                ('eleven_to_twelve_out', models.CharField(blank=True, max_length=10, null=True)),
                ('twelve_to_one_out', models.CharField(blank=True, max_length=10, null=True)),
                ('one_to_two_out', models.CharField(blank=True, max_length=10, null=True)),
                ('two_to_three_out', models.CharField(blank=True, max_length=10, null=True)),
                ('three_to_four_out', models.CharField(blank=True, max_length=10, null=True)),
                ('four_to_five_out', models.CharField(blank=True, max_length=10, null=True)),
                ('nine_to_ten_dis', models.CharField(blank=True, max_length=10, null=True)),
                ('ten_to_eleven_dis', models.CharField(blank=True, max_length=10, null=True)),
                ('eleven_to_twelve_dis', models.CharField(blank=True, max_length=10, null=True)),
                ('twelve_to_one_dis', models.CharField(blank=True, max_length=10, null=True)),
                ('one_to_two_dis', models.CharField(blank=True, max_length=10, null=True)),
                ('two_to_three_dis', models.CharField(blank=True, max_length=10, null=True)),
                ('three_to_four_dis', models.CharField(blank=True, max_length=10, null=True)),
                ('four_to_five_dis', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_asign_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.supervizor')),
            ],
            options={
                'verbose_name': 'TABLE DATA',
            },
        ),
    ]
