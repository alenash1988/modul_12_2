import inspect
import runner_2
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = runner_2.Runner('Усэйн', 10)
        self.runner_2 = runner_2.Runner('Андрей', 9)
        self.runner_3 = runner_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print()
        for i in cls.all_results:
            print()
            print(f'{i}:')
            print({key: str(value) for key, value in cls.all_results[i].items()})

    def test_name(self):
        tour = runner_2.Tournament(90, self.runner_1, self.runner_3)
        result = tour.start()
        self.all_results[inspect.stack()[0][3]] = result
        self.assertTrue('Ник' == result[len(result)].name)

    def test_name_2(self):
        tour = runner_2.Tournament(90, self.runner_2, self.runner_3)
        result = tour.start()
        self.all_results[inspect.stack()[0][3]] = result
        self.assertTrue('Ник' == result[len(result)].name)

    def test_name_3(self):
        tour = runner_2.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tour.start()
        self.all_results[inspect.stack()[0][3]] = result
        self.assertTrue('Ник' == result[len(result)].name)


if __name__ == "__main__":
    unittest.main()