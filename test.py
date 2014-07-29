#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mandrill Markdown Mails
# Author: Frédérique Mittelstaedt 2014
# License: MIT
# Requires the python modules BeautifulSoup, markdown and mandrill

from markdownmandrillmails import sendMarkdownMandrillMail

# Example
# John Doe <john.doe@invalid.com> sends a mail using his Mandrill template "mandrill-template" to Jane Doe<jane.doe@invalid.com>.
# The html template is expected to contain the placeholder *|message_html|*, the text template is expected to contain the placeholder *|message_txt|*.

dict = {
	"sender": {
		"email": 'john.doe@invalid.com',
		"name": 'John Doe'
	},
	"recipients": [
		{
			"name": 'Jane Doe',
			"email": 'jane.doe@invalid.com',
			"type": 'to'
		}
	],
	"subject": 'The subject',
	"variables": {
		"message": "The message content in *Markdown*!"
	}
}

sendMarkdownMandrillMail("mandrill-template", dict)
