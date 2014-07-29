#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mandrill Markdown Mails
# Author: Frédérique Mittelstaedt 2014
# License: MIT
# Requires the python modules pypandoc (and installed pandoc) and mandrill

import mandrill
import pypandoc

# Paste your Mandrill API key here
API_KEY = ''

# Sending mails via Mandrill
# Note: Currently sends a mail to the sender in BCC - adapt to your needs
def sendMandrillMail(template_name, sender, recipients, subject, variables):
	mandrill_client = mandrill.Mandrill(API_KEY)
	message = {
		'from_email': sender["email"],
		'from_name': sender["name"],
		'to': [],
		'subject': subject,
		'global_merge_vars': []
	}
	for r in recipients:
		message['to'].append(r)

	message['to'].append({
		"email": sender["email"],
		"name": "Blind carbon copy of sent mail",
		"type": "bcc"
	})
	 
	for k, v in variables.iteritems():
		message['global_merge_vars'].append(
			{ 'name': k, 'content': v }
		)
	mandrill_client.messages.send_template(template_name, [], message, async=True)

# Send mail providing the template and dict with information
# Note: Convention for variables: VARIABLENAME_html and VARIABLENAME_txt for html and txt mails respectively - adapt to your needs
def sendMandrillMarkdownMail(template, dict):
	variables = {}
	for (k, v) in dict["variables"].iteritems():
		variables[k+"_html"] = pypandoc.convert(v, "html", format='md')
		variables[k+"_txt"] = pypandoc.convert(v, "plain", format='md')

	sendMandrillMail(template, dict["sender"], dict["recipients"], dict["subject"], variables)
