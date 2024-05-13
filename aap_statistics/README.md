# Ansible Playbook for Gathering Job and Template Data from API and Writing to CSV

This Ansible playbook fetches job and template data from specified APIs, processes the data, and writes it to CSV files. It then transfers these files to remote hosts via SSH.

## Prerequisites

- Ansible installed on the control node.
- APIs accessible from the control node.
- Necessary credentials (bearer token) for API access.
- Remote hosts accessible via SSH with the necessary credentials.

## Variables

- `base_url`: Base URL of the API.
- `bearer_token`: Bearer token for API authorization.
- `job_api_url`: Endpoint URL for fetching job data.
- `template_api_url`: Endpoint URL for fetching template data.
- `base_output_folder`: Base folder for output files.
- `timestamp`: Timestamp for uniquely identifying the output folder.
- `job_template_output_file`: Filename for the job data CSV file.
- `unified_template_output_file`: Filename for the template data CSV file.
- `output_folder`: Full path for the output folder.
- `separator`: Separator used in CSV files.
- `job_csv_headers`: List of headers for the job data CSV file.
- `template_csv_headers`: List of headers for the template data CSV file.
- `remote_path`: Path on the remote host to copy the files to.
- `remote_host`: The remote host to copy the files to.
- `remote_user`: SSH username for the remote host.
- `remote_password`: SSH password for the remote host.
- `become_password`: Password for privilege escalation on the remote host.

## Playbook Overview

### Play: Gather job data and template data from API and write to CSV

#### Hosts

- `localhost`: This play runs on the control node itself.

#### Vars

- Sets up the necessary variables for API access, output file paths, and CSV headers.

#### Tasks

1. **Set output folder fact**: Initializes the output folder and file paths.
2. **Ensure output directory exists**: Creates the output directory if it doesn't exist.
3. **Initialize job CSV file with headers**: Writes headers to the job data CSV file.
4. **Initialize template CSV file with headers**: Writes headers to the template data CSV file.
5. **Fetch job data and write to CSV**: 
    - Fetches job data from the API.
    - Parses the JSON response.
    - Writes the job data to the CSV file.
    - Handles pagination to ensure all job data is retrieved.
6. **Fetch template data and write to CSV**: 
    - Fetches template data from the API.
    - Parses the JSON response.
    - Writes the template data to the CSV file.
    - Handles pagination to ensure all template data is retrieved.
7. **Display success message**: Outputs a success message with the paths of the generated CSV files.
8. **Copy job data CSV file over SSH**: Transfers the job data CSV file to the remote host.
9. **Copy template data CSV file over SSH**: Transfers the template data CSV file to the remote host.

## Usage

1. Clone this repository to your Ansible control node.
2. Update the playbook variables as needed, especially the API URLs, bearer token, and remote host credentials.
3. Run the playbook with the following command:
   ```sh
   ansible-playbook gather_and_write_data.yml



