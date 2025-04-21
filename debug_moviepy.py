import sys
import os
import site

# Print Python version
print(f"Python version: {sys.version}")

# Print site-packages directory
print(f"Site packages: {site.getsitepackages()}")

# Try to locate moviepy
try:
    import moviepy
    print(f"MoviePy found at: {moviepy.__file__}")
    print(f"MoviePy version: {moviepy.__version__}")
    
    # Check if editor module exists in the package
    moviepy_dir = os.path.dirname(moviepy.__file__)
    editor_path = os.path.join(moviepy_dir, 'editor.py')
    editor_dir_path = os.path.join(moviepy_dir, 'editor')
    
    print(f"Does editor.py exist? {os.path.exists(editor_path)}")
    print(f"Does editor directory exist? {os.path.exists(editor_dir_path)}")
    
    # List contents of the moviepy directory
    print("Contents of MoviePy directory:")
    for item in os.listdir(moviepy_dir):
        print(f"  - {item}")
        
except ImportError as e:
    print(f"Error importing moviepy: {e}")