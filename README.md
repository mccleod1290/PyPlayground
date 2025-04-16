# PyPlayground

A collection of Python scripts and implementations covering essential cybersecurity concepts, with a focus on practical applications and unique implementations. This repository serves as a learning resource for Python programming in security-related domains.

## Repository Structure

### 1. Cryptography
Implementation of fundamental cryptographic algorithms and protocols. This section is crucial for understanding the mathematical foundations of security, encryption techniques, and secure communication protocols. It covers both classical and modern cryptographic methods, providing hands-on experience with encryption, hashing, and digital signatures.
[View Cryptography Programs](cryptography/README.md)

### 2. Forensic
Tools and techniques for digital forensics and investigation. This section focuses on analyzing digital evidence, understanding file systems, and extracting meaningful information from various data sources. It's essential for incident response, evidence collection, and understanding how digital artifacts can be used in investigations.
[View Forensic Programs](forensic/README.md)

### 3. Image Processing
Implementation of image manipulation and analysis techniques. This section is important for understanding how to process and analyze visual data, which is crucial in various security contexts like steganography detection, image forensics, and pattern recognition in security systems.
[View Image Processing Programs](image-processing/README.md)

### 4. Reverse Engineering
Tools for analyzing and understanding binary programs and executables. This section is vital for malware analysis, vulnerability research, and understanding how software works at a low level. It includes implementations for debugging, disassembly, and binary analysis.
[View Reverse Engineering Programs](reverse/README.md)

### 5. Web Security
Tools and techniques for web application security testing. This section focuses on understanding and testing web vulnerabilities, session management, and HTTP protocol analysis. It's crucial for web application security testing and understanding common web vulnerabilities.
[View Web Security Programs](web/README.md)

## Note on Existing Tools

This repository focuses on unique implementations and learning resources. For common security tasks, we recommend using established tools:

### Web Security
- Directory enumeration: `dirb`, `gobuster`, `dirsearch`
- SQL injection testing: `sqlmap`
- XSS scanning: `XSStrike`, `XSS Hunter`
- Subdomain enumeration: `subfinder`, `amass`, `sublist3r`

### File Analysis
- Hex dump: `xxd`, `hexdump`
- String extraction: `strings`
- File type identification: `file`
- Metadata extraction: `exiftool`, `pdfinfo`

## Dependencies

Most programs require:
```bash
pip install opencv-python numpy pycryptodome requests beautifulsoup4
```

Additional dependencies may be required for specific programs and will be listed in their respective directories.

## Usage

Each program is designed to be self-contained and includes:
- Clear input prompts
- Error handling
- Documentation
- Example usage

## Contributing

Contributions are welcome! Please feel free to:
- Add new unique implementations
- Improve existing code
- Add documentation
- Fix bugs
- Suggest new topics

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- College academic labs
- CTF challenges
- Open-source security tools
- Security research papers
- Online security communities 