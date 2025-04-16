# Forensic Tools

This directory contains essential forensic analysis tools that provide unique functionality for digital investigations.

## Tools

### 1. Memory Pattern Analyzer (`memory_pattern_analyzer.py`)
A tool for analyzing memory dumps to identify patterns, potential artifacts, and suspicious memory regions. This tool helps in:
- Identifying memory patterns that might indicate malicious activity
- Analyzing memory allocation patterns
- Detecting potential memory corruption
- Finding hidden or obfuscated data in memory

### 2. Timeline Generator (`timeline_generator.py`)
A tool for creating comprehensive timelines from various system artifacts. This tool:
- Correlates timestamps from different sources (filesystem, registry, logs)
- Creates visual timelines of system activity
- Helps identify sequences of events during investigations
- Supports multiple timestamp formats and timezone handling

### 3. Artifact Correlator (`artifact_correlator.py`)
A tool for correlating digital artifacts across different sources to build a complete picture of system activity. Features:
- Cross-references data from multiple sources
- Identifies relationships between different artifacts
- Creates visual representations of artifact relationships
- Helps in building evidence chains

## Usage

Each tool includes detailed documentation and examples. Refer to the individual tool's documentation for specific usage instructions.

## Dependencies

Required packages:
```bash
pip install pandas matplotlib python-dateutil
```

## Note

These tools are designed to complement existing forensic tools rather than replace them. They focus on providing unique analysis capabilities that aren't readily available in standard forensic toolkits. 