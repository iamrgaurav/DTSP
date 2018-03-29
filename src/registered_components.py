from src.app import app
from src.models.retailers.views import retailers_blueprint
app.register_blueprint(retailers_blueprint, url_prefix='/retailers')
