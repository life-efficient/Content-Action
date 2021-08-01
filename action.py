import unittest
import os
from parameterized import parameterized


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
            # print("lesson:", lesson)
            path = os.path.join(module, lesson)
            paths.append(path)
    # print(paths)
    return paths


class MissingContent(unittest.TestCase):
    # @parameterized.expand(get_lesson_paths())
    # def test_missing_quiz(self, lesson_path):
    #     files = os.listdir(lesson_path)
    #     assert ".quiz.yaml" in files

    @parameterized.expand(get_lesson_paths())
    def test_missing_challenges(self, lesson_path):
        files = os.listdir(lesson_path)
        try:
            assert ".challenges.yaml" in files
        except:
            raise FileNotFoundError('Challenges file not found')

    @parameterized.expand(get_lesson_paths())
    def test_missing_lesson(self, lesson_path):
        files = os.listdir(lesson_path)
        try:
            assert "Lesson.ipynb" in files
        except:
            raise FileNotFoundError('Lesson notebook not found')


unittest.main(argv=[""], verbosity=2, exit=True)
