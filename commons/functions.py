import os
import sys
import csv
import threading
import traceback
import decimal
from datetime import datetime, date, timedelta
from shutil import rmtree

from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

# local settings
from portfolio.local_settings import config

def register_app_models(name):
    app_models = apps.get_app_config(name).get_models()
    loaded = 0
    ignored = 0
    for model in app_models:
        try:
            admin.site.register(model)
            loaded += 1
        except AlreadyRegistered:
            ignored += 1
    return f"loaded:{loaded}, ignored:{ignored}"

def progressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
	percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
	filledLength = int(length * iteration // total)
	bar = fill * filledLength + '-' * (length - filledLength)
	print(f'\r{prefix} |{bar}| {percent}% {suffix} de {total}', end="")
	# Print New Line on Complete
	if iteration == total: 
		print()

class ProgressBar():
	"""
	self.progress_bar = ProgressBar()
	self.progress_bar.reset(total)
		self.progress_bar.update(prefix = f" {str_fecha_analisis} ", suffix = f" Copiando: {nombre_ftp} ")
		OR
		self.progress_bar.update(" Carga COMERSSIA ")
	self.progress_bar.terminate()
	"""
	def __init__(self, total = 100, decimals = 1, length = 50, fill = '█'):
		self.total = total
		self.decimals = decimals
		self.length = length
		self.fill = fill

		self.iteration = 0
		self.prev = 0
		self.current = 0

	def reset(self, total = 100, decimals = 1, length = 50, fill = '█'):
		self.total = total
		self.decimals = decimals
		self.length = length
		self.fill = fill

		self.iteration = 0
		self.prev = 0
		self.current = 0

		self.prev_lenght = 0

	def update(self, prefix = '', suffix = ''):
		try:
			self.iteration += 1
			self.current = round(100*(self.iteration/self.total), self.decimals)
			if self.current > self.prev:
				self.prev = self.current
				value = 100 * (self.iteration / float(self.total))
				percent = f"{value:.{self.decimals}f}"
				filledLength = int(self.length * (self.iteration / self.total))
				bar = self.fill * filledLength + '-' * (self.length - filledLength)
				# print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
				mensaje = f'{prefix} |{bar}| {percent}% {suffix}'
				if self.prev_lenght > len(mensaje):
					delta = self.prev_lenght - len(mensaje)
					print((f'\r{mensaje}'+" "*delta), end = '\r')
				else:
					print((f'\r{mensaje}'), end = '\r')
				self.prev_lenght = len(mensaje)
				if self.iteration == self.total:
					self.terminate()
		except:
			traceback.format_exc()
	
	def terminate(self, saltos = 1):
		print("\n"*saltos)

def search_files(ruta, ext=""):
	files_names = []
	cont = 0
	for root, dirs, files in os.walk("{}".format(ruta)):
		for file in files:
			if ext != "" and file.endswith(".{}".format(ext)):
				cont += 1
			else:
				cont += 1
	cont2 = 0

	for root, dirs, files in os.walk("{}".format(ruta)):
		for file in files:
			if ext == "" or file.endswith(".{}".format(ext)):
				cont2 += 1
				name = str(root).replace("\\","/")+"/"+file
				files_names.append(name)
				# progressBar(cont2, cont, prefix = 'Progreso:', suffix = '', length = 50)
	return files_names

def search_dirs(ruta, name, exclude_dirs=[]):
	def correct_dir(root):
		for exclude in exclude_dirs:
			if exclude in root:
				return False
		return True
	correct_dirs = []
	for root, dirs, files in os.walk(f"{ruta}"):
		for dir in dirs:
			if name == dir and correct_dir(root):
				ms = root.replace('\\','/')
				correct_dirs.append(f"{ms}/{name}")
	return correct_dirs

def mr_dir(path):
	try:
		rmtree(path)
		return True
	except:
		return False

def remove_dir_files(path, ext=""):
	try:
		files = search_files(path, ext)
		for file in files:
			os.remove(file)
	except:
		return False

def is_double(valor):
	try:
		nuevo = float(valor)
		return True
	except:
		return False

def convert_decimal(valor):
	try:
		if isinstance(valor, decimal.Decimal):
			return float(valor)
		else:
			return valor
	except:
		return valor

def is_dir(path):
	try:
		if os.path.isdir(path):
			return True
		else:
			return False
	except:
		return False

def mk_dir(path):
	try:
		if os.mkdir(path):
			return True
		else:
			return False
	except:
		return False

def is_file(path):
	try:
		if os.path.isfile(path):
			return True
		else:
			return False
	except:
		return False

def get_date(str_date = ""):
	"""Get date
	
	Return datetime from String in format "yy-mm-dd" or "yyyy-mm-dd"

		Parametros:
		Ninguno.

		Retorna:
		hoy -- date
	"""
	try:
		if str_date == "":
			hoy = date.today()
			return hoy
		else:
			if len(str_date) == 8:
				return datetime.strptime(str_date, '%y-%m-%d')
			else:
				return datetime.strptime(str_date, '%Y-%m-%d')
	except:
		traceback.print_exc()

def get_date_days_ago(days):
	"""Get date days ago
	
	Use the current date and calculate a new date days ago

		Parametros:
		days -- int

		Retorna:
		previous_date -- date
	"""
	try:
		current = date.today()
		days_ago = timedelta(days = days)
		previous_date = current - days_ago
		
		return previous_date
	except:
		traceback.print_exc()

def get_same_date_last_year(base_date):
	"""Get same date last year
	
	Take a date and calculate the same date last year

		parameters:
		base_date -- str or date

		Return:
		calculated_date -- date
	"""
	def last_year(year, month, day):
		years = int(year)-1
		months = int(month)
		days = int(day)
		return date(years, months, days)
	
	current_year = ""
	current_month = ""
	current_day = ""
	if type(base_date) == str:
		current_year, current_month, current_day = base_date.split("-")
	if type(base_date) == date:
		dt = base_date.__str__()
		current_year, current_month, current_day = dt.split("-")
	calculated_date = last_year(current_year, current_month, current_day)
	return calculated_date

def read_csv(nombre_archivo, ignorar_cabecera = True, ignorar_total = True, col_ini = None, col_fin = None):
	try:
		def transformar_dato(dato):
			try:
				return float(dato.replace(".",","))
			except:
				pass
			try:
				return float(dato.replace(",","."))
			except:
				pass
			return dato
		matriz = []
		fl_test = open(nombre_archivo, "r", encoding="utf-8")
		csv_test = csv.reader(fl_test, delimiter=',')
		init = None
		fin = None
		if ignorar_cabecera:
			init = 1
		if ignorar_total:
			fin = -1
		csv_test = list(csv_test)[init:fin]
		if len(csv_test) > 0:
			for index, line in enumerate(csv_test):
				new_line = []
				for item in line:
					new_line.append(transformar_dato(item))
					
				matriz.append(new_line[col_ini:col_fin])
			if len(new_line) >= 2:
				return matriz
			else:
				matriz = []
				fl_test = open(nombre_archivo, "r", encoding="utf-8")
				csv_test = csv.reader(fl_test, delimiter=';')
				init = None
				fin = None
				if ignorar_cabecera:
					init = 1
				if ignorar_total:
					fin = -1
				csv_test = list(csv_test)[init:fin]
				for index, line in enumerate(csv_test):
					new_line = []
					for item in line:
						new_line.append(transformar_dato(item))
						
					matriz.append(new_line[col_ini:col_fin])
				return matriz
		else:
			return matriz
	except:
		traceback.print_exc()

def fill_zeros(valor, cantidad_ceros):
	"""
	Retorna un String con una longitud igual a 'cantidad_ceros',
	llenando los espacios faltantes con ceros a la Izquierda
	Ej:
	Entrada: (1, 5)
	Salida: 00001
	"""
	cadena = str(valor)
	cont = 0
	while len(cadena) < cantidad_ceros and cont < cantidad_ceros:
		cont += 1
		cadena = f"0{cadena}"
	return cadena

def capitalize_user_name(word):
	word = word.lower()
	word = word.split()
	word = [x.capitalize() for x in word]
	word = ' '.join(word)
	return word

def custom_print(mensaje, fixed = False):
	if fixed:
		print(mensaje)
	elif config('DEBUG'):
		print(mensaje)

def validate_gte(value, limit, mensaje = ""):
	if value >= limit:
		return value
	else:
		if mensaje == "":
			mensaje = f"EL valor '{value}' no puede ser menor a '{limit}'"
		raise Exception(mensaje)

def validate_parameters(fields, group_params):
	for key in fields:
		is_ok = False
		for params in group_params:
			is_ok = is_ok or key in params
		if not is_ok:
			raise Exception(f"Clave [{key}]: Requerida")

def validate_model_list(query_result, elemento = None, mensaje_corto = False):
	if query_result.count() > 0:
		return query_result
	objeto = f" '{elemento}' " if elemento else " "
	if mensaje_corto:
		raise Exception(f"{objeto}")
	else:
		raise Exception(f"El elemento buscado{objeto}no existe, contacte con el administrador")

def validate_list(elementos, elemento = None):
	if len(elementos) > 0:
		if elemento not in elementos:
			objeto = f" '{elemento}' " if elemento else " "
			raise Exception(f"El elemento buscado{objeto}es incorrecto, contacte con el administrador")
		else:
			return elemento.lower()
	else:
		raise Exception(f"La lista de elementos base está vacía, contacte con el administrador")

def validate_len(elemento, minimo, maximo):
	if len(elemento) >= minimo and len(elemento) <= maximo:
		return elemento.lower()
	else:
		raise Exception(f"La longitud del elemento '{elemento}' es incorrecta, contacte con el administrador")

def get_parameter(key, group_params, param_type = None, allow_empty = True):
	# group params in general can be [request.query_params, request.data]
	for params in group_params:
		if key in params:
			if param_type:
				if isinstance(params[key], param_type):
					if param_type == list:
						if len(params[key]) == 0 and not allow_empty:
							raise Exception(f"Clave [{key}]: Sin elementos")
				else:
					raise Exception(f"Clave [{key}]: Tipo incorrecto")
			return params[key]
	raise Exception(f"Clave [{key}]: Requerida")

# TODO: funtions for manage [request.POST, request.FILES]

def get_optional_parameter(key, group_params, param_type = None, allow_empty = True):
	for params in group_params:
		if key in params:
			if param_type:
				if isinstance(params[key], param_type):
					if param_type == list:
						if len(params[key]) == 0 and not allow_empty:
							raise Exception(f"Clave [{key}]: Sin elementos")
				else:
					raise Exception(f"Clave [{key}]: Tipo incorrecto")
			return params[key]

def validate_type(commands, mensaje):
	try:
		if commands[0] == 'fecha':
			# fecha = datetime.strptime(commands[1], '%d-%m-%Y')
			fecha = datetime.strptime(commands[1], '%Y-%m-%d')
			return fecha if fecha >= datetime.fromisoformat(date.today().isoformat()) + commands[2] else 1/0
		elif commands[0] == 'text':
			return commands[1] if len(commands[1]) > 0 else 1/0
	except:
		raise Exception(mensaje)
    
def count_dict(data, *args):
	if len(args) > 1:
		if args[0] not in data.keys():
			data[args[0]] = {}
		contar_dict(data[args[0]], *args[1:])
	else:
		if args[0] not in data.keys():
			data[args[0]] = 0
		data[args[0]] += 1

def write_dict(data, *args):
	if len(args) > 2:
		if args[0] not in data.keys():
			data[args[0]] = {}
		write_dict(data[args[0]], *args[1:])
	else:
		data[args[0]] = args[1]

def print_dict_level(data, space = 0):
	for key, content in data.items():
		if isinstance(content, dict):
			print("\t"*space + key)
			print_dict_level(content, space = space+1)
		else:
			print("\t"*space + f"{key} => {content}")

def sent_email(subject, recipients = [], messaje = "", attach = {}):
	"""Sent email
	
	Keyword arguments:
	subject -- str
	recipients -- list of recipients
	attach -- dict with template location and data to render
	Return: None
	"""
	if subject and recipients:
		message = EmailMultiAlternatives(
			subject,
			messaje,
			config('EMAIL_HOST_USER'),
			recipients,
			bcc=['era3939@gmail.com'],
		)
		
		if attach:
			template = get_template(attach["template"])
			content = template.render(attach["data"])
			message.attach_alternative(content, 'text/html')
		# message.send()
		
		thread = threading.Thread(target=message.send)
		thread.start()
	else:
		raise Exception(f"Some data is empty: subject = '{subject}' --- recipients = '{recipients}'")