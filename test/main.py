def main():

    file = open("test.txt", "r")
    for line in file.readlines():
        print(line.split())
    file.close()

main()