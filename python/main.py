
from datetime import datetime

def getStatus():
	now = str(datetime.now())
	ret = { 'status' : 'ok', 'time' : now }
	return ret


def main():
	status = getStatus()
	print(status)


if __name__ == "__main__":
	main()