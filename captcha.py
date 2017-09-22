print('Captcha')

from random import randint as r
from random import choice as c
import string

captcha = []
r1 = r(6, 10)

i = 0
while i <= r1:
	r2 = r(0, 9)
	if r2 <= 6:
		r3 = str(r(0, 9))
	else:
		r3 = c(string.ascii_letters)
	captcha.append(r3)
	i += 1

captcha = ''.join(captcha)
print('Captcha generated: ' + captcha)

