import unittest
import os
from unittest.case import skipIf
from parameterized import parameterized
import yaml


def testFails(test):
    """Evaluates whether a test fails - used for skipping tests"""
    try:
        test()
        return False
    except:
        return True


def get_module_paths():
    return [p for p in os.listdir() if os.path.isdir(p) and p[0] != "."]


def get_lesson_paths():
    paths = []
    modules = get_module_paths()
    for module in modules:
        # print("module:", module)
        lesson_names = [m for m in os.listdir(module)]
        lesson_names = [
            ln for ln in lesson_names if os.path.isdir(os.path.join(module, ln))
        ]

        for lesson in lesson_names:
            if lesson == "Extra":
                continue
            # print("lesson:", lesson)
            path = os.path.join(module, lesson)
            paths.append(path)
    # print(paths)
    return paths


class FileNamingConvention(unittest.TestCase):
    @parameterized.expand(get_module_paths())
    def test_module_numbered(self, module_path):
        try:
            assert module_path.split("/")[-1].split(".")[0].isdigit()
        except:
            raise NameError(f"Module not numbered ({module_path})")

    @parameterized.expand(get_lesson_paths())
    def test_lesson_numbered(self, lesson_path):
        try:
            assert lesson_path.split("/")[-1].split(".")[0].isdigit()
        except:
            raise NameError(f"Lesson not numbered ({lesson_path})")


class MissingMetaDataFiles(unittest.TestCase):
    @parameterized.expand(get_lesson_paths())
    def test_missing_lesson_meta_file(self, path):
        files = os.listdir(path)
        try:
            assert ".lesson.yaml" in files
        except:
            raise FileNotFoundError(
                "Lesson meta file (`.lesson.yaml`) not found in {path}"
            )

    @parameterized.expand(get_module_paths())
    def test_missing_module_meta_file(self, module_path):
        files = os.listdir(module_path)
        try:
            assert ".module.yaml" in files
        except:
            raise FileNotFoundError(
                f"Module meta file (`.module.yaml`) not found in {module_path}"
            )

    def test_missing_unit_meta_file(self):
        files = os.listdir()
        try:
            assert ".unit.yaml" in files
        except:
            raise FileNotFoundError(
                "Unit meta file (`.unit.yaml`) not found in repository root"
            )


class FileContent(unittest.TestCase):
    @skipIf(
        testFails(MissingMetaDataFiles().test_missing_unit_meta_file),
        "Test skipped as `.unit.yaml` not found",
    )
    def test_unit_meta_content(self):
        with open(".unit.yaml") as f:
            unit_meta = yaml.safe_load(f)

        try:
            assert type(unit_meta) == dict
        except:
            raise AssertionError(".unit.yaml is not a dict")

        try:
            assert "description" in unit_meta
        except:
            raise AssertionError("'description' key not found in .unit.yaml")


class MissingLessonContent(unittest.TestCase):
    # @parameterized.expand(get_lesson_paths())
    # def test_missing_quiz(self, lesson_path):
    #     files = os.listdir(lesson_path)
    #     try:
    #         assert ".quiz.yaml" in files
    #     except:
    #         raise FileNotFoundError('Quiz file not found')

    @parameterized.expand(get_lesson_paths())
    def test_missing_challenges(self, lesson_path):
        files = os.listdir(lesson_path)
        try:
            assert ".challenges.yaml" in files
        except:
            raise FileNotFoundError(
                f"Challenges file (`.challenges.yaml`) not found in {lesson_path}"
            )

    @parameterized.expand(get_lesson_paths())
    def test_missing_lesson(self, lesson_path):
        files = os.listdir(lesson_path)
        try:
            assert "Lesson.ipynb" in files
        except:
            raise FileNotFoundError(
                f"Lesson notebook (`Lesson.ipynb`) not found in {lesson_path}"
            )


unittest.main(verbosity=2, exit=True)
