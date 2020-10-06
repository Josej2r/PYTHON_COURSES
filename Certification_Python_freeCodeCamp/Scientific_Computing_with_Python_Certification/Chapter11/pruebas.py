import re
linea = "New Revision: 39772"
regExp = "^New Revision: ([0-9]+)"
x = re.findall(regExp, linea)
y = float(x[0])

print(x)
