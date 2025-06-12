# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-06-09

### Added
- Initial release of Figma Icon Library Batch Exporter
- Batch export functionality for Figma components
- Support for component variants (Solid, Duotone, etc.)
- Page filtering capability to export from specific pages
- Intelligent naming convention: `ParentComponent-Variant.svg`
- API rate limiting with automatic batching
- Comprehensive error handling and progress feedback
- Configuration via `config.py` or environment variables
- Character sanitization for safe filenames
- Detailed logging and debugging output

### Features
- Export hundreds of icons in a single operation
- Selective component export by name
- Automatic filename sanitization
- Progress tracking with emoji indicators
- Graceful error handling for failed downloads
- Support for custom output directories
- Configurable batch sizes for API requests

### Security
- Configuration file (`config.py`) excluded from version control
- Support for environment variables for sensitive data
- Clear documentation on token security best practices
