# Reverse Engineering Tools

A collection of Python tools for reverse engineering and binary analysis.

## Tools

### 1. String Analyzer (`string_analyzer.py`)
Extracts and analyzes ASCII strings from binary files.

Usage:
```bash
python string_analyzer.py <binary_file>
```

Features:
- Extracts printable ASCII strings
- Configurable minimum string length
- Handles binary file reading errors

### 2. Hex Dump (`hex_dump.py`)
Displays binary file contents in hexadecimal format.

Usage:
```bash
python hex_dump.py <binary_file>
```

Features:
- Hexadecimal and ASCII representation
- Configurable bytes per line
- File offset display
- Visual separation of bytes

### 3. PE Analyzer (`pe_analyzer.py`)
Analyzes Portable Executable (PE) file headers and sections.

Usage:
```bash
python pe_analyzer.py <pe_file>
```

Features:
- PE header analysis
- Section information
- Machine type detection
- Entry point identification
- Timestamp analysis

### 4. x86 Disassembler (`x86_disassembler.py`)
Basic disassembler for x86 instructions.

Usage:
```bash
python x86_disassembler.py <binary_file>
```

Features:
- Common x86 instruction decoding
- Hex and assembly output
- Offset tracking
- Basic operand handling

### 5. Basic Unpacker (`basic_unpacker.py`)
Attempts to unpack common packed executables.

Usage:
```bash
python basic_unpacker.py <packed_file>
```

Features:
- Packer detection
- Common packer signatures
- UPX unpacking support
- Backup creation

### 6. Pattern Generator (`pattern_generator.py`)
Generates and analyzes cyclic patterns for buffer overflow exploits.

Usage:
```bash
# Generate pattern
python pattern_generator.py generate <length>

# Find offset
python pattern_generator.py find <pattern> <value>
```

Features:
- Pattern generation
- Offset calculation
- Byte order handling
- Error checking

### 7. Basic Debugger (`basic_debugger.py`)
Basic debugger interface for process analysis.

Usage:
```bash
python basic_debugger.py <program>
```

Features:
- Process control
- Breakpoint management
- Memory operations
- Register access
- Step execution

## Requirements
- Python 3.x
- No additional dependencies required (except for UPX unpacking)

## Usage Examples

1. Extract strings from a binary:
```bash
python string_analyzer.py target.exe
```

2. View hex dump of a binary:
```bash
python hex_dump.py target.exe
```

3. Analyze PE file:
```bash
python pe_analyzer.py target.exe
```

4. Disassemble x86 code:
```bash
python x86_disassembler.py target.bin
```

5. Unpack executable:
```bash
python basic_unpacker.py packed.exe
```

6. Generate pattern:
```bash
python pattern_generator.py generate 100
```

7. Use debugger:
```bash
python basic_debugger.py target.exe
```

## Notes
- These tools are for educational purposes only
- Always analyze files in a safe environment
- Be aware of legal implications when reverse engineering software
- Some features may require additional system permissions 