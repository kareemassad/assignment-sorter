import tkinter
import tkinter.filedialog
import ntpath
import Transport


def search(fname, kword):
    # this function just checks the filename for the keyword, returns true if it is there, false if not
    if fname.find(kword) != -1:
        return True
    return False


def returnfilename(filepath):
    # this function takes the filepath and returns the filename
    head, tail = ntpath.split(filepath)
    return tail


def sortfolder(filenames, keyword, directory):
    length = (len(filenames))
    # this keyword will be set based on the input of the user on what to search

    for x in range(length):
        filepath = filenames[x]
        filename = returnfilename(filepath)
        if search(filename, keyword):
            Transport.create_folder(directory, keyword)
            print(directory)
            Transport.trans(directory, filepath, keyword)


def main():
    # this returns a tuple based on the selected files of the user
    filenames = tkinter.filedialog.askopenfilenames()
    keywords = ["ECOR", "Young", "carbon"]
    directory = "C:/Users/dhruv/Documents"
    for x in range(len(keywords)):
        keyword = keywords[x]
        sortfolder(filenames, keyword, directory)


if __name__ == "__main__":
    main()


