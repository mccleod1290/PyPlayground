import struct
import sys

# Common x86 opcodes and their mnemonics
opcodes = {
    0x50: "push eax", 0x51: "push ecx", 0x52: "push edx", 0x53: "push ebx",
    0x54: "push esp", 0x55: "push ebp", 0x56: "push esi", 0x57: "push edi",
    0x58: "pop eax", 0x59: "pop ecx", 0x5A: "pop edx", 0x5B: "pop ebx",
    0x5C: "pop esp", 0x5D: "pop ebp", 0x5E: "pop esi", 0x5F: "pop edi",
    0x90: "nop", 0xC3: "ret", 0xCC: "int 3",
    0xE8: "call", 0xE9: "jmp", 0xEB: "jmp short",
    0x74: "je", 0x75: "jne", 0x72: "jb", 0x73: "jnb",
    0x76: "jbe", 0x77: "jnbe", 0x7C: "jl", 0x7D: "jnl",
    0x7E: "jle", 0x7F: "jnle", 0x70: "jo", 0x71: "jno",
    0x78: "js", 0x79: "jns", 0x7A: "jp", 0x7B: "jnp"
}

def disassemble_instruction(data, offset):
    if offset >= len(data):
        return None, 0
        
    opcode = data[offset]
    mnemonic = opcodes.get(opcode, "unknown")
    size = 1
    
    # Handle instructions with operands
    if opcode in [0xE8, 0xE9]:  # call, jmp
        if offset + 4 < len(data):
            target = struct.unpack('<I', data[offset+1:offset+5])[0]
            mnemonic += f" 0x{target:08x}"
            size = 5
    elif opcode == 0xEB:  # jmp short
        if offset + 1 < len(data):
            disp = data[offset+1]
            target = offset + 2 + disp
            mnemonic += f" 0x{target:08x}"
            size = 2
    elif opcode in [0x74, 0x75, 0x72, 0x73, 0x76, 0x77, 0x7C, 0x7D, 0x7E, 0x7F, 0x70, 0x71, 0x78, 0x79, 0x7A, 0x7B]:  # conditional jumps
        if offset + 1 < len(data):
            disp = data[offset+1]
            target = offset + 2 + disp
            mnemonic += f" 0x{target:08x}"
            size = 2
            
    return mnemonic, size

def disassemble(data, start_offset=0, count=50):
    offset = start_offset
    instructions = []
    
    while len(instructions) < count and offset < len(data):
        mnemonic, size = disassemble_instruction(data, offset)
        if mnemonic is None:
            break
            
        hex_data = ' '.join(f'{b:02x}' for b in data[offset:offset+size])
        instructions.append((offset, hex_data, mnemonic))
        offset += size
        
    return instructions

def main():
    if len(sys.argv) != 2:
        print("Usage: python x86_disassembler.py <binary_file>")
        sys.exit(1)
        
    try:
        with open(sys.argv[1], 'rb') as f:
            data = f.read()
            
        print("\nDisassembly:")
        print("=" * 50)
        print("Offset    Hex Data              Instruction")
        print("-" * 50)
        
        instructions = disassemble(data)
        for offset, hex_data, mnemonic in instructions:
            print(f"0x{offset:08x}  {hex_data.ljust(20)} {mnemonic}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 