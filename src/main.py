from extract_and_generate_page import generate_pages_recursive
import os
import shutil


def delete_dir_contents(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        print(f"created directory '{dir_path}'")
        return

    dir_contents = os.listdir(dir_path)
    for item in dir_contents:
        if os.path.isdir(dir_path + item):
            delete_dir_contents(f"{dir_path}{item}/")
            os.rmdir(f"{dir_path}{item}/")
            print(f"deleted directory '{item}' from public/")
        else:
            os.remove(dir_path + item)
            print(f"deleted file '{item}' from {"/".join(dir_path.split("/")[-2:])}")


def copy_dir_contents(src_dir_path, dest_dir_path):
    dir_contents = os.listdir(src_dir_path)
    for item in dir_contents:
        if os.path.isdir(src_dir_path + item):
            os.mkdir(dest_dir_path + item)
            print(f"created directory '{item}' in public/ ")
            copy_dir_contents(f"{src_dir_path}{item}/", f"{dest_dir_path}{item}/")
        else:
            shutil.copy(src_dir_path + item, dest_dir_path)
            print(f"copied file '{item}' from static/ to public/")


def main():
    root_dir = os.getcwd() + "/"
    destination_dir = f"{root_dir}public/"
    source_dir = f"{root_dir}static/"
    gen_page_from_path = f"{root_dir}content/"
    template_path = f"{root_dir}template.html"
    gen_page_to_path = f"{root_dir}public/"

    delete_dir_contents(destination_dir)

    copy_dir_contents(source_dir, destination_dir)

    generate_pages_recursive(gen_page_from_path, template_path, gen_page_to_path)


if __name__ == "__main__":
    main()
