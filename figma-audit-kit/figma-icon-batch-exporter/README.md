# Figma Icon Library Batch Exporter

A Python script for batch exporting SVG icons from Figma component libraries with support for component variants, page filtering, and intelligent naming conventions.

## Overview

This tool allows you to programmatically export specific icons from a Figma file as SVG files. It's particularly useful for design systems and icon libraries where you need to export multiple component variants (like solid, duotone, outlined styles) while maintaining organized file naming.

## Features

- **Batch Export**: Export hundreds of icons in a single operation
- **Variant Support**: Automatically handles component variants (Solid, Duotone, etc.)
- **Page Filtering**: Export from specific pages or all pages in your Figma file
- **Intelligent Naming**: Creates descriptive filenames using `ParentComponent-Variant.svg` format
- **Selective Export**: Choose specific components to export rather than the entire library
- **API Rate Limiting**: Automatically batches requests to respect Figma API limits
- **Error Handling**: Comprehensive error reporting and graceful failure handling
- **Progress Tracking**: Real-time feedback on export progress

## Prerequisites

- Python 3.6 or higher
- `requests` library (`pip install requests`)
- `pathlib` (included in Python 3.4+)
- Figma account with API access
- Access to the Figma file you want to export from

## Quick Start

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/figma-icon-batch-exporter.git
   cd figma-icon-batch-exporter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the script**
   - Copy `config.example.py` to `config.py`
   - Add your Figma token and file key
   - Specify which components to export

4. **Run the script**
   ```bash
   python figma_icon_exporter.py
   ```

## Setup

### 1. Get Your Figma Access Token

