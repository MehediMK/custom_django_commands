import datetime
import logging
from django.core.management import BaseCommand
from scripts.services.service import Service
from scripts.utils import Util


class Command(BaseCommand):
    help = "Insert api data into db"
    service = Service()
    def add_arguments(self, parser):
        parser.add_argument('--type', nargs='+', type=str, required=False, help="Enter insert type")
        parser.add_argument('--username', type=str, required=True, help='Username of the user')

    def handle(self, *args, **options):
        start_time = datetime.datetime.now()
        username = options.get('username')
        self.service.insert_data_from_api(username)
        execution_time = Util.get_execution_time(start_time)
        logging.info(f'Script takes {execution_time} minutes.')