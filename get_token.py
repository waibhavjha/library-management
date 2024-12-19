import os
import sys
sys.path.append(os.getcwd())

try:
    from app.auth import generate_token
    token = generate_token("admin")
    print("\nYour token is:")
    print(token)
except ImportError as e:
    print("Error: Please install required packages:")
    print("pip install flask requests")
except Exception as e:
    print(f"Error: {str(e)}") 