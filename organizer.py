from pathlib import (Path, PurePath)
import shutil

my_dir = Path('.')

exercicios = list()

c_sources = list(my_dir.glob("**/*.c"))
cpp_sources = list(my_dir.glob("**/*.cpp"))
python_sources = list(my_dir.glob("**/*.py"))


def return_files():
    for x in c_sources:
        yield x
    for x in cpp_sources:
        yield x
    for x in python_sources:
        yield x


def return_my_dir_with_exercise(exercise: str) -> PurePath:
    return my_dir.joinpath(exercise)

def get_exercise(file):
    return file.stem if not file.stem.startswith(
            "URI ") else file.stem[4:]

def create_all_folders():
    for file in return_files():
        exercicio = get_exercise(file)
        if exercicio == 'organizer':
            continue
        if not return_my_dir_with_exercise(exercicio).exists():
            return_my_dir_with_exercise(exercicio).mkdir()

create_all_folders()

for file in c_sources:
    exercicio = get_exercise(file)
    c_dir = my_dir.joinpath(exercicio).joinpath("C")
    if not c_dir.exists():
        c_dir.mkdir()
    shutil.move(
        file.absolute(),
        c_dir.joinpath(f"{exercicio}.c").absolute()
    )
for file in cpp_sources:
    exercicio = get_exercise(file)
    c_dir = my_dir.joinpath(exercicio).joinpath("CPP")
    if not c_dir.exists():
        c_dir.mkdir()
    shutil.move(
        file.absolute(),
        c_dir.joinpath(f"{exercicio}.cpp").absolute()
    )
for file in python_sources:
    exercicio = get_exercise(file)
    if exercicio != "organizer":
        c_dir = my_dir.joinpath(exercicio).joinpath("Python3")
        if not c_dir.exists():
            c_dir.mkdir()
        shutil.move(
            file.absolute(),
            c_dir.joinpath(f"{exercicio}.py").absolute()
        )