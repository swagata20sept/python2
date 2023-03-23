import zipfile
import pathlib
def make_archive(filepaths,dest_dir):
    with zipfile.ZipFile(dest_dir,'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)

if __name__=="__main__":
    make_archive(filepaths=["50_days_code_python\day1.py","50_days_code_python\day2.py"],dest_dir="dest")
