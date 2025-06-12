# Contributing to Figma Icon Library Batch Exporter

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## Development Setup

1. **Fork the repository** on GitHub

2. **Clone your fork locally**:
   ```bash
   git clone https://github.com/yourusername/figma-icon-batch-exporter.git
   cd figma-icon-batch-exporter
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Create your configuration**:
   ```bash
   cp config.example.py config.py
   # Edit config.py with your Figma credentials and test data
   ```

## Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and test thoroughly

3. **Test with your own Figma file** to ensure everything works

4. **Update documentation** if needed

5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: description of your changes"
   ```

6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a pull request** on GitHub

## Code Guidelines

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and small

### Error Handling
- Always include proper error handling for API calls
- Provide helpful error messages for users
- Use try/except blocks appropriately
- Log errors with sufficient detail for debugging

### Testing
- Test with various Figma file structures
- Test error conditions (invalid tokens, missing components, etc.)
- Test with different component naming patterns
- Verify the script works with large component libraries

## Documentation

- Update README.md for new features
- Update CHANGELOG.md following the format
- Add docstrings to new functions
- Include examples for new configuration options

## Types of Contributions

### Bug Reports
When reporting bugs, please include:
- Python version
- Operating system
- Exact error message
- Steps to reproduce
- Figma file structure (if relevant)

### Feature Requests
For new features, please:
- Describe the use case
- Explain why it would be valuable
- Provide examples if possible
- Consider backward compatibility

### Code Contributions
We welcome:
- Bug fixes
- Performance improvements
- New features
- Documentation improvements
- Test improvements

## Commit Message Format

Use clear, descriptive commit messages:

```
Type: Brief description

Longer description if needed
```

Types:
- `Add:` New features
- `Fix:` Bug fixes
- `Update:` Changes to existing features
- `Remove:` Removing features
- `Docs:` Documentation changes
- `Style:` Code style changes
- `Refactor:` Code refactoring
- `Test:` Adding or updating tests

## Pull Request Guidelines

- Fill out the pull request template
- Include a clear description of changes
- Reference any related issues
- Ensure all tests pass
- Update documentation as needed
- Keep pull requests focused on a single feature/fix

## Security Considerations

- Never commit API tokens or secrets
- Review code for potential security issues
- Be mindful of rate limiting and API abuse
- Consider the impact of changes on token security

## Getting Help

If you need help:
- Check existing issues and discussions
- Read the documentation thoroughly
- Ask questions in GitHub Discussions
- Mention specific maintainers if needed

## Code Review Process

1. All changes require review before merging
2. Maintainers will review for:
   - Code quality and style
   - Security considerations
   - Backward compatibility
   - Test coverage
   - Documentation completeness

## Release Process

1. Update version in relevant files
2. Update CHANGELOG.md
3. Create release notes
4. Tag the release
5. Update documentation if needed

Thank you for contributing! 🎉
