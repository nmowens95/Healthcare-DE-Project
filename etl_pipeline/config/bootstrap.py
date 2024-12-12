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
    if not os.path.exists('logs'):
        os.makedirs('logs')

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        filename='logs/etl.log',
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )

    # Add console handler to see logs in terminal as well
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S'))
    console_handler.setLevel(logging.DEBUG)
    logging.getLogger().addHandler(console_handler)
