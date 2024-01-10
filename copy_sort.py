import os
import shutil
import argparse
from tqdm import tqdm


class FileCopier:
    def __init__(self, src_dir, dest_dir='dist'):
        self.src_dir = src_dir
        self.dest_dir = dest_dir

    def copy_and_sort(self):
        try:
            if not os.path.exists(self.dest_dir):
                os.makedirs(self.dest_dir)

            file_count = sum(len(files) for _, _, files in os.walk(self.src_dir))
            progress_bar = tqdm(total=file_count, desc='Copying files', unit='file')

            for root, dirs, files in os.walk(self.src_dir):
                for file in files:
                    src_path = os.path.join(root, file)
                    self._copy_file(src_path)
                    progress_bar.update(1)

            progress_bar.close()
        except KeyboardInterrupt:
            print("\nКопіювання перервано користувачем.")

    def _copy_file(self, src_path):
        try:
            extension = os.path.splitext(src_path)[-1].lower()
            dest_subdir = os.path.join(self.dest_dir, extension[1:] if extension else 'other')

            os.makedirs(dest_subdir, exist_ok=True)
            dest_path = os.path.join(dest_subdir, os.path.basename(src_path))

            shutil.copy2(src_path, dest_path)
            print(f"Файл {os.path.basename(src_path)} скопійовано у {dest_subdir}")
        except Exception as e:
            print(f"Помилка копіювання {os.path.basename(src_path)}: {e}")


def parse_arguments():
    parser = argparse.ArgumentParser(description='Копіювання та сортування файлів рекурсивно.')
    parser.add_argument('src_dir', help='Шлях до директорії-джерела')
    parser.add_argument('--dest_dir', default='dist', help='Шлях до директорії призначення (за замовчуванням: dist)')
    return parser.parse_args()


def main():
    args = parse_arguments()
    copier = FileCopier(args.src_dir, args.dest_dir)

    try:
        copier.copy_and_sort()
    except FileNotFoundError:
        print(f"Помилка: директорія-джерело '{args.src_dir}' не знайдена.")
    except PermissionError:
        print(f"Помилка: відмовлено в доступі. Перевірте права на читання директорії-джерела.")


if __name__ == "__main__":
    main()
