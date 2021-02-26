# Ansible examples

Examples demonstrating Ansible features. Each example aims to be as simple as possible to showcase one aspect of Ansible.
Most of them do not require external hosts, simply can be verified using the local file system or memory.
Where some kind of host is necessary, the example uses Molecule to spin up a Docker container.

## Features

- [Handlers](handlers_example)
- [Tags](tags_example)
- [Templates](templates_example)
- [Roles - structure](roles_structure_example)
- [Roles - import](roles_import_example)
- [Modules](modules_example)
- [Inventory - single file config](inventory_single_file_configuration_example)
- [Inventory - standard config](inventory_standard_configuration_example)
- [Molecule - Ansible verification](molecule_ansible_verification_example)
- [Molecule - Testinfra](molecule_testinfra_example)