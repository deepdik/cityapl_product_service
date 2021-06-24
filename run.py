import os
from app import app


if __name__ == '__main__':
    app.run(host=os.environ.get('FLASK_RUN_HOST', '0.0.0.0'),
    	port=int(os.environ.get('FLASK_RUN_PORT', '5000')))
