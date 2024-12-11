import logging
import sys
import os

# Dry set up for finding project root (not needed)
# def configure_project_root():
#     """Ensure the project root is in sys.path for module imports."""
#     project_root = os.path.abspath(os.path.dirname(__file__))
#     if project_root not in sys.path:
#         sys.path.insert(0, project_root)

def config_logging():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )