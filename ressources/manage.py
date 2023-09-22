import os
import sys


def main():
    """Run administrative tasks."""
    # Set the DJANGO_SETTINGS_MODULE environment variable to the settings module of the project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'litreview_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If there's an ImportError, raise a new ImportError
        raise ImportError() from exc
    # Execute the Django management command specified in the command line arguments
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Call the main function when the script is executed directly
    main()