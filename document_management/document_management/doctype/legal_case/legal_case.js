// Copyright (c) 2022, alantechnologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Legal Case', {
	// refresh: function(frm) {

	// }
	company: function(frm, cdt, cdn) 
	{ 
		 var d = locals[cdt][cdn];
		 
		if(!frm.doc.company){
			
			return false;
			}
			
		if(!frm.doc.customer){
			
			return false;
			}	
			
		  
		frappe.call(
			{ 
				method: "document_management.document_management.doctype.legal_case.legal_case.get_outstanding",
				args: { 					
					'company':frm.doc.company,
					'customer':frm.doc.customer,
				},
				callback: function(r) 
					{ 
						if(r.message) 
							{ 
								d.outstanding_amount = flt(r.message,2); 
					            frm.refresh_fields()
							} 
					}
			});
	},
	customer: function(frm, cdt, cdn) 
	{ 
		 var d = locals[cdt][cdn];
		 
		if(!frm.doc.company){
			
			return false;
			}
			
		if(!frm.doc.customer){
			
			return false;
			}	
			
		  
		frappe.call(
			{ 
				method: "document_management.document_management.doctype.legal_case.legal_case.get_outstanding",
				args: { 					
					'company':frm.doc.company,
					'customer':frm.doc.customer,
				},
				callback: function(r) 
					{ 
						if(r.message) 
							{ 
								d.outstanding_amount = flt(r.message,2); 
					            frm.refresh_fields()
							} 
					}
			});
	}
});
