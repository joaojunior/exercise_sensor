test: clean
	tox

quality:
	flake8
	isort -c -rc sensor_parser/ tests/

clean:
	find -regex '.*\.pyc' -exec rm {} \;
	find -regex '.*~' -exec rm {} \;
	rm -rf MANIFEST dist build *.egg-info
	rm -rf .tox

requirements:
	pip install -r requirements.txt

run: clean requirements
	gunicorn api_energy_sensor.wsgi --chdir api_energy_sensor/
