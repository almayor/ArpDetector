#!/usr/bin/env python

"""
Simple program to detect ARP attacks on local network.
Runs in the background using launchd.
"""

import os
import re

from collections import namedtuple

__author__ = 'almayor'
__license__ = 'MIT'
__version__ = '0.1.0'

ArpEntry = namedtuple('ArpEntry', 'ip interface')


def notify(arp, entry_list):
	"""Trigger OS X notification"""

	ip_list = [
		"{} ({})".format(entry.ip, entry.interface)
		for entry in entry_list
	]
	title = 'ARP Spoof Detector'
	message = "Attack from {} on\n".format(arp) + "\n".join(ip_list)
	os.system(
		"""
		osascript -e 'display notification "{}" with title "{}" sound name "Hero.aiff"'
		""".format(message, title)
	)


arp_raw = os.popen('arp -a').read()
arp_dict = dict()

arp_re = re.compile(
	r'\(((\d{1,3}\.?){4})\)\s+at\s+'
	r'(([a-f0-9]{1,2}:?){6})\s+on\s+'
	r'([^\n]*)$'
)

for line in arp_raw.split('\n'):
	match = arp_re.search(line)
	if match:
		arp = match.group(3)
		entry = ArpEntry(match.group(1), match.group(5))
		if arp not in arp_dict:
			arp_dict[arp] = list()
		arp_dict[arp].append(entry)

for arp, entry_list in arp_dict.items():
	if len(entry_list) > 1:
		notify(arp, entry_list)
