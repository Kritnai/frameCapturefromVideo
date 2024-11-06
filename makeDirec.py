import os

def makeDirectory(nameOfDirectory):
    
    os.makedirs(f"output/{nameOfDirectory}", exist_ok=True)
    
makeDirectory("test")