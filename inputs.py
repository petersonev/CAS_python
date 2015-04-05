import basic


def numNum(arg):
	new = ''
	while len(arg)!=0:
		end = 0
		for i in arg:
			if i not in '0123456789.':
				break
			end += 1

		if end != 0:
			new += 'Num('+arg[0:end]+')'
			arg = arg[end:]
		else:
			new += arg[0]
			arg = arg[1:]
	return (new+arg)