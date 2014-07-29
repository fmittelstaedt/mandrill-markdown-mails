mandrill-markdown-mails
=======================

A python script for sending mails using Mandrill with parameters being specified as Markdown and automatic application of inline styles.

**In order to use the script, the Mandrill API key in markdownmandrillmails.py has to be set.**

Call `sendMarkdownMandrillMail(template, dict)` to send a mail using the template name provided in the first parameter and the information provided in the second parameter `dict`.

The `dict` needs to have a `sender` entry with an `email` and a `name`,  a list of `recipients`, each with a `name`, `email` and `type` (`to`, `cc` or `bcc`), a `subject` and a dict with `variables`, whose content is Markdown. For each passed `variable`, the Mandrill template should contain `variable_html` and/or `variable_txt` as needed.

License: MIT
