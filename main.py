# main.py - Legacy entry point (use app.py for web version)
print("\n" + "="*60)
print("🏠 Dynamic Energy Assessment Tool")
print("="*60)
print("\nThis tool has been upgraded to a web-based interface!")
print("\nTo run the application:")
print("  1. Install dependencies: pip install -r requirements.txt")
print("  2. Run the web app: python app.py")
print("  3. Open your browser to: http://localhost:5000")
print("\n" + "="*60 + "\n")

# For backward compatibility, try to run the web app
if __name__ == "__main__":
    try:
        import subprocess
        import sys
        print("Starting web application...\n")
        subprocess.run([sys.executable, "app.py"])
    except Exception as e:
        print(f"Error starting web app: {e}")
        print("Please run 'python app.py' manually.")
