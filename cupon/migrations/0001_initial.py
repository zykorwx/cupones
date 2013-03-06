# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Promocion'
        db.create_table('cupon_promocion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresa.Empresa'])),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('fecha_publicacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_termino', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('num_limite', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(default='0', max_length=1)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('cupon', ['Promocion'])

        # Adding model 'Cupon'
        db.create_table('cupon_cupon', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_promocion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cupon.Promocion'])),
            ('num_cupon', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('cupon', ['Cupon'])


    def backwards(self, orm):
        # Deleting model 'Promocion'
        db.delete_table('cupon_promocion')

        # Deleting model 'Cupon'
        db.delete_table('cupon_cupon')


    models = {
        'cupon.cupon': {
            'Meta': {'object_name': 'Cupon'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_promocion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cupon.Promocion']"}),
            'num_cupon': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'cupon.promocion': {
            'Meta': {'object_name': 'Promocion'},
            'estado': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_publicacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_termino': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresa.Empresa']"}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'num_limite': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'empresa.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'delegacion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'giro': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_encargado': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'num_exterior': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'num_interior': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cupon']