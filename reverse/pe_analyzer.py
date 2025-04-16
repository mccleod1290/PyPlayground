import struct
import sys
import os

def analyze_pe(file_path):
    try:
        with open(file_path, 'rb') as f:
            # Check DOS header
            dos_header = f.read(2)
            if dos_header != b'MZ':
                print("Not a valid PE file")
                return
                
            # Get PE header offset
            f.seek(60)
            pe_offset = struct.unpack('<I', f.read(4))[0]
            
            # Check PE header
            f.seek(pe_offset)
            pe_header = f.read(4)
            if pe_header != b'PE\0\0':
                print("Invalid PE header")
                return
                
            print("\nPE File Analysis:")
            print("=" * 50)
            
            # Get machine type
            machine = struct.unpack('<H', f.read(2))[0]
            machine_types = {
                0x014c: "x86",
                0x0200: "Intel Itanium",
                0x8664: "x64"
            }
            print(f"Machine Type: {machine_types.get(machine, 'Unknown')}")
            
            # Get number of sections
            f.seek(pe_offset + 6)
            num_sections = struct.unpack('<H', f.read(2))[0]
            print(f"Number of Sections: {num_sections}")
            
            # Get timestamp
            f.seek(pe_offset + 8)
            timestamp = struct.unpack('<I', f.read(4))[0]
            print(f"Timestamp: {timestamp}")
            
            # Get entry point
            f.seek(pe_offset + 40)
            entry_point = struct.unpack('<I', f.read(4))[0]
            print(f"Entry Point: 0x{entry_point:08x}")
            
            # Analyze sections
            print("\nSections:")
            print("-" * 50)
            section_offset = pe_offset + 24 + struct.unpack('<H', f.read(2))[0]
            f.seek(section_offset)
            
            for i in range(num_sections):
                name = f.read(8).decode().strip('\0')
                virtual_size = struct.unpack('<I', f.read(4))[0]
                virtual_address = struct.unpack('<I', f.read(4))[0]
                raw_size = struct.unpack('<I', f.read(4))[0]
                raw_offset = struct.unpack('<I', f.read(4))[0]
                
                print(f"\nSection {i+1}:")
                print(f"Name: {name}")
                print(f"Virtual Size: 0x{virtual_size:08x}")
                print(f"Virtual Address: 0x{virtual_address:08x}")
                print(f"Raw Size: 0x{raw_size:08x}")
                print(f"Raw Offset: 0x{raw_offset:08x}")
                
    except Exception as e:
        print(f"Error analyzing file: {str(e)}")

if len(sys.argv) != 2:
    print("Usage: python pe_analyzer.py <pe_file>")
    sys.exit(1)

file_path = sys.argv[1]
analyze_pe(file_path) 