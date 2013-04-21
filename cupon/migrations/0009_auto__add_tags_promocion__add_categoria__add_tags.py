# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tags_promocion'
        db.create_table(u'cupon_tags_promocion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('promocion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cupon.Promocion'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cupon.Tags'])),
        ))
        db.send_create_signal('cupon', ['Tags_promocion'])

        # Adding model 'Categoria'
        db.create_table(u'cupon_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal('cupon', ['Categoria'])

        # Adding model 'Tags'
        db.create_table(u'cupon_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cupon.Categoria'])),
        ))
        db.send_create_signal('cupon', ['Tags'])


    def backwards(self, orm):
        # Deleting model 'Tags_promocion'
        db.delete_table(u'cupon_tags_promocion')

        # Deleting model 'Categoria'
        db.delete_table(u'cupon_categoria')

        # Deleting model 'Tags'
        db.delete_table(u'cupon_tags')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cupon.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'cupon.confpromocion': {
            'Meta': {'object_name': 'ConfPromocion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'precio_x_cupon': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        'cupon.cupon': {
            'Meta': {'object_name': 'Cupon'},
            'canjeado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_promocion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cupon.Promocion']"}),
            'num_cupon': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'cupon.promocion': {
            'Meta': {'object_name': 'Promocion'},
            'activo': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'confPromocion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cupon.ConfPromocion']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_publicacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_termino': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresa.Empresa']"}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'num_limite': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'cupon.tags': {
            'Meta': {'object_name': 'Tags'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cupon.Categoria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'cupon.tags_promocion': {
            'Meta': {'object_name': 'Tags_promocion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'promocion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cupon.Promocion']"}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cupon.Tags']"})
        },
        'empresa.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'giro': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'nombre_encargado': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'num_exterior': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'num_interior': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cupon']