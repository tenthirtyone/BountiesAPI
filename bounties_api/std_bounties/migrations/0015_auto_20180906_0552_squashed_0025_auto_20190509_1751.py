# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-29 20:39
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# std_bounties.migrations.0019_auto_20190331_1807

class Migration(migrations.Migration):

    replaces = [('std_bounties', '0015_auto_20180906_0552'), ('std_bounties', '0016_bounty_image_preview'), ('std_bounties', '0017_auto_20190131_0525'), ('std_bounties', '0018_auto_20190331_1807'), ('std_bounties', '0020_auto_20190331_1916'),
                ('std_bounties', '0021_auto_20190401_1836'), ('std_bounties', '0022_auto_20190401_1856'), ('std_bounties', '0023_auto_20190502_2217'), ('std_bounties', '0024_auto_20190509_1256'), ('std_bounties', '0025_auto_20190509_1751')]

    dependencies = [
        ('user', '0027_auto_20190223_1548'),
        ('std_bounties', '0014_remove_category_platform'),
        ('user', '0024_user_dismissed_signup_prompt'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='private_fulfillments',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='draftbounty',
            name='private_fulfillments',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='image_preview',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.CreateModel(
            name='FulfillerApplication',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('state', models.CharField(choices=[
                 ('A', 'accepted'), ('R', 'rejected'), ('P', 'pending')], default='P', max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.AddField(
            model_name='bounty',
            name='fulfillers_need_approval',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='draftbounty',
            name='fulfillers_need_approval',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fulfillerapplication',
            name='bounty',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='std_bounties.Bounty'),
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('refunded', models.BooleanField(default=False)),
                ('contribution_id', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=0, max_digits=64)),
                ('calculated_amount', models.DecimalField(
                    decimal_places=30, default=0, max_digits=70, null=True)),
                ('usd_amount', models.FloatField(default=0)),
                ('platform', models.CharField(blank=True,
                                              default='bounties-network', max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('raw_event_data',
                 django.contrib.postgres.fields.jsonb.JSONField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='sourceDirectoryHash',
            new_name='attached_data_hash',
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='sourceFileName',
            new_name='attached_filename',
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='webReferenceURL',
            new_name='attached_url',
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='bountyStage',
            new_name='bounty_stage',
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='calculated_fulfillmentAmount',
            new_name='calculated_fulfillment_amount',
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='experienceLevel',
            new_name='experience_level',
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='tokenContract',
            new_name='token_contract',
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='tokenDecimals',
            new_name='token_decimals',
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='tokenLockPrice',
            new_name='token_lock_price',
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='tokenSymbol',
            new_name='token_symbol',
        ),
        migrations.RenameField(
            model_name='bountystate',
            old_name='bountyStage',
            new_name='bounty_stage',
        ),
        migrations.RenameField(
            model_name='draftbounty',
            old_name='sourceDirectoryHash',
            new_name='attached_data_hash',
        ),
        migrations.RenameField(
            model_name='draftbounty',
            old_name='sourceFileName',
            new_name='attached_filename',
        ),
        migrations.RenameField(
            model_name='draftbounty',
            old_name='webReferenceURL',
            new_name='attached_url',
        ),
        migrations.RenameField(
            model_name='draftbounty',
            old_name='calculated_fulfillmentAmount',
            new_name='calculated_fulfillment_amount',
        ),
        migrations.RenameField(
            model_name='draftbounty',
            old_name='experienceLevel',
            new_name='experience_level',
        ),
        migrations.RenameField(
            model_name='draftbounty',
            old_name='tokenContract',
            new_name='token_contract',
        ),
        migrations.RenameField(
            model_name='draftbounty',
            old_name='tokenDecimals',
            new_name='token_decimals',
        ),
        migrations.RenameField(
            model_name='draftbounty',
            old_name='tokenSymbol',
            new_name='token_symbol',
        ),
        migrations.RemoveField(
            model_name='bounty',
            name='arbiter',
        ),
        migrations.RemoveField(
            model_name='bounty',
            name='fulfillmentAmount',
        ),
        migrations.RemoveField(
            model_name='bounty',
            name='issuer_address',
        ),
        migrations.RemoveField(
            model_name='bounty',
            name='issuer_email',
        ),
        migrations.RemoveField(
            model_name='bounty',
            name='issuer_githubUsername',
        ),
        migrations.RemoveField(
            model_name='bounty',
            name='issuer_name',
        ),
        migrations.RemoveField(
            model_name='bounty',
            name='sourceFileHash',
        ),
        migrations.RemoveField(
            model_name='draftbounty',
            name='arbiter',
        ),
        migrations.RemoveField(
            model_name='draftbounty',
            name='fulfillmentAmount',
        ),
        migrations.RemoveField(
            model_name='draftbounty',
            name='issuer_address',
        ),
        migrations.RemoveField(
            model_name='draftbounty',
            name='issuer_email',
        ),
        migrations.RemoveField(
            model_name='draftbounty',
            name='issuer_githubUsername',
        ),
        migrations.RemoveField(
            model_name='draftbounty',
            name='issuer_name',
        ),
        migrations.RemoveField(
            model_name='draftbounty',
            name='sourceFileHash',
        ),
        migrations.AddField(
            model_name='bounty',
            name='approvers',
            field=models.ManyToManyField(
                related_name='std_bounties_bounty_relateda', to='user.User'),
        ),
        migrations.AddField(
            model_name='bounty',
            name='contract_state',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='contract_version',
            field=models.IntegerField(
                choices=[(1, 'v1'), (2, 'v2')], default=1),
        ),
        migrations.AddField(
            model_name='bounty',
            name='fulfillment_amount',
            field=models.DecimalField(
                decimal_places=0, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='bounty',
            name='issuers',
            field=models.ManyToManyField(
                related_name='std_bounties_bounty_related', to='user.User'),
        ),
        migrations.AddField(
            model_name='bounty',
            name='raw_event_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='raw_ipfs_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='token_version',
            field=models.IntegerField(
                choices=[(0, 'Ether'), (20, 'ERC-20'), (721, 'ERC-721')], null=True),
        ),
        migrations.AddField(
            model_name='draftbounty',
            name='approvers',
            field=models.ManyToManyField(
                related_name='std_bounties_draftbounty_relateda', to='user.User'),
        ),
        migrations.AddField(
            model_name='draftbounty',
            name='fulfillment_amount',
            field=models.DecimalField(
                decimal_places=0, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='draftbounty',
            name='issuers',
            field=models.ManyToManyField(
                related_name='std_bounties_draftbounty_related', to='user.User'),
        ),
        migrations.AddField(
            model_name='draftbounty',
            name='token_version',
            field=models.IntegerField(
                choices=[(0, 'Ether'), (20, 'ERC-20'), (721, 'ERC-721')], null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='contract_event_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='fulfillment',
            name='contract_version',
            field=models.IntegerField(
                choices=[(1, 'v1'), (2, 'v2')], default=1),
        ),
        migrations.AddField(
            model_name='fulfillment',
            name='fulfillers',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=128), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='id',
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='platform',
            field=models.CharField(
                blank=True, default='bounties-network', max_length=128),
        ),
        migrations.AddField(
            model_name='contribution',
            name='bounty',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='std_bounties.Bounty'),
        ),
        migrations.AddField(
            model_name='contribution',
            name='contributor',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.RemoveField(
            model_name='bounty',
            name='paysTokens',
        ),
        migrations.RemoveField(
            model_name='draftbounty',
            name='paysTokens',
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='schemaName',
            new_name='schema_name',
        ),
        migrations.RenameField(
            model_name='bounty',
            old_name='schemaVersion',
            new_name='schema_version',
        ),
        migrations.RenameField(
            model_name='draftbounty',
            old_name='schemaName',
            new_name='schema_name',
        ),
        migrations.RenameField(
            model_name='draftbounty',
            old_name='schemaVersion',
            new_name='schema_version',
        ),
        migrations.AlterField(
            model_name='bounty',
            name='attached_data_hash',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='attached_filename',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='attached_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='draftbounty',
            name='attached_data_hash',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='draftbounty',
            name='attached_filename',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='draftbounty',
            name='attached_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='issuer_address',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='bounty',
            name='issuer_email',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='bounty',
            name='issuer_githubUsername',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='bounty',
            name='issuer_name',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='draftbounty',
            name='issuer_address',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='draftbounty',
            name='issuer_email',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='draftbounty',
            name='issuer_githubUsername',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='draftbounty',
            name='issuer_name',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='draftbounty',
            name='sourceDirectoryHash',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='draftbounty',
            name='sourceFileName',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
