""" Set up app before running it """
from scripts import prepare
from config import INPUT_FILE, OUTPUT_FILE

prepare.write_dump(INPUT_FILE, OUTPUT_FILE)
prepare.print_ratings(OUTPUT_FILE)
