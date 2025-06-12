# Figma Component Audit Tool

A Python script that extracts all components from a Figma file and maintains their hierarchical structure. This tool helps designers and developers maintain a clear overview of their design system components and their relationships with parent containers.

## Features

- Extracts all components from a Figma file
- Maintains hierarchical structure (parent frames/sections)
- Outputs a clean, readable format showing component relationships
- Shows component relationships with parent containers
- Easy to set up and use
- Uses environment variables for secure credential management

## Prerequisites

- Python 3.x
- `requests` library
- Figma access token
- Figma file key

## Installation

1. Navigate to the component audit tool directory:
```bash
cd figma-component-audit
```

2. Install the required dependency:
```bash
pip install requests
```

## Configuration

### Method 1: Environment Variables (Recommended)

Set your Figma credentials as environment variables:

```bash
export FIGMA_ACCESS_TOKEN="your_figma_access_token_here"
export FIGMA_FILE_KEY="your_figma_file_key_here"
```

### Getting Your Credentials

1. **Figma Access Token**: 
   - Go to Figma.com → Account Settings → Personal access tokens
   - Create a new access token
   - Copy the token (starts with `figd_`)

2. **Figma File Key**: 
   - Open your Figma file in the browser
   - The file key is in the URL: `figma.com/file/[FILE_KEY]/...`
   - Copy the file key from the URL

## Usage

1. Set your environment variables (see Configuration above)

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
Button Container > Primary Button
Navigation > Menu Item
```

## Example Output

```
Icons > Home Icon
Icons > Search Icon
Buttons > Primary Button
Buttons > Secondary Button
Cards > Product Card
Navigation > Main Nav Item
```

## Security Note

⚠️ **Important**: Never commit your Figma access token to version control. Always use environment variables or a configuration file that's excluded from git for sensitive information.

## Troubleshooting

### Common Issues

1. **Missing credentials error**: Make sure both `FIGMA_ACCESS_TOKEN` and `FIGMA_FILE_KEY` environment variables are set
2. **401 Unauthorized**: Check that your access token is valid and has permission to access the file
3. **404 Not Found**: Verify that your file key is correct
4. **No components found**: Ensure your Figma file contains components (not just frames or other elements)

### Getting Help

If you encounter issues:
1. Verify your credentials have access to the Figma file
2. Check that the file contains components (not just regular frames)
3. Ensure you have the `requests` library installed

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Part of the Figma Audit Kit by Steven Villarino 