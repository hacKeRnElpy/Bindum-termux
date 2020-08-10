import os
os.system("clear")
while True:
	print('[1]Create bind')
	choose=input('\n  [bindum] >> ')
	if (choose=='1'):
		bind=input('Input bind: ')
		bindcommand=input('Input bind command: ')
		postrov="'"
		bid='alias ' + bind +'=' + postrov + bindcommand + postrov
		binds=open('/data/data/com.termux/files/usr/etc/binds.txt', 'a')
		binds.write('\n' + bid)
		binds.close
		f=open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'a')
		f.write('\n' + bid)
		f.close
		os.system("clear")