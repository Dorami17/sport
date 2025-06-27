from flask import Flask
from Blueprint import bp  # Import the blueprint
app = Flask(__name__)
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)