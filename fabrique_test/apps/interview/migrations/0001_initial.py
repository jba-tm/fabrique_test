# Generated by Django 3.2.3 on 2021-05-18 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='AnswerOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_interview.answerowner_set+', to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='ChoiceVariations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=255)),
                ('is_right', models.BooleanField()),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('status', models.CharField(choices=[('ACTIVE', 'active'), ('INACTIVE', 'inactive')], default='ACTIVE', max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='interview.interview')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_interview.question_set+', to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='AnonymousUserAnswerOwner',
            fields=[
                ('answerowner_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='interview.answerowner')),
                ('anonymous_user', models.UUIDField(default=uuid.uuid4, unique=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('interview.answerowner',),
        ),
        migrations.CreateModel(
            name='ChoiceQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='interview.question')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('interview.question',),
        ),
        migrations.CreateModel(
            name='MultiChoicesQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='interview.question')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('interview.question',),
        ),
        migrations.CreateModel(
            name='TextAnswer',
            fields=[
                ('answer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='interview.answer')),
                ('answer', models.TextField(max_length=1000)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('interview.answer',),
        ),
        migrations.CreateModel(
            name='TextQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='interview.question')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('interview.question',),
        ),
        migrations.AddField(
            model_name='answer',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='interview.answerowner'),
        ),
        migrations.AddField(
            model_name='answer',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_interview.answer_set+', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='interview.question'),
        ),
        migrations.CreateModel(
            name='UserAnswerOwner',
            fields=[
                ('answerowner_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='interview.answerowner')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('interview.answerowner',),
        ),
        migrations.CreateModel(
            name='MultiChoicesVariations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=255)),
                ('is_right', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='interview.multichoicesquestion')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='MultiChoicesAnswer',
            fields=[
                ('answer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='interview.answer')),
                ('answer', models.ManyToManyField(to='interview.ChoiceVariations')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('interview.answer',),
        ),
        migrations.AddField(
            model_name='choicevariations',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='interview.choicequestion'),
        ),
        migrations.CreateModel(
            name='ChoiceAnswer',
            fields=[
                ('answer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='interview.answer')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.choicevariations')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('interview.answer',),
        ),
    ]
