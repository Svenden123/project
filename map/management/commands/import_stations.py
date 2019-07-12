from django.core.management.base import BaseCommand

from map.models import Station, Route

import csv
import os
import django

django.setup()
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'


class Command(BaseCommand):
    help = 'Just another cool command'

    def handle(self, *args, **options):

        with open('moscow_bus_stations.csv', newline='') as csvfile:

            reader = csv.reader(csvfile, delimiter=';', quotechar='"')

            next(reader)
            for row in reader:

                station = Station()
                station.name = row[1]
                station.longitude = row[2]
                station.latitude = row[3]
                station.save()

                routes = str(row[7]).split('; ')

                for route_name in routes:

                    if not Route.objects.filter(name=route_name):

                        route = Route(name=route_name)
                        route.save()

                    route_id = Route.objects.get(name=route_name)
                    station.routes.add(route_id)

                station.save()
