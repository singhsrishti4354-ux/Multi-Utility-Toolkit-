def read_file(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")

def create_file(filename):
    try:
        file = open(filename, "x")
        file.close()
        print("File created:", filename)
    except FileExistsError:
        print("File already exists")
    except Exception as e:
        print("Error:", e)

def write_file(filename, content):
    try:
        file = open(filename, "w")
        file.write(content)
        file.close()
        print("Content written successfully.")
    except Exception as e:
        print("Error:", e)