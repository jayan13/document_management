﻿# -*- coding: utf-8 -*-
# Copyright (c) 2017, Direction and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from distutils.log import debug
import frappe, erpnext
from frappe.utils import flt, cstr, nowdate, comma_and, cint, getdate
from frappe import throw, msgprint, _


@frappe.whitelist()
def get_limit(company,customer):

	#emprv=frappe.db.sql(""" select * from `tabExpense Request Item` where docstatus=1 and employee='{0}' and date between DATE_SUB('{2}', INTERVAL {1} YEAR) and '{2}' """.format(employee,exp_year,exp_date),as_dict=1,debug=0)
	return frappe.db.get_value('Customer Credit Limit', {'company': company,'parent':customer}, ['credit_limit'],debug=0) or 0
	
	
