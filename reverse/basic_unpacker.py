import struct
import sys
import os

def detect_packer(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
            
        # Check for common packer signatures
        signatures = {
            b'UPX!': 'UPX',
            b'!EP': 'PECompact',
            b'FSG!': 'FSG',
            b'MZP': 'Morphine',
            b'MEW': 'MEW',
            b'ASPack': 'ASPack'
        }
        
        for sig, name in signatures.items():
            if sig in data:
                return name
                
        return "Unknown"
        
    except Exception as e:
        print(f"Error detecting packer: {str(e)}")
        return None

def unpack_file(file_path):
    packer = detect_packer(file_path)
    if not packer:
        return
        
    print(f"\nDetected packer: {packer}")
    
    if packer == "UPX":
        try:
            # Create backup
            backup_path = file_path + '.bak'
            os.system(f'copy "{file_path}" "{backup_path}"')
            
            # Try to unpack using UPX
            os.system(f'upx -d "{file_path}"')
            print("Unpacking completed")
            
        except Exception as e:
            print(f"Error unpacking: {str(e)}")
    else:
        print(f"Automatic unpacking not supported for {packer}")
        print("Please use appropriate unpacking tools")

if len(sys.argv) != 2:
    print("Usage: python basic_unpacker.py <packed_file>")
    sys.exit(1)

file_path = sys.argv[1]
unpack_file(file_path) 