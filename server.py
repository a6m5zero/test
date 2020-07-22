# Popitka napisat bottle server
from bottle import route, run, view
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies

@route("/")
@view("horoscope")
def index():
	now = dt.now()
	x = random()
	predictions = generate_prophecies()
	return {"date": f"{now.year}-{now.month}-{now.day}",
			"predictions":predictions,
			"special_date": x > 0.5,
			"x": x,}


@route("/api/test")
def api_test():
	return {"test_passed": True}

@route("/api/return_predictions")
def api_return_predictions():
	return {"predictions":generate_prophecies()}

@route("/static/<filename>")
def send_static_file(filename):
	return static_file(filename)


run(
	host = "localhost", 
	port=8080, 
	debug = True
	)