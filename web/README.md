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

### 4. Directory Enumerator (`dir_enum.py`)
Enumerates common files and directories on a web server.

Usage:
```bash
python dir_enum.py <url>
```

Features:
- Common path checking
- Multi-threaded scanning
- Status code analysis
- Error handling

### 5. SQL Injection Tester (`sql_injection_tester.py`)
Tests for basic SQL injection vulnerabilities.

Usage:
```bash
python sql_injection_tester.py <url>
```

Features:
- Common SQL payloads
- Parameter testing
- Error message detection
- URL parameter analysis

### 6. XSS Scanner (`xss_scanner.py`)
Tests for basic Cross-Site Scripting vulnerabilities.

Usage:
```bash
python xss_scanner.py <url>
```

Features:
- Common XSS payloads
- Parameter testing
- Response analysis
- Error handling

### 7. Subdomain Enumerator (`subdomain_enum.py`)
Enumerates possible subdomains for a domain.

Usage:
```bash
python subdomain_enum.py <domain>
```

Features:
- Common subdomain checking
- Multi-threaded scanning
- Status code analysis
- Error handling

## Requirements
- Python 3.x
- requests
- beautifulsoup4
- concurrent.futures

Install dependencies:
```bash
pip install requests beautifulsoup4
```

## Usage Examples

1. Scan a URL:
```bash
python url_scanner.py
```

2. Test HTTP methods:
```bash
python http_method_tester.py http://example.com
```

3. Enumerate directories:
```bash
python dir_enum.py http://example.com
```

4. Test for SQL injection:
```bash
python sql_injection_tester.py http://example.com/page.php?id=1
```

5. Test for XSS:
```bash
python xss_scanner.py http://example.com/page.php?input=test
```

6. Enumerate subdomains:
```bash
python subdomain_enum.py example.com
```

## Notes
- These tools are for educational purposes only
- Always get permission before testing websites
- Be aware of legal implications
- Use responsibly and ethically 