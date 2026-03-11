import unittest
import questions


class TestQuestions(unittest.TestCase):

# ----- SUM TYPE QUESTIONS -----

    def test_daily_sales(self):
        self.assertEqual(questions.daily_sales([12,8,5,10]), 35)

    def test_total_goals(self):
        self.assertEqual(questions.total_goals([2,3,1,4]), 10)

    def test_class_attendance(self):
        self.assertEqual(questions.class_attendance([25,24,26,23]), 98)

    def test_total_distance(self):
        self.assertEqual(questions.total_distance([5,3,6,4]), 18)

    def test_warehouse_items(self):
        self.assertEqual(questions.warehouse_items([20,15,30]), 65)

# ----- DISCOUNT TYPE QUESTIONS -----

    def test_half_price(self):
        self.assertEqual(
            questions.half_price([80,120,200]),
            ["R 40","R 60","R 100"]
        )

    def test_student_discount(self):
        self.assertEqual(
            questions.student_discount([60,100,40]),
            ["R 30","R 50","R 20"]
        )

    def test_movie_special(self):
        self.assertEqual(
            questions.movie_special([20,30,50]),
            ["R 10","R 15","R 25"]
        )

    def test_gym_promo(self):
        self.assertEqual(
            questions.gym_promo([500,800]),
            ["R 250","R 400"]
        )

    def test_tech_sale(self):
        self.assertEqual(
            questions.tech_sale([1000,600,200]),
            ["R 500","R 300","R 100"]
        )


if __name__ == "__main__":
    unittest.main()