import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def published_courses(category=None):
    filters={"published":1}
    if category: filters["category"]=category
    return frappe.get_all("Training Course", filters=filters, fields=["name","title","category","level","short_description","thumbnail","price","currency","is_paid","duration_hours","certificate_enabled"], order_by="modified desc")

@frappe.whitelist()
def enroll(course, learner=None):
    learner = learner or frappe.session.user
    if frappe.db.exists("Training Enrollment", {"course":course,"learner":learner}):
        return {"status":"exists","name":frappe.db.get_value("Training Enrollment", {"course":course,"learner":learner})}
    doc=frappe.get_doc({"doctype":"Training Enrollment","course":course,"learner":learner,"status":"Enrolled","enrollment_date":frappe.utils.today(),"progress_percent":0})
    doc.insert(ignore_permissions=True); return {"status":"created","name":doc.name}

@frappe.whitelist()
def my_learning():
    return frappe.get_all("Training Enrollment", filters={"learner":frappe.session.user}, fields=["name","course","status","progress_percent","completion_date","certificate"] , order_by="modified desc")

@frappe.whitelist()
def update_progress(enrollment, progress, lesson=None):
    doc=frappe.get_doc("Training Enrollment", enrollment); doc.progress_percent=min(100,max(0,float(progress)))
    doc.status="Completed" if doc.progress_percent>=100 else "In Progress"
    if doc.status=="Completed": doc.completion_date=frappe.utils.today()
    doc.save(ignore_permissions=True); return doc.as_dict()
