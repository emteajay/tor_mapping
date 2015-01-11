#!/usr/bin/env python

import requests
import re
import json

relays = {'relays' : []}

# We pick a random directory authority, and pull down the consensus
consensus = requests.get('http://82.94.251.203/tor/status-vote/current/consensus').text

# Then, we parse out the IP address, nickname, and flags using a regular expression
regex = re.compile('''^r\s(.*?)\s(?:.*?\s){4}(.*?)\s.*?\ns\s(.*?)\n''', re.MULTILINE)

# Find all the matches in the consenses
# matches = regex.finditer(consensus)
for record in regex.finditer(consensus):
  # For each record, create a dictionary object for the relay
	relay = {
	'nickname' : record.group(1),
	'ip' : record.group(2),
	'type' : 'exit' if 'Exit' in record.group(3) else 'normal'
	}
	# And append it to the master list
	relays['relays'].append(relay)
open('tor_relays.txt','w').write(json.dumps(relays, indent=4))