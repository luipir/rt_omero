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

from MultiTabInterventi import MultiTabInterventi
from AutomagicallyUpdater import *

class SezInterventi(QWidget, MappingPart):

	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		MappingPart.__init__(self, "SCHEDA_EDIFICIO")
		self.setupUi()

		# mappa i widget con i campi delle tabelle
		childrenList = [
			self.INTERVENTO_EDIFICIO.firstTab.EPOCA_COSTRUTTIVA,
			self.INTERVENTO_EDIFICIO
		]
		self.setupValuesUpdater(childrenList)

	def setupUi(self):
		gridLayout = QGridLayout(self)
		self.INTERVENTO_EDIFICIO = MultiTabInterventi(self)
		gridLayout.addWidget(self.INTERVENTO_EDIFICIO, 0, 0, 1, 1)

	def toHtml(self):
		epoca = self.INTERVENTO_EDIFICIO.firstTab.EPOCA_COSTRUTTIVA
		inizio_epoca_costruttiva = self.getValue(epoca.INIZIO_EPOCA_COSTRUTTIVA)
		fine_epoca_costruttiva = self.getValue(epoca.FINE_EPOCA_COSTRUTTIVA)

		return u"""
<div id="sez4" class="block">
<p class="section">SEZIONE A4 - DATAZIONE INTERVENTI DELL'EDIFICIO</p>
<table class="white border">
	<tr class="line">
		<td colspan="6" class="subtitle">Epoca di impianto</td>
	</tr>
	<tr>
		<td class="subtitle">Inizio della costruzione</td><td class="value">%s</td>
		<td class="subtitle line">Fine della costruzione</td><td class="value">%s</td>
		<td class="line">Qualit&agrave; dell'informazione</td><td class="value">%s</td>
	</tr>
</table>
%s
</div>
""" % ( inizio_epoca_costruttiva if inizio_epoca_costruttiva != None else '', fine_epoca_costruttiva if fine_epoca_costruttiva != None else '', epoca.ZZ_QUALITA_INFORMAZIONE_EPOCA_COSTRUTTIVAID.currentText(), self.INTERVENTO_EDIFICIO.toHtml() )
