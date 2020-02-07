
import edification.gitsetup

def main():
    edification.gitsetup.gitsetup()
    print("""
    echo install .vimrc
    echo setup python3.8 symlink
    """)

if __name__ == "__main__":
    main()
