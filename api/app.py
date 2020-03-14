import hug

from api.config import db, config
from api.resources.forum import views as forum_views


app = hug.API(__name__)

# init DB
db.init_app(app, config.SQLALCHEMY_DATABASE_URI)

app.extend(forum_views, '/forum')
