import requests
import csv
from datetime import datetime

RED = '\033[31m'  # Red text
GREEN = '\033[32m'  # Green text
YELLOW = '\033[33m'  # Yellow text
RESET = '\033[0m'  # Reset the color

                                                                                                            
# Setup
base_url = ''
headers = 

now = datetime.now()
timestamp = now.strftime("%Y%m%d%H%M%S")
#Template Configuration
api_url = base_url+'/api/v2/unified_job_templates/?or__type=job_template&or__type=workflow_job_template'
template_output_file = 'AAP_Templates.csv'
separator = '|'  
output_folder = 'AAP_Report/'
base_name, extension = template_output_file.rsplit('.', 1)
output_file = f"{base_name}_{timestamp}.{extension}"

#Job Execution Configuration
job_url = base_url+'/api/v2/jobs/'
job_output_file = 'ansible_template_report.csv'
job_file_separator = '|'  

# Prepare to write to CSV - Templates
with open(output_folder+output_file, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=separator)
    # Writing CSV Headers
    writer.writerow([
        'ORGANIZATION_NAME',
        'ORGANIZATION_DESCRIPTION',
        'TEMPLATE_ID',
        'TEMPLATE_TYPE',
        'TEMPLATE_NAME', 
        'TEMPLATE_DESCRIPTION',
        'TEMPLATE_CREATED_BY',
        'TEMPLATE_CREATION_DATE',
        'TEMPLATE_EDIT_DATE',
        'PLAYBOOK',
        'HAS_SURVEY',
        'PROJECT_ID',
        'PROJECT_NAME',
        'PROJECT_DESCRIPTION',
        'TOTAL_EXECUTED_JOBS',
        'LAST_JOB_RUN',
        'LAST_JOB_FAILED',
        'NEXT_JOB_RUN'
        ])  

    while api_url:  # This loop will run as long as api_url is not None
        response = requests.get(api_url, headers=headers)
        templates_data = response.json()

        # Write each template to the CSV file
        for template in templates_data['results']:
            #Manage Project
            project_value= template.get('summary_fields',{}).get('project',{})
            # Print Short Results
            print(f"{GREEN}Found Template: {template['id']}  --> Writing to file{RESET}")
            writer.writerow([
                template['summary_fields']['organization']['name'],
                template['summary_fields']['organization']['description'],
                template['id'],
                template['type'],
                template['name'], 
                template['description'],
                template['summary_fields']['created_by']['username'],
                template['created'],
                template['modified'],
                template.get('playbook',''),
                template['survey_enabled'],
                project_value.get('id', ''),
                project_value.get('name', ''),
                project_value.get('description', ''),
                len(template['summary_fields']['recent_jobs']),
                template['last_job_run'],
                template['last_job_failed'],
                template['next_job_run']
                ])
        
        # Check for next page
        api_url = templates_data.get('next')  # Update the URL for the next request; will be None if no more pages

print(f"{GREEN}Data written to {output_file}{RESET}")
