# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'pagoEmpresa'
        db.create_table(u'empresa_pagoempresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresa.Empresa'])),
            ('cantidad', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('fecha_pago', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('empresa', ['pagoEmpresa'])


    def backwards(self, orm):
        # Deleting model 'pagoEmpresa'
        db.delete_table(u'empresa_pagoempresa')


    models = {
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
        },
        'empresa.pagoempresa': {
            'Meta': {'object_name': 'pagoEmpresa'},
            'cantidad': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresa.Empresa']"}),
            'fecha_pago': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'empresa.userempresa': {
            'Meta': {'object_name': 'UserEmpresa'},
            'empresa': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['empresa.Empresa']", 'unique': 'True'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['empresa']