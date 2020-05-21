from zeep import Client



cliente = Client(wsdl='http://www.dneonline.com/calculator.asmx?WSDL')
print("Suma",cliente.service.Add(5,2))
print("Division",cliente.service.Divide(4,2))
print("Multiplicacion",cliente.service.Multiply(4,2))
print("Resta",cliente.service.Subtract(4,2))


cliente2 = Client(wsdl='https://www.dataaccess.com/webservicesserver/NumberConversion.wso?wsdl')
print(cliente2.service.NumberToDollars(12.50))
print(cliente2.service.NumberToWords(12.00))





