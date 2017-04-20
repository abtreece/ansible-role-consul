consul-cluster
==============
This Ansible role will configure a server or servers to run consul

Requirements
------------
Requires and installs zip because why would we want to create packages for the standard OS'es.

Role Variables
--------------
The setable variables for this role are configured in defaults/main.yml. The following vars are important modifiers for this role.

-   *node_role*: Should be set to server or bootstrap. The bootstrap role should only be used on one node in the cluster.
-   *consul_version*: The version of consul to be installed. default is “0.7.5"
-   *consul_iface*: The interface consul should use for communication. default
    is "eth1"
-   ...
 

Dependencies
------------
None
 

Example Playbook
----------------
A simple example of this playbook.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- hosts: all
  roles:
    - role: consul-cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
