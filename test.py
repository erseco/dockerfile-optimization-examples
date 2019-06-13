#!/usr/bin/env python

import sys
import whois

parameter = sys.argv[1]

domain = whois.query(parameter)

print(domain.__dict__)

print(domain.expiration_date)
