#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mandrill Markdown Mails
# Author: Frédérique Mittelstaedt 2014
# License: MIT
# Requires the python modules BeautifulSoup, markdown and mandrill

from BeautifulSoup import BeautifulSoup
import markdown
import mandrill

# Paste your Mandrill API key here
API_KEY = 'f7pVy_5pVHFabHFgdyj9Dw'

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

# Send mail providing the 
# Note: Convention for variables: VARIABLENAME_html and VARIABLENAME_txt for html and txt mails respectively - adapt to your needs
def sendMandrillMarkdownMail(template, dict):
	variables = {}
	for (k, v) in dict["variables"].iteritems():
		variables[k+"_html"] = markdown.markdown(v);
		variables[k+"_txt"] = ''.join(BeautifulSoup(variables[k+"_html"]).findAll(text=True))

	sendMandrillMail(template, dict["sender"], dict["recipients"], dict["subject"], variables)
