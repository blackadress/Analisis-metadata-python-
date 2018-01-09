import argparse
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfparser import PDFDocument

def getMetaData(pdf, salida):
	try:
		metaData = {}

		pdfFile = open(pdf, 'rb')
		print("Obteniendo meta datos...")
		parser = PDFParser(pdfFile)
		doc = PDFDocument(parser)
		parser.set_document(doc)
		doc.set_parser(parser)

		if doc.info:
			print("Meta Datos encontrados!")
			info = doc.info[0]

			for etiqueta,valor in info.items():
				metaData[etiqueta] = valor
				if not salida:
					print(etiqueta, valor)

			if salida:
				print("Escribiendo a archivo...")
				with open(salida, 'w') as text:
					for (etiqueta, valor) in metaData.items():
						text.write(str(etiqueta) + "\t" + \
							str(valor) + "\n")

		if not info:
			print('Metadatos no presentes!')
		
	except:
		print("Operación fallida")
   
def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("pdf", help = "Nombre de un archivo pdf.")
	parser.add_argument("--salida", "-s", help = "Fichero donde se guardarán los metadatos obtenidos.")
	args = parser.parse_args()
	if args.pdf:
		getMetaData(args.pdf, args.salida)
	else:
		print(parser.usage)

if __name__ == '__main__':
	Main()