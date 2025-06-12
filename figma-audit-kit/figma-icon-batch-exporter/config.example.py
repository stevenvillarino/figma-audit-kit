"""
Configuration file for Figma Icon Library Batch Exporter

Copy this file to config.py and update with your settings.
"""

# --- Required Configuration ---

# Your Figma file key (from the URL)
# Example: https://www.figma.com/design/44F3bU0GUSdy8kA9FvvM3o/My-Icon-Library
#                                    ^^^^^^^^^^^^^^^^^^^^
#                                    This is your file key
FIGMA_FILE_KEY = 'your-figma-file-key-here'

# Your Figma personal access token (starts with 'figd_')
# Get this from: https://www.figma.com/settings (Personal Access Tokens section)
FIGMA_TOKEN = 'your-figma-token-here'

# --- Optional Configuration ---

# Specify which page to export from (set to None to export from all pages)
# Example: "Simple", "Icons", "Components", etc.
TARGET_PAGE_NAME = None  # Change to "YourPageName" to filter by page

# List of component names you want to export
# Leave empty [] to see all available components
COMPONENT_NAMES = [
    # Example component names - replace with your actual component names
    "Icon1",
    "Icon2",
    "Button",
    "Card",
    # Add your component names here...
]

# --- Output Settings ---

# Directory where exported SVG files will be saved
OUTPUT_DIR = 'exported_icons'

# Number of components to process in each batch (adjust if you hit rate limits)
BATCH_SIZE = 100

# --- Advanced Settings ---

# Uncomment and modify these if you need custom behavior

# Custom filename sanitization (optional)
# def sanitize_filename(name):
#     return name.replace(" ", "_").replace("/", "-").lower()

# Custom variant filtering (optional)
# ALLOWED_VARIANTS = ["Solid", "Duotone"]  # Only export these variants
