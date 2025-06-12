# Figma Audit Kit

A collection of Python-based tools for working with Figma files, including component auditing and batch icon export functionality.

## Tools Included

### 1. Component Audit Tool (`figma-component-audit/`)
Extracts all components from a Figma file and maintains their hierarchical structure. Helps designers and developers maintain a clear overview of their design system components.

### 2. Icon Batch Exporter (`figma-icon-batch-exporter/`)
A comprehensive tool for batch exporting icons from Figma files with various format and size options.

## Quick Start

### Component Audit Tool
1. Navigate to the component audit directory:
   ```bash
   cd figma-component-audit
   ```

2. Set your environment variables:
   ```bash
   export FIGMA_ACCESS_TOKEN="your_token_here"
   export FIGMA_FILE_KEY="your_file_key_here"
   ```

3. Run the component extractor:
   ```bash
   python extract_components.py
   ```

### Icon Batch Exporter
1. Navigate to the icon exporter directory:
   ```bash
   cd figma-icon-batch-exporter
   ```

2. Follow the setup instructions in the `figma-icon-batch-exporter/README.md`

## Project Structure

```
figma-audit-kit/
├── README.md                          # This file - main documentation
├── figma-component-audit/             # Component audit tool
│   ├── extract_components.py          # Main audit script
│   └── README.md                      # Detailed audit tool docs
└── figma-icon-batch-exporter/         # Icon batch export tool
    ├── figma_icon_exporter.py         # Main export script
    ├── config.example.py              # Configuration template
    ├── requirements.txt               # Dependencies
    ├── setup.py                       # Package setup
    └── README.md                      # Detailed icon exporter docs
```

## Features

### Component Audit Tool Features
- Extracts all components from a Figma file
- Maintains hierarchical structure (parent frames/sections)
- Outputs a clean, readable format
- Shows component relationships with parent containers
- Uses secure environment variables for credentials

### Icon Batch Exporter Features
- **Batch Export**: Export hundreds of icons in a single operation
- **Variant Support**: Automatically handles component variants (Solid, Duotone, etc.)
- **Page Filtering**: Export from specific pages or all pages in your Figma file
- **Intelligent Naming**: Creates descriptive filenames using `ParentComponent-Variant.svg` format
- **Selective Export**: Choose specific components to export rather than the entire library
- **API Rate Limiting**: Automatically batches requests to respect Figma API limits

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

2. Choose your tool and follow the specific installation instructions in each tool's README:
   - **Component Audit**: See `figma-component-audit/README.md`
   - **Icon Exporter**: See `figma-icon-batch-exporter/README.md`

## Getting Your Figma Credentials

Both tools require the same Figma credentials:

1. **Figma Access Token**: Get this from your Figma account settings
   - Go to Figma.com → Account Settings → Personal access tokens
   - Create a new access token
   - Copy the token (starts with `figd_`)

2. **Figma File Key**: This is the unique identifier for your Figma file
   - Open your Figma file in the browser
   - The file key is in the URL: `figma.com/file/[FILE_KEY]/...`
   - Copy the file key from the URL

## Security Note

⚠️ **Important**: Never commit your Figma access token to version control. Both tools use environment variables for secure credential management.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

---

Created by Steven Villarino
