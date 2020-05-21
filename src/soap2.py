from zeep import Client


cliente3 = Client(wsdl='https://cvnet.cpd.ua.es/servicioweb/publicos/pub_gestdocente.asmx?wsdl')
print(cliente3.service.wsareasdpto('C','2011-12','B142'))
print(cliente3.service.wsareasdpto('C','V','E'))
