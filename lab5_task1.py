import pprint
keys = ["bin","dec","oct","hex" ]
main=[{"bin":bin(i),"dec":(i),"oct":oct(i),"hex":hex(i),} for i in range(16)]
pprint.pprint (main)
# TODO решить с помощью list comprehension и распечатать его
