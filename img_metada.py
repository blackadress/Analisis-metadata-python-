import argparse
from PIL import Image
from PIL.ExifTags import TAGS

def getMetaData(img, salida):
	try:
		metaData = {}

		imagen = Image.open(img)
		print("Obteniendo meta datos...")
		info = imagen._getexif()
		if info:
			print("Meta datos encontrados!")
			for (etiqueta, valor) in info.items():
				nombreEtiqueta = TAGS.get(etiqueta, etiqueta)
				metaData[nombreEtiqueta] = valor
				if not salida:
					print(nombreEtiqueta, valor)

			if salida:
				print("Escribiendo a archivo...")
				with open(salida, 'w') as text:
					for (nombreEtiqueta, valor) in metaData.items():
						text.write(str(nombreEtiqueta) + "\t" + \
							str(valor) + "\n")

		if not info:
			print('Metadatos no presentes!')
		
	except:
		print("Operación fallida")

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("img", help = "Nombre de un archivo de imagen.")
	parser.add_argument("--salida","-s", help = "Fichero donde se guardarán los metadatos obtenidos.")
	args = parser.parse_args()
	if args.img:
		getMetaData(args.img, args.salida)
	else:
		print(parser.usage)

if __name__ == '__main__':
	Main()
