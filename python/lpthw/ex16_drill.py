from sys import argv

script, filename = argv

test = open(filename)

print "Opening the file created in ex16.py..."
print test.read()
