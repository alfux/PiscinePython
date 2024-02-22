import sys as sys

try:
	if (len(sys.argv) > 2):
		raise AssertionError("more than one argument is provided")
	elif (len(sys.argv) == 2):
		try:
			var: float = float(sys.argv[1])
			if (var % 1):
				raise ValueError()
			if (var % 2):
				print("I'm Odd.")
			else:
				print("I'm Even.")
		except ValueError:
			raise AssertionError("argument is not an integer")
		except BaseException:
			pass
except BaseException as err:
	print(err.__class__.__name__ + ':', err)
