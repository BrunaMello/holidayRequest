import csv
from datetime import datetime

from django.core.management.base import BaseCommand

from department.models import Department, Position
from employee.models import Employees


class Command(BaseCommand):

	def add_arguments(self, parser):
		parser.add_argument(
			'file_name',
			type=str,
			help='CSV name to import employees from.'
		)

	def handle(self, *args, **options):
		file_name = options['file_name']

		with open(file_name, 'r', encoding='utf-8') as file:
			reader = csv.DictReader(file)
			for row in reader:
				name = row['name']
				email = row['email'] if row['email'] else None
				department_name = row['department']
				department, created = Department.objects.get_or_create(name=department_name)

				position_name = row['position']
				position, created = Position.objects.get_or_create(name=position_name, department=department)

				city = 'Cork' if row['city'] == 'Cork' else 'Dublin'
				employment_type = 'Full-Time' if row['employment_type'] == 'Full-Time' else 'Part-Time'
				hire_date = datetime.strptime(row['hire_date'], '%d/%m/%Y').date()
				fire_date = datetime.strptime(row['fire_date'], '%d/%m/%Y').date() if row['fire_date'] else None
				is_active = True if row['is_active'] == 'TRUE' else False

				self.stdout.write(self.style.NOTICE(name))

				Employees.objects.create(
					name=name,
					email=email,
					department=department,
					position=position,
					city=city,
					employment_type=employment_type,
					hire_date=hire_date,
					fire_date=fire_date,
					is_active=is_active
				)

		self.stdout.write(self.style.SUCCESS('Employees imported successfully.'))
