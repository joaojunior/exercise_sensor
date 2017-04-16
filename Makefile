test: clean
	tox

clean:
	find -regex '.*\.pyc' -exec rm {} \;
	find -regex '.*~' -exec rm {} \;
	rm -rf MANIFEST dist build *.egg-info
	rm -rf .tox
