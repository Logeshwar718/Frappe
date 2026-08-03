# Copyright (c) 2026, logeshwar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Test_Document(Document):
	def before_save(self):
		self.description="Default Description"