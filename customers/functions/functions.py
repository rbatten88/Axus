def upload_attachment(f):
	with open('customers/attachments'+ f.name,'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
