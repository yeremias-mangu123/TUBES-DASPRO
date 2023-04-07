import Commands
import argparse

# program utama

# parser folder name
parser = argparse.ArgumentParser()
parser.add_argument("folder")
args = parser.parse_args()


while True:
    masukan = input(">>> ")
    
    
    Commands.run(masukan, folder)