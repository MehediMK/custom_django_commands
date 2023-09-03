from django.core.management import BaseCommand
from scripts.services.service import Service

class Command(BaseCommand):
    help = "Insert api data into db"
    service = Service()
    def add_arguments(self, parser):
        parser.add_argument('--type', nargs='+', type=str, required=False, help="Enter insert type")
        parser.add_argument('--username', type=str, required=True, help='Username of the user')

    def handle(self, *args, **options):
        api_type = options.get('type')
        username = options.get('username')
        self.service.insert_data_from_api(username, api_type)
