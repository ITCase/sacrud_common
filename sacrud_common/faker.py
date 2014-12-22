#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
Fake data for fixtures
"""
import os
import csv
import decimal
import random
from datetime import date

here = os.path.dirname(os.path.realpath(__file__))


def get_random_decimal():
    return decimal.Decimal(random.randrange(10000)) / 100


def get_ru_sex(middlename):
    if not middlename or middlename[-2:-1] != '\xb0':
        return True
    return False


def get_random_day(day=1, month=1, year=1920):
    start_date = date.today().replace(day=day,
                                      month=month,
                                      year=year).toordinal()
    end_date = date.today().toordinal()
    return date.fromordinal(random.randint(start_date, end_date))


class FakeAddress():

    def __init__(self,
                 city=os.path.join(here, 'fixtures/ru/city.csv'),
                 country=os.path.join(here, 'fixtures/ru/country.csv'),
                 region=os.path.join(here, 'fixtures/ru/region.csv')):
        self.country = country
        self.region = region
        self.city = [x for x in csv.DictReader(open(city),
                                               delimiter=';')]

    def get_row_csv(self, file_name, key, value):
        with open(file_name) as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                if row[key] == value:
                    return row

    def get_country(self, row):
        country = self.get_row_csv(self.country, 'country_id',
                                   row['country_id'])
        return country['name']

    def get_region(self, row):
        return self.get_row_csv(self.region, 'region_id',
                                row['region_id'])['name']

    def get_random_address(self):
        row = random.choice(self.city)
        city = row['name']
        region = self.get_region(row)
        country = self.get_country(row)
        return ', '.join((city, region, country))
