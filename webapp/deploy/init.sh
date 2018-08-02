#!/bin/bash
ansible-playbook -vvv ./init_config.yml --private-key=/home/wynkel/do_deploy -u root -i ./hosts


