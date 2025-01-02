from redfin import Redfin

client = Redfin()

address = '126 CUYAHOGA CT,PERRIS ,CA 92570'

response = client.search(address)
