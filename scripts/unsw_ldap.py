#!/usr/bin/python3

import ldap3, os, sys

def authenticate(zid, zpass, bind_password=None, debug=False):
	server_uri = 'ldaps://ad.unsw.edu.au'
	bind_dn = 'svcCSEMaestro@ad.unsw.edu.au'
	base_dn = 'ou=IDM_People,ou=IDM,dc=ad,dc=unsw,dc=edu,dc=au'
	search_filter = '(sAMAccountName=%s)' % zid
	attributes = ["displayName", "mail"]
	try:
		if not bind_password:
			with open(os.path.join(os.environ.get('HOME', '.'), '.unsw_ldap_password')) as f:
				bind_password = f.read().strip()
		server = ldap3.Server(server_uri)
		connection = ldap3.Connection(server, user=bind_dn, password=bind_password, auto_bind=True)
		connection.search(base_dn, search_filter, attributes=attributes)
		if len(connection.response) != 1:
			if debug:
				print('Authentication failed, search returned', len(connection.response), 'matches:', connection.response, file=sys.stderr)
			return False
		c = ldap3.Connection(server, user=connection.response[0]['dn'], password=zpass)
		if c.bind():
			authenticated = True
			c.unbind()
		else:
			authenticated = False
		connection.unbind()
		return authenticated
	except (ldap3.LDAPException,OSError) as e:
		if debug:
			print('Authentication failed due to exception:', str(e), file=sys.stderr)
		return False
			
if __name__ == "__main__":
	zid = input()
	zpass= input()
	if authenticate(zid, zpass):
		print("Authenticated")
	else:
		print("Authentication failed")
