import os

import unittest
from sqlalchemy_utils import database_exists, create_database, drop_database

from alembic import command
from alembic.config import Config

from api.config import db, config
from api.app import app
from api.models import User

TESTDB_URI = config.TEST_SQLALCHEMY_DATABASE_URI
MIGRATIONS = os.path.join(config.PROJECT_ROOT, 'migrations')

class APITest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not database_exists(TESTDB_URI):
            create_database(TESTDB_URI)

        alembic_cfg = Config(os.path.join(config.PROJECT_ROOT, 'alembic.ini'))
        alembic_cfg.set_main_option('script_location', MIGRATIONS)
        alembic_cfg.set_main_option('sqlalchemy.url', TESTDB_URI)

        command.upgrade(alembic_cfg, 'head')
        db.init_app(app, TESTDB_URI)

    @classmethod
    def tearDownClass(cls):
        drop_database(TESTDB_URI)

class ForumAPITest(APITest):

    @classmethod
    def setUpClass(cls):
        super(ForumAPITest, cls).setUpClass()
        db.connect()
        db.session.begin()
        cls.user = User(email='testuser@email.com', name='Test User')
        db.session.add(cls.user)
        db.session.commit()
        cls.user_id = cls.user.id
        cls.user_email = cls.user.email
        db.close()
