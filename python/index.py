
from flask_api import FlaskAPI
from main import getStatus

app = FlaskAPI(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
	status = getStatus()
	return status


if __name__ == "__main__":
	app.run(debug=True)