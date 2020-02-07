
import edification.gitsetup
import edification.vimsetup
import edification.storage

def main():
    edification.storage.prepare()
    edification.vimsetup.vimsetup()
    print("""
    echo setup python3.8 symlink
    """)

if __name__ == "__main__":
    main()
