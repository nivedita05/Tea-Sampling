// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tea Sample', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on("Tea Sample", "validate", function(frm) {
  for(var i in frm.doc.plucking_sheet){
     frm.doc.plucking_sheet[i].date = frm.doc.date;
     frm.doc.plucking_sheet[i].garden = frm.doc.garden;
     }
  });

frappe.ui.form.on("Tae Sample", "validate", function(frm) {
    frm.name_ser="";
    name=frm.doc.garden+":"+frm.doc.date;
    frm.set_value("name_ser",name);
});
