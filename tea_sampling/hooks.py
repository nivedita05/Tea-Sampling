# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "tea_sampling"
app_title = "Tea Sampling"
app_publisher = "Frappe"
app_description = "App to maintain the tea sampling related information"
app_icon = "octicon octicon-file-directory"
app_color = "Orange"
app_email = "info@frappe.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tea_sampling/css/tea_sampling.css"
# app_include_js = "/assets/tea_sampling/js/tea_sampling.js"

# include js, css files in header of web template
# web_include_css = "/assets/tea_sampling/css/tea_sampling.css"
# web_include_js = "/assets/tea_sampling/js/tea_sampling.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "tea_sampling.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "tea_sampling.install.before_install"
# after_install = "tea_sampling.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tea_sampling.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tea_sampling.tasks.all"
# 	],
# 	"daily": [
# 		"tea_sampling.tasks.daily"
# 	],
# 	"hourly": [
# 		"tea_sampling.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tea_sampling.tasks.weekly"
# 	]
# 	"monthly": [
# 		"tea_sampling.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "tea_sampling.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tea_sampling.event.get_events"
# }

