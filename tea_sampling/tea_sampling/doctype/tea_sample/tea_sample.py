# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import datetime,timedelta
from frappe.utils import getdate, add_days, add_years, cstr,formatdate, strip
from erpnext.stock.stock_ledger import get_previous_sle, NegativeStockError
from frappe.model.naming import make_autoname
from frappe import _
from frappe.model.mapper import get_mapped_doc
from frappe import utils
class TeaSample(Document):
	def autoname(self):
		#estateabr = frappe.db.get_value("Estate",{"estate_name": self.estatename}, "abbreviation")
		self.name = make_autoname("SAM"+ "/" +self.customer_name+ "/.####")
