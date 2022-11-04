from typing import Union

from config import *
import logging
import os


logs_folder.mkdir() if not logs_folder.exists() else None

logging.basicConfig(filename=f'logs/file.log',
                    level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s - %(message)s',
                    datefmt='%H:%M:%S:',
                    encoding='utf-8')


class Sorter:
    """Класс для сортивки файлов папки"""

    def __init__(self, path: Union[Path, str]):
        self.path = path
        self._sort_files_by_extensions()

    def _get_file_paths(self):
        """Получение файловых путей"""

        return (file.path for file in os.scandir(self.path) if not file.is_dir())

    def _create_subfolder(self, subfolder_name: str):
        """Создания подпапки"""
        global subfolder_path
        try:
            subfolder_path = self.path / subfolder_name
            if not  subfolder_path.exists():
                subfolder_path.mkdir()
        except OSError:
            logging.error(f'Ошибка создания подпапки {subfolder_path}')

    def _sort_files_by_extensions(self):
        """Сортировка файлов по расширениям"""

        file_count = 0
        for filepath in self._get_file_paths():
            path = Path(filepath)
            extension = filepath.split('.')[-1]

            if extension in extensions:
                subfolder_name = get_subfolder_name_by_extension(extension)
                self._create_subfolder(subfolder_name)

                new_path = Path(self.path, subfolder_name, path.name)
                logging.info(f'{path.name} ---> {"/".join(new_path.parts[-2:])}')
                path.rename(new_path)
                file_count += 1
        logging.info(f'Файлов отсортировано: {file_count}')


if __name__ == '__main__':
    sorter = Sorter(fordef_path)