#!/usr/bin/env python
# encoding: utf-8
# 
# Find members of Plone's directory who aren't in any group

import ldap, sys

def main(argv):
    if len(argv) > 1:
        print >>sys.stderr, 'This program takes no arguments, sorry.'
        return False
    con = None
    try:
        con = ldap.initialize('ldap://localhost:9389')
        # First find all the groups, taking note of every member
        members = set()
        results = con.search_s('ou=Groups,dc=plone,dc=org', ldap.SCOPE_ONELEVEL, filterstr='(objectClass=groupOfUniqueNames)',
            attrlist=['uniqueMember'])
        for group in results:
            members.update(group[1]['uniqueMember'])
        
        # Now go through every user.  If that person is in our members set, no problem. If not,
        # well, let's just say he or she may be in for a surprise.
        results = con.search_s('ou=People,dc=plone,dc=org', ldap.SCOPE_ONELEVEL, filterstr='(objectClass=pilotPerson)',
            attrlist=['dn'])
        for member in results:
            dn = member[0]
            if dn not in members:
                print dn
        return True
    except:
        con.close()
        return False
        

if __name__ == '__main__':
    sys.exit(0 if main(sys.argv) else -1)