1. Go to [Figma Account Settings](https://www.figma.com/settings)
2. Scroll down to "Personal Access Tokens"
3. Click "Create new token"
4. Give it a descriptive name (e.g., "Icon Export Script")
5. Copy the generated token (it starts with `figd_`)

### 2. Get Your Figma File Key

Your Figma file key is found in the URL of your Figma file:
```
https://www.figma.com/design/44F3bU0GUSdy8kA9FvvM3o/My-Icon-Library
                              ^^^^^^^^^^^^^^^^^^^^
                              This is your file key
```

### 3. Install Dependencies

```bash
pip install requests
```

Or if you prefer using a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

### Method 1: Using config.py (Recommended)

1. Copy `config.example.py` to `config.py`:
   ```bash
   cp config.example.py config.py
   ```

2. Edit `config.py` with your settings:
   ```python
   # Your Figma credentials
   FIGMA_FILE_KEY = 'your-figma-file-key-here'
   FIGMA_TOKEN = 'your-figma-token-here'
   
   # Page filtering (optional)
   TARGET_PAGE_NAME = "Simple"  # Set to None to export from all pages
   
   # Components to export
   COMPONENT_NAMES = [
       "IconName1",
       "IconName2", 
       "IconName3"
   ]
   
   # Output settings
   OUTPUT_DIR = 'exported_icons'
   BATCH_SIZE = 100
   ```

### Method 2: Environment Variables

Set environment variables:
```bash
export FIGMA_TOKEN="your-token-here"
export FIGMA_FILE_KEY="your-file-key-here"
```

### Method 3: Direct Script Editing

Edit the configuration section directly in `figma_icon_exporter.py`.

## Usage

### Basic Usage

```bash
python figma_icon_exporter.py
```

### Page-Specific Export

To export only from a specific page:
```python
TARGET_PAGE_NAME = "Simple"  # Only export from "Simple" page
```

To export from all pages:
```python
TARGET_PAGE_NAME = None  # Export from all pages
```

### Finding Available Components and Pages

Run with an empty component list to discover what's available:
```python
COMPONENT_NAMES = []  # Empty list
```

The script will output:
```
Available pages: Simple, Complex, Legacy
Available component names in the file:
  - AVSync
  - ClosedCaptions
  - Camera360
  - PlayCircle
  ... and 150 more
```

### Output Structure

The script creates the following file structure:

```
your-project-directory/
├── figma_icon_exporter.py
├── config.py
└── exported_icons/
    ├── AVSync-Solid.svg
    ├── AVSync-Duotone.svg
    ├── ClosedCaptions-Solid.svg
    ├── ClosedCaptions-Duotone.svg
    └── ...
```

## File Naming Convention

The script uses the following naming pattern:

```
{ParentComponentName}-{VariantName}.svg
```

Examples:
- `ClosedCaptions-Solid.svg`
- `ClosedCaptions-Duotone.svg`
- `PlayCircle-Filled.svg`
- `Camera360-Outline.svg`

### Character Sanitization

The script automatically sanitizes filenames by:
- Removing spaces
- Converting `/` to `_`
- Removing `!` characters
- Converting `+` to `Plus`

So `HDR10+` becomes `HDR10Plus.svg`.

## Error Handling

The script includes comprehensive error handling for common issues:

### Authentication Errors
```
Error from Figma API: Invalid token
```
**Solution**: Check your `FIGMA_TOKEN` is correct and hasn't expired.

### File Access Errors
```
Error from Figma API: File not found
```
**Solution**: Verify your `FIGMA_FILE_KEY` and ensure you have access to the file.

### Component Not Found
```
Missing components: IconName1, IconName2, IconName3
```
**Solution**: Check component names match exactly (case-sensitive).

### Rate Limiting
The script automatically handles rate limiting by:
- Batching requests (100 components per batch by default)
- Continuing with remaining batches if one fails
- Providing detailed progress feedback

## Advanced Usage

### Custom Output Directory

```python
OUTPUT_DIR = '/path/to/your/icon/folder'
```

### Filtering Specific Variants

Modify the filtering logic to export only certain variants:

```python
# Only export 'Solid' variants
filtered = [c for c in components 
           if c.get('containing_frame', {}).get('name') in COMPONENT_NAMES 
           and c.get('name') == 'Variant=Solid']
```

### Processing Large Libraries

For very large icon libraries (500+ components):

1. Reduce batch size:
```python
BATCH_SIZE = 50  # Smaller batches
```

2. Run in segments:
```python
COMPONENT_NAMES = COMPONENT_NAMES[:100]  # First 100 components
```

## Integration Examples

### Using with Build Systems

```bash
# In your package.json scripts
"export-icons": "python figma_icon_exporter.py",
"build": "npm run export-icons && npm run build-app"
```

### Using with CI/CD

```yaml
# GitHub Actions example
- name: Export Figma Icons
  run: |
    python figma_icon_exporter.py
  env:
    FIGMA_TOKEN: ${{ secrets.FIGMA_TOKEN }}
    FIGMA_FILE_KEY: ${{ secrets.FIGMA_FILE_KEY }}
```

### Using with Make

```makefile
export-icons:
	python figma_icon_exporter.py

build: export-icons
	# Your build commands here
```

## Troubleshooting

### Common Issues

**Problem**: Script says "No matching components found"
**Solution**: 
- Verify component names are spelled exactly as they appear in Figma
- Check that components are published in your Figma library
- Use empty `COMPONENT_NAMES` list to see available components
- Verify you're targeting the correct page with `TARGET_PAGE_NAME`

**Problem**: Some icons fail to download
**Solution**:
- Check your internet connection
- Verify the failed components exist and are accessible
- Try running the script again (it will skip already downloaded files)

**Problem**: "400 Bad Request" errors
**Solution**:
- Reduce batch size to 50 or fewer components
- Check for special characters in component names
- Verify your file key and token are correct

**Problem**: Icons from wrong page are exported
**Solution**:
- Set `TARGET_PAGE_NAME` to the specific page you want
- Run with empty `COMPONENT_NAMES` to see available pages

### Debug Mode

For detailed debugging, the script includes verbose logging that shows:
- API request URLs
- Response status codes
- Component discovery process
- Page filtering results
- Batch processing progress
- Individual file download status

## API Limits and Best Practices

### Figma API Limits
- Rate limit: ~100 requests per minute
- File size limit: Components must be under 4MB each
- Token expiration: Personal access tokens don't expire but can be revoked

### Best Practices
1. **Use descriptive component names** in Figma for easier identification
2. **Organize variants consistently** (e.g., always use "Solid", "Duotone", "Outline")
3. **Use page organization** to separate different icon sets
4. **Test with small batches first** before running large exports
5. **Keep your token secure** and don't commit it to version control
6. **Use version control** for your exported icons to track changes

## Security Notes

- Never commit your Figma token to version control
- Use environment variables or `config.py` (which should be gitignored) for sensitive data
- Regularly rotate your Figma access tokens
- Be mindful of file permissions when using in shared environments

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

1. Fork the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Create `config.py` from `config.example.py`
6. Make your changes and test thoroughly

## License

MIT License - see [LICENSE](LICENSE) for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history.

## Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/figma-icon-batch-exporter/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/figma-icon-batch-exporter/discussions)
- **Figma API Docs**: [Figma REST API](https://www.figma.com/developers/api)

---

Made with ❤️ for the design systems community