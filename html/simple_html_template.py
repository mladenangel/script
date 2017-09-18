template = '''<html><head><title>%(title)s</title></head>
<body><h1>%(title)s</h1><p>%(text)s</p></body></hml>'''
data = {'title':'My home page','text':'Wellcome!'}
print(template % data)
