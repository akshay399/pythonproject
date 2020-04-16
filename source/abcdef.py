

import smtplib

def mailSender(mail_id,body,subject):
	# print(body)
	# print(subject)
	# print(mail_id)
	msg=f'Subject: {subject}\n\n{body}'
	conn = smtplib.SMTP('smtp.gmail.com',587)
	# print(conn.ehlo())
	conn.starttls()
	conn.login('quickbook6969@gmail.com', 'quickbook@123')

	conn.sendmail('quickbook6969@gmail.com',mail_id,msg)
	conn.quit()

if __name__ == '__main__':
	print('running main')
	print('running main.')
	print('running main..')
	print('end')


