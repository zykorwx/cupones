# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Empresa'
        db.create_table('empresa_empresa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('calle', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('num_exterior', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('num_interior', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('colonia', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('municipio', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('delegacion', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('giro', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre_encargado', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('empresa', ['Empresa'])


    def backwards(self, orm):
        # Deleting model 'Empresa'
        db.delete_table('empresa_empresa')


    models = {
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

    complete_apps = ['empresa']