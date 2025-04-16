# Web Security Tools

A collection of Python tools for web security testing and analysis.

## Tools

### 1. URL Scanner (`url_scanner.py`)
Basic web scanner that analyzes URLs for common information.

Usage:
```bash
python url_scanner.py
```

Features:
- Server information
- Form detection
- Link enumeration
- Basic vulnerability checks

### 2. Session Analyzer (`session_analyzer.py`)
Analyzes web sessions and cookies for security issues.

Usage:
```bash
python session_analyzer.py
```

Features:
- Cookie analysis
- Security headers check
- Session information
- HttpOnly flag detection

### 3. HTTP Method Tester (`http_method_tester.py`)
Tests which HTTP methods are accepted by a web server.

Usage:
```bash
python http_method_tester.py <url>
```

Features:
- Tests common HTTP methods
- Shows response codes
- OPTIONS method analysis
- Error handling

## Note on Common Tools

For common web security tasks, we recommend using established tools:

- Directory enumeration: `dirb`, `gobuster`, `dirsearch`
- SQL injection testing: `sqlmap`
- XSS scanning: `XSStrike`, `XSS Hunter`
- Subdomain enumeration: `subfinder`, `amass`, `sublist3r`

## Dependencies

Required packages:
```bash
pip install requests beautifulsoup4
```

## Contributing

Contributions are welcome! Please feel free to:
- Add new unique implementations
- Improve existing code
- Add documentation
- Fix bugs
- Suggest new topics 