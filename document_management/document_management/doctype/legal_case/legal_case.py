# Copyright (c) 2022, alantechnologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LegalCase(Document):
	pass

@frappe.whitelist()
def get_outstanding(company,customer):
	ot=frappe.db.sql(
			"""
		select sum(debit_in_account_currency) - sum(credit_in_account_currency) as outst
		from `tabGL Entry`
		where party_type = 'Customer' and company=%s and party=%s
		and is_cancelled = 0
		group by company""",
			(company, customer),as_dict=1,debug=0
		)
	if ot:
		return ot[0].outst
	else:
		return '0'

@frappe.whitelist()
def get_payments(customer,case_initiated_date):
	return frappe.db.get_all('GL Entry',filters={'party':customer,'posting_date':['>',case_initiated_date],'credit':['>',0]},fields=['voucher_type','voucher_no','account','credit','posting_date'])