# Figma Audit Kit

A Python-based tool for auditing and extracting component information from Figma files. This tool helps designers and developers maintain a clear overview of their design system components and their hierarchical structure.

## Features

- Extracts all components from a Figma file
- Maintains hierarchical structure (parent frames/sections)
- Outputs a clean, readable format
- Shows component relationships with parent containers
- Easy to set up and use

## Prerequisites

- Python 3.x
- `requests` library
- Figma access token
- Figma file key

## Installation

1. Clone the repository:
```bash
git clone git@github.com:stevenvillarino/figma-audit-kit.git
cd figma-audit-kit
```

2. Install the required dependency:
```bash
pip install requests
```

## Configuration

Before running the script, you need to set up two important pieces of information in `extract_components.py`:

1. **Figma Access Token**: Get this from your Figma account settings
   - Go to Figma.com → Account Settings → Personal access tokens
   - Create a new access token
   - Replace `'FIGMA ACCESS TOKEN HERE'` in the script

2. **Figma File Key**: This is the unique identifier for your Figma file
   - Open your Figma file in the browser
   - The file key is in the URL: `figma.com/file/[FILE_KEY]/...`
   - Replace `'FIGMA FILE KEY HERE'` in the script

## Usage

1. Configure your access token and file key in `extract_components.py`

2. Run the script:
```bash
python extract_components.py
```

3. Check the output file `components_list.txt` for the extracted component list

## Output Format

The script generates a `components_list.txt` file with components listed in a hierarchical format:
```
Parent Frame > Component Name
Section > Subsection > Component Name
```

## Security Note

⚠️ Never commit your Figma access token to version control. Consider using environment variables or a configuration file that's excluded from git for sensitive information.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

---

Created by Steven Villarino
