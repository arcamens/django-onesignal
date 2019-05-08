#! /usr/bin/env python3

from distutils.core import setup

setup(name="django-onesignal",
      version="2.0.0",
      description="Django app for integrating with onesignal.",
      packages=["onesignal", 'onesignal.templates', 
      'onesignal.templates.onesignal', 'onesignal.static', 'onesignal.static.onesignal'],

      package_data={'onesignal.templates.onesignal': ['init_onesignal.html'],
      'onesignal.static.onesignal':['OneSignalSDKUpdaterWorker.js', 
      'manifest.json', 'OneSignalSDKWorker.js']},

      author="Iury O. G. Figueiredo",
      author_email="ioliveira@id.uff.br",
      url='',
      download_url='',
      keywords=[],
      classifiers=[])

































































