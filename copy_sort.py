import shutil
import argparse
from pathlib import Path


class FileCopier:
    def __init__(self, src_dir, dest_dir='dist'):
        self.src_dir = Path(src_dir)
        self.dest_dir = Path(dest_dir)

    def copy_and_sort(self):
        try:
            if not self.dest_dir.exists():
                self.dest_dir.mkdir(parents=True)

            self._recursive_copy_and_sort(self.src_dir)

        except KeyboardInterrupt:
            print("\nКопіювання перервано користувачем.")

    def _recursive_copy_and_sort(self, src_path):
        for src_item in src_path.iterdir():
            if src_item.is_file():
                self._copy_file(src_item)
            elif src_item.is_dir():
                self._recursive_copy_and_sort(src_item)

    def _copy_file(self, src_path):
        try:
            extension = src_path.suffix.lower()
            dest_subdir = self.dest_dir / (extension[1:] if extension else 'other')

            dest_subdir.mkdir(parents=True, exist_ok=True)
            dest_path = dest_subdir / src_path.name

            shutil.copy2(src_path, dest_path)
            print(f"Файл {src_path.name} скопійовано у {dest_subdir}")
        except Exception as e:
            print(f"Помилка копіювання {src_path.name}: {e}")


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
