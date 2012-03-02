************************
 LDAP Analysis Buildout
************************

This buildout creates a simple OpenLDAP_ server that loads the Plone_ LDAP
data and lets you perform queries to analyze the kinds of users and groups
that the Plone project has.


Installation
============

Edit buildout.cfg and adjust the paths to the various files in the [paths]
section.  If necessary, edit the port number in the [ports] section too.

Then::

    python bootstrap.py -d
    bin/buildout

This will set up OpenLDAP configuration files, load the database with the
Plone export, and configure a process Supervisor_ to manage the server, as
well as create a wrapper ``bin/ldapsearch`` command for use with it.


Starting the Server
===================

To start the LDAP server, just start the Supervisor::

    bin/supervisord

You can then use ``bin/supervisorctl`` to check on it, restart it etc.


Querying the Server
===================

To simplify command-lines, the buildout generated a wrapper script that you
can use to query the server.  Here are some example queries:

``bin/ldapsearch '(uid=jonstahl)'``
    Look up Jon Stahl's entry.
``bin/ldapsearch '(uid=nutjob)' mail``
    Get nutjob's email address.
``bin/ldapsearch '(objectClass=groupOfUniqueNames)'``
    Show all the groups and their members.


Future Work
===========

How about:

* Adding a Python interpreter with the python-ldap egg baked in.
* Add some sample Python scripts to query for all users outside of groups.
* Check this into Github—nevermind, DONE!


.. References:
.. _OpenLDAP: http://www.openldap.org/
.. _Plone: http://plone.org/
.. _Supervisor: http://supervisord.org/
