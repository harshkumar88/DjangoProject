#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newApiProject.settings')
    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    except ImportError as exc:
       "error"
   


if __name__ == '__main__':
    main()
