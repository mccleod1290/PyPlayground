import sys
import os
import subprocess
import time

class BasicDebugger:
    def __init__(self, program_path):
        self.program_path = program_path
        self.process = None
        self.breakpoints = set()
        
    def start(self):
        try:
            self.process = subprocess.Popen(
                self.program_path,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print(f"Started process with PID: {self.process.pid}")
            return True
        except Exception as e:
            print(f"Error starting process: {str(e)}")
            return False
            
    def attach(self, pid):
        try:
            # This is a simplified version - in reality, you'd use ptrace or similar
            print(f"Attached to process {pid}")
            return True
        except Exception as e:
            print(f"Error attaching to process: {str(e)}")
            return False
            
    def set_breakpoint(self, address):
        try:
            # In a real debugger, you'd use ptrace to set breakpoints
            self.breakpoints.add(address)
            print(f"Breakpoint set at 0x{address:08x}")
            return True
        except Exception as e:
            print(f"Error setting breakpoint: {str(e)}")
            return False
            
    def continue_execution(self):
        try:
            # In a real debugger, you'd use ptrace to continue execution
            print("Continuing execution...")
            return True
        except Exception as e:
            print(f"Error continuing execution: {str(e)}")
            return False
            
    def step(self):
        try:
            # In a real debugger, you'd use ptrace to single step
            print("Stepping instruction...")
            return True
        except Exception as e:
            print(f"Error stepping: {str(e)}")
            return False
            
    def read_memory(self, address, size):
        try:
            # In a real debugger, you'd use ptrace to read memory
            print(f"Reading {size} bytes from 0x{address:08x}")
            return True
        except Exception as e:
            print(f"Error reading memory: {str(e)}")
            return False
            
    def write_memory(self, address, data):
        try:
            # In a real debugger, you'd use ptrace to write memory
            print(f"Writing {len(data)} bytes to 0x{address:08x}")
            return True
        except Exception as e:
            print(f"Error writing memory: {str(e)}")
            return False
            
    def get_registers(self):
        try:
            # In a real debugger, you'd use ptrace to get registers
            print("Getting register values...")
            return True
        except Exception as e:
            print(f"Error getting registers: {str(e)}")
            return False
            
    def detach(self):
        try:
            if self.process:
                self.process.terminate()
                print("Process terminated")
            return True
        except Exception as e:
            print(f"Error detaching: {str(e)}")
            return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python basic_debugger.py <program>")
        sys.exit(1)
        
    debugger = BasicDebugger(sys.argv[1])
    
    while True:
        print("\nDebugger Commands:")
        print("1. Start program")
        print("2. Attach to process")
        print("3. Set breakpoint")
        print("4. Continue execution")
        print("5. Step instruction")
        print("6. Read memory")
        print("7. Write memory")
        print("8. Get registers")
        print("9. Detach")
        print("0. Exit")
        
        choice = input("\nEnter command number: ")
        
        if choice == "1":
            debugger.start()
        elif choice == "2":
            pid = int(input("Enter PID: "))
            debugger.attach(pid)
        elif choice == "3":
            addr = int(input("Enter address (hex): "), 16)
            debugger.set_breakpoint(addr)
        elif choice == "4":
            debugger.continue_execution()
        elif choice == "5":
            debugger.step()
        elif choice == "6":
            addr = int(input("Enter address (hex): "), 16)
            size = int(input("Enter size: "))
            debugger.read_memory(addr, size)
        elif choice == "7":
            addr = int(input("Enter address (hex): "), 16)
            data = input("Enter data (hex): ")
            debugger.write_memory(addr, bytes.fromhex(data))
        elif choice == "8":
            debugger.get_registers()
        elif choice == "9":
            debugger.detach()
        elif choice == "0":
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main() 