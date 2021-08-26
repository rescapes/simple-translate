#!/usr/bin/env python
import sys
from os import environ
# This is a sample Python script.
from google.oauth2 import service_account
# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from google.cloud import translate_v2 as translate

credentials = service_account.Credentials.from_service_account_file(environ['GOOGLE_APPLICATION_CREDENTIALS'])
client = translate.Client()
language = sys.argv[1]
original = sys.argv[2]
print(client.translate(original, source_language=language))
