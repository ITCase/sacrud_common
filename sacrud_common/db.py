#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
Common tools for fixtures
"""
import json
import os
from random import randint

import transaction

from sacrud.action import CRUD


class Fixture(object):

    def __init__(self, DBSession, path=None):
        self.DBSession = DBSession
        self.path = path

    def add(self, model, fixtures, delete=True):
        """
        Add fixtures to database.

        Example::

        fixture = Fixture(DBSession)
        hashes = ({'foo': "{'foo': 'bar', '1': '2'}}", {'foo': "{'test': 'data'}"})
        fixture.add(TestHSTORE, hashes)
        """
        if delete:
            model.__table__.create(checkfirst=True,
                                   bind=self.DBSession.bind.engine)
            self.DBSession.query(model).delete()
            transaction.commit()
        if isinstance(fixtures, str):
            path = os.path.join(self.path, fixtures)
            json_data = open(path).read()
            fixtures = json.loads(json_data)

        for fixture in fixtures:
            if isinstance(fixture, dict):
                CRUD(self.DBSession, model, request=fixture).add()

    def rand_id(self, model):
        qty = len(self.DBSession.query(model).all())
        return randint(1, qty)


def add_extension(engine, *args):
    """
    Add extension to PostgreSQL database.
    """
    conn = engine.connect()
    is_superuser = conn.scalar('''SELECT * FROM pg_user
                               WHERE usename=CURRENT_USER
                               AND usesuper=True;''')
    if not is_superuser:
        conn.close()
        return False

    for ext in args:
        conn.execute('CREATE EXTENSION IF NOT EXISTS "%s"' % ext)
    conn.execute('COMMIT')
    conn.close()
    return True


def add_triggers(engine, SQL_path, *args):
    """
    Add triggers from files
    """
    conn = engine.connect()
    for trigger in args:
        path_to_trigger = os.path.join(SQL_path, trigger)
        # only nobomb files
        conn.execute(open(path_to_trigger, 'r').read().decode('utf-8'))
    conn.execute('COMMIT')
    conn.close()
