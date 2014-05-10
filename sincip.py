#!/usr/bin/python
import smtplib
import sys
import re
import os

# Mail configuration
#===================
mail_account = 'your email address'
mail_password = 'your email password'
mail_smtp_server = 'smtp.gmail.com'
mail_smtp_server_port = '587'
mail_to='mail to receive the data'

# system settings
#================
get_hostname=os.uname()[1]
step1=os.popen("curl http://bluesystems.com.br/apps/myip/?p=text > cache/info.tmp").read()
step2=os.popen("cat cache/info.tmp").read()

# receive parameters
#===================
get_to = mail_to 
get_subject = 'SINC IP Updater:: '+get_hostname
get_messages = 'xxx'

sys.stdout.write(""+get_messages+"")
re.escape(get_messages)

#from time import gmtime, strftime
#local_time=strftime("%Y-%m-%d %H:%M:%S", gmtime())
from datetime import datetime
local_time=str(datetime.now())

message = """From: SINC IP Updater <"""+mail_account+""">
To: <"""+get_to+"""to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: """+get_subject+"""
<h3>SINC IP UPDATER</h3>
<p>The easiest way to stay updated with the information from your dynamic ip address</p> 
<br/>
Hostname: """+get_hostname+ """<br/>
Current ip: """+step2+"""<br/>
Updated:  """+local_time+"""<br/><br/>
<hr/>
"""+get_messages+"""
SincIP Updater by <a href='http://www.twitter.com/jaccon'>@jaccon</a>

"""
server = smtplib.SMTP(mail_smtp_server, mail_smtp_server_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(mail_account,mail_password)
server.sendmail(mail_account,get_to,message)
server.rset()
server.quit()
