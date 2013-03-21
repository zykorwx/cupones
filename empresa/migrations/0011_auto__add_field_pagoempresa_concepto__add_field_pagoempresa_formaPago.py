# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'pagoEmpresa.concepto'
        db.add_column(u'empresa_pagoempresa', 'concepto',
                      self.gf('django.db.models.fields.CharField')(default='1', max_length=1),
                      keep_default=False)

        # Adding field 'pagoEmpresa.formaPago'
        db.add_column(u'empresa_pagoempresa', 'formaPago',
                      self.gf('django.db.models.fields.CharField')(default='0', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'pagoEmpresa.concepto'
        db.delete_column(u'empresa_pagoempresa', 'concepto')

        # Deleting field 'pagoEmpresa.formaPago'
        db.delete_column(u'empresa_pagoempresa', 'formaPago')


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
            'concepto': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '1'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresa.Empresa']"}),
            'fecha_pago': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'formaPago': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
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