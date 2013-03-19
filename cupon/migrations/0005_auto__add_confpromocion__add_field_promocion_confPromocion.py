# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ConfPromocion'
        db.create_table(u'cupon_confpromocion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('precio_x_cupon', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'cupon', ['ConfPromocion'])

        # Adding field 'Promocion.confPromocion'
        db.add_column(u'cupon_promocion', 'confPromocion',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['cupon.ConfPromocion']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ConfPromocion'
        db.delete_table(u'cupon_confpromocion')

        # Deleting field 'Promocion.confPromocion'
        db.delete_column(u'cupon_promocion', 'confPromocion_id')


    models = {
        u'cupon.confpromocion': {
            'Meta': {'object_name': 'ConfPromocion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'precio_x_cupon': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        u'cupon.cupon': {
            'Meta': {'object_name': 'Cupon'},
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_promocion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cupon.Promocion']"}),
            'num_cupon': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'cupon.promocion': {
            'Meta': {'object_name': 'Promocion'},
            'confPromocion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cupon.ConfPromocion']"}),
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