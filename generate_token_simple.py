import os
import sys
sys.path.append(os.getcwd())

try:
    from app.auth import generate_token
    
    # Generate token
    token = generate_token("admin")
    print("\nGenerated token:")
    print("-" * 50)
    print(token)
    print("-" * 50)
    
except ImportError as e:
    print("\nError: Missing required packages")
    print("Please run: pip install flask requests")
    print(f"Original error: {e}")
except Exception as e:
    print(f"\nUnexpected error: {e}") 