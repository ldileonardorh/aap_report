# README.md

## Overview

This Ansible playbook gathers job and template data from specified APIs, writes the data to CSV files, and then transfers these files to a remote host. The playbook is designed to fetch data for the last 30 days by default and allows customization through variables.

## Prerequisites

- Ansible installed on the control node
- API access with a bearer token
- SSH access to the remote host

## Variables

### Required Variables

- `bearer_token`: Authorization token for API access
- `base_output_folder`: Base directory for output files
- `base_url`: Base URL for the API
- `job_api_url`: Endpoint for job data API
- `template_api_url`: Endpoint for template data API
- `job_template_output_file`: Filename for job data CSV
- `unified_template_output_file`: Filename for template data CSV
- `remote_path`: Base directory on the remote host
- `remote_host`: Remote host address
- `remote_user`: SSH user for the remote host
- `remote_password`: SSH password for the remote host
- `become_password`: Password for privilege escalation on the remote host

### Optional Variables

- `start_date`: Start date for job data filtering (default is 30 days ago)
- `separator`: CSV column separator (default is `|`)

## Playbook Structure

### Vars

- `headers`: Contains the authorization token
- `timestamp`: Timestamp for unique output folder naming
- `output_folder`: Combined base folder and timestamp
- `job_csv_headers`: Headers for the job data CSV
- `template_csv_headers`: Headers for the template data CSV

### Tasks

1. **Get the date 30 days ago:** Fetches the date 30 days prior to the current date.
2. **Set date_30_days_ago fact:** Stores the fetched date in a variable.
3. **Ensure my_variable is set:** Sets the job date filter.
4. **Print result:** Prints the start date for job data filtering.
5. **Set output folder fact:** Sets the output folder and file paths.
6. **Ensure output directory exists:** Creates the output directory if it doesn't exist.
7. **Initialize job CSV file with headers:** Writes the headers to the job CSV file.
8. **Initialize template CSV file with headers:** Writes the headers to the template CSV file.
9. **Fetch job data and write to CSV:** Fetches job data from the API and writes it to the CSV file.
10. **Fetch template data and write to CSV:** Fetches template data from the API and writes it to the CSV file.
11. **Display success message:** Prints a success message with file paths.
12. **Create remote directory:** Creates a directory on the remote host.
13. **Copy job data to remote host:** Copies the job CSV file to the remote host.
14. **Copy template data to remote host:** Copies the template CSV file to the remote host.

## Usage

1. Clone the repository or copy the playbook to your Ansible control node.
2. Set the required variables in a `vars` file or directly in the playbook.
3. Run the playbook using the following command:
    ```bash
    ansible-playbook -i localhost playbook.yml
    ```

## Example Variables File (vars.yml)

```yaml
bearer_token: "your_bearer_token_here"
base_output_folder: "/path/to/output"
base_url: "https://api.example.com"
job_api_url: "/api/v1/jobs"
template_api_url: "/api/v1/templates"
job_template_output_file: "job_data.csv"
unified_template_output_file: "template_data.csv"
remote_path: "/remote/path/to/output"
remote_host: "remote.example.com"
remote_user: "your_remote_user"
remote_password: "your_remote_password"
become_password: "your_become_password"
start_date: "2023-01-01T00:00:00"  # Optional
separator: ","  # Optional

