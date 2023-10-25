import os, sys

from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from alien_invasion.alien_invasion import AlienInvasion

def main():
    try:
        ai = AlienInvasion()
        ai.run_game()
    except ValueError as ve:
        return str(ve)

if __name__ == "__main__":
    sys.exit(main())