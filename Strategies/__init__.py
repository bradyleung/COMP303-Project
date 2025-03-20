import os
import importlib

# Ensure the folder is treated as a package
PACKAGE_NAME = "Strategies"

# Get the absolute path to the folder
folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), PACKAGE_NAME)

# Get the list of all .py files in the folder (excluding __init__.py)
module_files = [f for f in os.listdir(folder_path) 
                if f.endswith('.py') and f != '__init__.py']

# Dynamically import all modules and collect their classes
for module_file in module_files:
    module_name = module_file[:-3]  # Remove the .py extension
    try:
        # Import the module
        module = importlib.import_module(f".{module_name}", package=PACKAGE_NAME)
        
        # Add all classes from the module to the current namespace
        for name, obj in vars(module).items():
            if isinstance(obj, type):  # Check if it's a class
                globals()[name] = obj
    except ImportError as e:
        print(f"Failed to import module {module_name}: {e}")
    except Exception as e:
        print(f"Error processing module {module_name}: {e}")