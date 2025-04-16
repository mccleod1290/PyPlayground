import sys
import string

def generate_pattern(length):
    pattern = ""
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    
    a = 0
    b = 0
    c = 0
    
    while len(pattern) < length:
        pattern += chars[a] + chars[b] + chars[c]
        c += 1
        if c == len(chars):
            c = 0
            b += 1
            if b == len(chars):
                b = 0
                a += 1
                if a == len(chars):
                    a = 0
                    
    return pattern[:length]

def find_offset(pattern, value):
    try:
        # Convert value to bytes if it's a string
        if isinstance(value, str):
            value = value.encode()
            
        # Search for the pattern
        index = pattern.find(value)
        if index != -1:
            return index
            
        # Try reversed byte order
        reversed_value = value[::-1]
        index = pattern.find(reversed_value)
        if index != -1:
            return index
            
        return -1
        
    except Exception as e:
        print(f"Error finding offset: {str(e)}")
        return -1

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("Generate pattern: python pattern_generator.py generate <length>")
        print("Find offset: python pattern_generator.py find <pattern> <value>")
        sys.exit(1)
        
    command = sys.argv[1].lower()
    
    if command == "generate":
        if len(sys.argv) != 3:
            print("Usage: python pattern_generator.py generate <length>")
            sys.exit(1)
            
        try:
            length = int(sys.argv[2])
            pattern = generate_pattern(length)
            print(f"\nGenerated pattern ({length} bytes):")
            print(pattern)
            
        except ValueError:
            print("Error: Length must be an integer")
            
    elif command == "find":
        if len(sys.argv) != 4:
            print("Usage: python pattern_generator.py find <pattern> <value>")
            sys.exit(1)
            
        pattern = sys.argv[2]
        value = sys.argv[3]
        
        offset = find_offset(pattern, value)
        if offset != -1:
            print(f"\nOffset found at position: {offset}")
        else:
            print("\nOffset not found")
            
    else:
        print("Unknown command. Use 'generate' or 'find'")

if __name__ == "__main__":
    main() 