from . import __version__ as app_version

app_name = "document_management"
app_title = "Document Management"
app_publisher = "alantechnologies"
app_description = "manage and notify on documents expiry"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "jayakumar@alantechnologies.net"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/document_management/css/document_management.css"
# app_include_js = "/assets/document_management/js/document_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/document_management/css/document_management.css"
# web_include_js = "/assets/document_management/js/document_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "document_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "document_management.install.before_install"
# after_install = "document_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "document_management.uninstall.before_uninstall"
# after_uninstall = "document_management.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "document_management.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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
scheduler_events = {

 	"daily": [
 		"document_management.insurance.doctype.insurance.update_insurance.update_insurance_status"
 	],

    }
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"document_management.tasks.all"
# 	],
# 	"daily": [
# 		"document_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"document_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"document_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"document_management.tasks.monthly"
# 	]
# }

# Testing
# -------
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                (
                    "Insurance-column_break_6",                    
                    "Insurance-section_break_12",
                ),
            ]
        ],
    },
    
]
# before_tests = "document_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "document_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "document_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"document_management.auth.validate"
# ]

