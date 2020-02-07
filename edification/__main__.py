
import edification.gitsetup
import edification.vimsetup
import edification.pysetup
import edification.storage

def main():
    edification.storage.prepare()
    edification.vimsetup.vimsetup()
    edification.pysetup.pysetup()

if __name__ == "__main__":
    main()
