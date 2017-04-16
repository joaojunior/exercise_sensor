test: clean
	tox

quality:
	isort -c -rc sensor_parser/ tests/

clean:
	find -regex '.*\.pyc' -exec rm {} \;
	find -regex '.*~' -exec rm {} \;
	rm -rf MANIFEST dist build *.egg-info
	rm -rf .tox
