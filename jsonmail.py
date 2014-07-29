#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mandrill Markdown Mails
# Author: Frédérique Mittelstaedt 2014
# License: MIT
# Requires the python modules pypandoc (and installed Pandoc) and mandrill

# This example also requires the modules sys and json

import sys
import json
from mandrillmarkdownmails import sendMandrillMarkdownMail

# Script for sending an email on Mandrill with the template and a JSON containing the information provided as a command line parameters
# First parameter: template
# Second parameter: JSON with mail information

if (len(sys.argv) != 3):
  print "Two variables need to be passed on to this script."
  raise

template = sys.argv[1]
dict = json.loads(sys.argv[2])

sendMandrillMarkdownMail(template, dict)
