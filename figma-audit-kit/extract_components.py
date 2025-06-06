import requests
import json

# Get credentials from environment variables
import os

ACCESS_TOKEN = os.getenv('FIGMA_ACCESS_TOKEN')
FILE_KEY = os.getenv('FIGMA_FILE_KEY')

if not ACCESS_TOKEN or not FILE_KEY:
    print("❌ Error: Please set FIGMA_ACCESS_TOKEN and FIGMA_FILE_KEY environment variables")
    exit(1)
headers = {
    'X-Figma-Token': ACCESS_TOKEN
}

url = f"https://api.figma.com/v1/files/{FILE_KEY}"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    components = []

    # New function to walk tree and track parent
    def find_components(node, parent_name=None):
        if node.get('type') == 'COMPONENT':
            # Save parent frame/section + component name
            components.append(f"{parent_name} > {node['name']}")
        if 'children' in node:
            for child in node['children']:
                find_components(child, node.get('name', parent_name))

    find_components(data['document'])

    with open('components_list.txt', 'w') as f:
        for item in components:
            f.write(item + '\n')

    print(f"✅ Extracted {len(components)} components with parent names into 'components_list.txt'")
else:
    print(f"❌ Failed to fetch file: {response.status_code} - {response.text}")