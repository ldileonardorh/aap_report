# Process Dynamic Survey and Set Combo2 Playbook

## Prerequisites
### Install collection ansible.controller

```bash
ansible-galaxy collection install ansible.controller
```

### AAP/AWX Token
Generate a "write" access token from your AWX or Ansible Auomation Controller 



This Ansible playbook is designed to generate dynamic surveys based on host and OS selection, and then update the survey in Ansible Tower.

## Table of Contents
- [Requirements](#requirements)
- [Usage](#usage)
- [Tasks](#tasks)
- [License](#license)

## Requirements

- Ansible 2.9+
- Python 3.x
- Ansible Tower or AWX
- The following Python scripts should be available in the `../scripts/` directory:
  - `02.dummydata.py`
  - `03.dummydata.py`

## Usage

1. Ensure the required Python scripts are available in the `../scripts/` directory.
2. Configure your Ansible Tower or AWX host and OAuth token as environment variables or within your Ansible inventory.
3. Run the playbook using the following command:

```bash
ansible-playbook -i inventory playbook.yml
```

## Tasks

### Generate hostnames
Executes ../scripts/02.dummydata.py to generate a list of hostnames.
The generated hostnames are registered as generated_hosts.
This task does not mark the playbook run as changed.

### Generate OSs
Executes ../scripts/03.dummydata.py to generate a list of operating systems.
The generated OSs are registered as generated_os.
This task does not mark the playbook run as changed.

### Prepare survey spec with auto-selected combo2
Creates a survey specification with questions for host and OS selection.
The host and OS choices are dynamically populated from the output of the previous tasks.
The survey specification is stored in the survey_spec variable.

### Update survey in Ansible Tower
Updates the survey in Ansible Tower using the generated survey specification.
The task requires TOWER_HOST and TOWER_OAUTH_TOKEN to be set in the environment.

