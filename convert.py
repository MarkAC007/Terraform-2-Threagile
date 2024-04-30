import hcl2
import yaml

# Load and parse the Terraform file
def parse_terraform(terraform_file):
    with open(terraform_file, 'r') as file:
        tf_config = hcl2.load(file)
    return tf_config

# Convert Terraform configuration to YAML format
def terraform_to_yaml(tf_config)
    yaml_data = {
        'assets': [],
        'components': [],
        'data_assets': [],
        'technical_assets': [],
    }
    for resource_type, resources in tf_config.get('resource', {}).items():
        for name, attributes in resources.items():
            item = {
                'name': name,
                'description': f'{resource_type} managed by Terraform',
                'technology': resource_type,
                'classification': 'Confidential',  # Default classification
            }
            if 'aws_dynamodb_table' in resource_type:
                yaml_data['data_assets'].append(item)
            elif 'aws_s3_bucket' in resource_type:
                yaml_data['technical_assets'].append(item)
            else:
                yaml_data['components'].append(item)
    return yaml_data

# Example usage
terraform_file = 'samples\terr.tf'
tf_config = parse_terraform(terraform_file)
yaml_output = terraform_to_yaml(tf_config)
yaml_str = yaml.dump(yaml_output, sort_keys=False)
print(yaml_str)
