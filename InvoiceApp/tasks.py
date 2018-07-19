from __future__ import absolute_import
from celery import shared_task
from InvoiceApp.models import *
from OrderManagement.NotificationEngine.NotificationApp.CeleryTasks import NotifyTask
from django.forms.models import model_to_dict

@shared_task(name='tasks.generate_invoice')
class InvoiceTask:

	def __init__(self,*args):
		self.orderline_id   = args[0]
		self.generate()

	def generate(self):
		print "Creating Invoice"
		self.invoice = Invoice(**kwargs)
		self.generate_pdf()
		self.upload_invoice_to_s3()
		self.invoice.url = self.url
		self.invoice.save()
		self.notify_user()


	def upload_invoice_to_s3(self):
		print "Invoice uploaded to s3"
		self.url = "http://s3:/..."
		
		

	def generate_pdf(self):
		print "PDF generated"

	def notify_user(self):
		print "User notified"
		customer = model_to_dict(self.invoice.orderline.order.customer)
		invoice = model_to_dict(self.invoice)
		NotifyTask.apply_async(args=[customer,invoice],)


