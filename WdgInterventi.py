# -*- coding: utf-8 -*-

"""
/***************************************************************************
Name                 : Omero RT
Description          : Omero plugin
Date                 : August 15, 2010 
copyright            : (C) 2010 by Giuseppe Sucameli (Faunalia)
email                : sucameli@faunalia.it
 ***************************************************************************/

Omero plugin
Works done from Faunalia (http://www.faunalia.it) with funding from Regione 
Toscana - S.I.T.A. (http://www.regione.toscana.it/territorio/cartografia/index.html)

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.wdgInterventi_ui import Ui_Form
from AutomagicallyUpdater import *

class WdgInterventi(QWidget, MappingOne2One, Ui_Form):

	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		MappingOne2One.__init__(self, "INTERVENTO_EDIFICIO")
		self.setupUi(self)
		self.showOtherInfos(False)

		self.SCHEDA_EDIFICIOID.hide()

		# carica i widget multivalore con i valori delle relative tabelle
		tablesDict = {
			self.ZZ_QUALITA_INFORMAZIONEID: AutomagicallyUpdater.ZZTable( "ZZ_QUALITA_INFORMAZIONE" ),
			self.ZZ_TIPO_INTERVENTOID: AutomagicallyUpdater.ZZTable( "ZZ_TIPO_INTERVENTO" ),
			self.ZZ_NORMATIVA_SISMICAID: AutomagicallyUpdater.ZZTable( "ZZ_NORMATIVA_SISMICA" )
		}
		self.setupTablesUpdater(tablesDict)
		self.loadTables()

		# mappa i widget con i campi delle tabelle
		childrenList = [
			self.SCHEDA_EDIFICIOID, 
			(self.ANNO_PROGETTAZIONE, AutomagicallyUpdater.OPTIONAL),
			self.ZZ_QUALITA_INFORMAZIONEID,
			(self.DESCRIZ_INTERV, AutomagicallyUpdater.OPTIONAL),
			(self.TITOLO_ABILITATIVO, AutomagicallyUpdater.OPTIONAL),
			(self.DATA_TITOLO_ABILITATIVO, AutomagicallyUpdater.OPTIONAL),
			self.ZZ_TIPO_INTERVENTOID,
			self.INTERVENTO_IN_CORSO, 
			(self.ZZ_NORMATIVA_SISMICAID, AutomagicallyUpdater.OPTIONAL)
		]
		self.setupValuesUpdater(childrenList)

	def showOtherInfos(self, show=True):
		self.EPOCA_COSTRUTTIVA.setVisible(show)

	def toHtml(self, index):
		descrizione = self.getValue(self.DESCRIZ_INTERV)
		titolo_abilitivo = self.getValue(self.TITOLO_ABILITATIVO)

		return QString( u"""
<table class="white border">
	<tr class="line">
		<td colspan="4" class="subtitle">Interventi strutturali successivi</td>
	</tr>
	<tr class="line">
		<td>Categoria di intervento</td><td class="value">%s</td>
		<td class="line">Normativa sismica di riferimento</td><td class="value">%s</td>
	</tr>
	<tr class="line">
		<td>Anno di progettazione</td><td class="value">%s</td>
		<td class="line">Qualit&agrave; dell'informazione</td><td class="value">%s</td>
	</tr>
	<tr class="line">
		<td>Descrizione dell'intervento</td><td colspan="3" class="value">%s</td>
	</tr>
	<tr class="line">
		<td>Titolo abilitativo n.</td><td class="value">%s</td>
		<td>data</td><td class="value">%s</td>
	</tr>
	<tr>
		<td>Intervento in corso</td><td colspan="3" class="value">%s</td>
	</tr>
</table>
""" % ( self.ZZ_TIPO_INTERVENTOID.currentText(), self.ZZ_NORMATIVA_SISMICAID.currentText(), self.getValue(self.ANNO_PROGETTAZIONE), self.ZZ_QUALITA_INFORMAZIONEID.currentText(), descrizione if descrizione != None else '', titolo_abilitivo if titolo_abilitivo != None else '', self.getValue(self.DATA_TITOLO_ABILITATIVO), "SI" if self.getValue(self.INTERVENTO_IN_CORSO) else "NO" )
)
