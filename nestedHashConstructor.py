def explodeReport(inputArray):
	retDict = {}
	if (len(inputArray) < 1):
		return retDict
	for line in inputArray:
		infoArr = line.split('|')
		dataDict = retDict
		for i in range(0, len(infoArr)-2):
			data = infoArr[i]
			if (dataDict.get(data) == None):
				dataDict[data] = {}
			dataDict = dataDict[data]
		dataDict[infoArr[len(infoArr)-2]] = infoArr[len(infoArr)-1]
	return retDict


if __name__ == '__main__':
	# Test Cases
	emptyList = []
	outputDict = {}
	print ('Input:', emptyList)
	print ('Expected Output:', outputDict)
	print ('Actual Output:', explodeReport(emptyList))

	server1 = ['app1|server1|uptime|5']
	outputDict = {'app1': {'server1': {'uptime': '5'}}}
	print ('Input:', server1)
	print ('Expected Output:', outputDict)
	print ('Actual Output:', explodeReport(server1))

	server1A = ['app1|server1|uptime|5', 'app1|server1|loadavg|0.01 0.02 0.03']
	outputDict = {'app1': {'server1': {'uptime': '5', 'loadavg': '0.01 0.02 0.03'}}}
	print ('Input:', server1A)
	print ('Expected Output:', outputDict)
	print ('Actual Output:', explodeReport(server1A))

	server1B = ['app1|server1|uptime|5','app1|server1|loadavg|0.01 0.02 0.03','app1|server1|conn1|state|up']
	outputDict = {'app1': {'server1': {'uptime': '5', 'loadavg': '0.01 0.02 0.03', 'conn1': {'state': 'up'}}}}
	print ('Input:', server1B)
	print ('Expected Output:', outputDict)
	print ('Actual Output:', explodeReport(server1B))

	server2 = ['app1|server1|uptime|5','app1|server1|loadavg|0.01 0.02 0.03','app1|server1|conn1|state|up', 'app1|server2|uptime|10', 'app1|server2|loadavg|0.11 0.22 0.33', 'app1|server2|conn1|state|down']
	outputDict = {'app1': {'server1': {'uptime': '5', 'loadavg': '0.01 0.02 0.03', 'conn1': {'state': 'up'}}, 'server2': {'uptime': '10', 'loadavg': '0.11 0.22 0.33', 'conn1': {'state': 'down'}}}}
	print ('Input:', server2)
	print ('Expected Output:', outputDict)
	print ('Actual Output:', explodeReport(server2))

	serverRun = server2
	serverRun.append('app1|running|true')
	outputDict = {'app1': {'server1': {'uptime': '5', 'loadavg': '0.01 0.02 0.03', 'conn1': {'state': 'up'}}, 'server2': {'uptime': '10', 'loadavg': '0.11 0.22 0.33', 'conn1': {'state': 'down'}}, 'running': 'true'}}
	print ('Input:', serverRun)
	print ('Expected Output:', outputDict)
	print ('Actual Output:', explodeReport(serverRun))

	serverApp2 = serverRun
	serverApp2.append('app2|running|true')
	outputDict = {'app1': {'server1': {'uptime': '5', 'loadavg': '0.01 0.02 0.03', 'conn1': {'state': 'up'}}, 'server2': {'uptime': '10', 'loadavg': '0.11 0.22 0.33', 'conn1': {'state': 'down'}}, 'running': 'true'}, 'app2': {'running': 'true'}}
	print ('Input:', serverApp2)
	print ('Expected Output:', outputDict)
	print ('Actual Output:', explodeReport(serverApp2))
