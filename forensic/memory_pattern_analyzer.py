#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import re
import argparse

class MemoryPatternAnalyzer:
    def __init__(self, memory_dump_path):
        self.memory_dump_path = memory_dump_path
        self.patterns = defaultdict(int)
        self.suspicious_regions = []
        
    def analyze_memory_dump(self):
        """Analyze the memory dump for patterns and suspicious regions"""
        try:
            with open(self.memory_dump_path, 'rb') as f:
                data = f.read()
                
            # Analyze for common patterns
            self._analyze_patterns(data)
            
            # Look for suspicious regions
            self._find_suspicious_regions(data)
            
            # Generate report
            self._generate_report()
            
        except Exception as e:
            print(f"Error analyzing memory dump: {str(e)}")
    
    def _analyze_patterns(self, data):
        """Analyze the data for common patterns"""
        # Look for common memory patterns
        patterns = {
            'Null bytes': b'\x00' * 4,
            'FF bytes': b'\xFF' * 4,
            'Common shellcode patterns': b'\x90' * 4,  # NOP sled
            'PE header': b'MZ',
            'ELF header': b'\x7FELF'
        }
        
        for pattern_name, pattern in patterns.items():
            count = data.count(pattern)
            if count > 0:
                self.patterns[pattern_name] = count
    
    def _find_suspicious_regions(self, data):
        """Identify potentially suspicious memory regions"""
        # Look for regions with high entropy
        chunk_size = 1024
        for i in range(0, len(data), chunk_size):
            chunk = data[i:i+chunk_size]
            if len(chunk) < chunk_size:
                continue
                
            entropy = self._calculate_entropy(chunk)
            if entropy > 0.8:  # High entropy threshold
                self.suspicious_regions.append({
                    'offset': i,
                    'entropy': entropy,
                    'size': chunk_size
                })
    
    def _calculate_entropy(self, data):
        """Calculate the entropy of a data chunk"""
        if not data:
            return 0
            
        counts = defaultdict(int)
        for byte in data:
            counts[byte] += 1
            
        entropy = 0
        length = len(data)
        for count in counts.values():
            probability = count / length
            entropy -= probability * np.log2(probability)
            
        return entropy / 8  # Normalize to 0-1 range
    
    def _generate_report(self):
        """Generate a report of the analysis"""
        print("\n=== Memory Pattern Analysis Report ===")
        print(f"\nFile: {self.memory_dump_path}")
        
        print("\nPattern Analysis:")
        for pattern, count in self.patterns.items():
            print(f"{pattern}: {count} occurrences")
            
        print("\nSuspicious Regions:")
        for region in self.suspicious_regions:
            print(f"Offset: 0x{region['offset']:08x}")
            print(f"Entropy: {region['entropy']:.3f}")
            print(f"Size: {region['size']} bytes")
            print("---")

def main():
    parser = argparse.ArgumentParser(description='Analyze memory dumps for patterns and suspicious regions')
    parser.add_argument('memory_dump', help='Path to the memory dump file')
    args = parser.parse_args()
    
    analyzer = MemoryPatternAnalyzer(args.memory_dump)
    analyzer.analyze_memory_dump()

if __name__ == '__main__':
    main() 