# Ansible examples

Examples demonstrating the main building blocks of Ansible, like roles, handlers, inventories, etc. 
Each subfolder under the root aims to showcase one such building block in a form of actions and verification.
The verifications are done by assertions at the end of the playbooks or by Molecule tests.

Most of the examples do not require external hosts and their target feature simply can be demonstrated using the local file system or memory.
Where some kind of host is necessary, Molecule is used to spin up Docker containers.

## Local requirements: Ansible and Docker installed

## Main building blocks

- [Handlers](handlers_example)
- [Tags](tags_example)
- [Templates](templates_example)
- [Roles - structure](roles_structure_example)
- [Roles - import](roles_import_example)
- [Modules](modules_example)
- [Inventory - single file config](inventory_single_file_configuration_example)
- [Inventory - standard config](inventory_standard_configuration_example)
- [Molecule - Ansible verification](molecule_ansible_verification_example)
- [Molecule - Testinfra verification](molecule_testinfra_example)