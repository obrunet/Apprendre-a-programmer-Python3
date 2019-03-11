class Domino(object):
    "Domino Class definition"

    def __init__(self, face_a, face_b):
        "method instance initialization"
        self.face_a = face_a
        self.face_b = face_b

    def display_domino(self):
        "method displaying the domino faces"
        print("face A = {} and face B = {}".format(self.face_a, self.face_b))

    def sum_values(self):
        "method that retrun the sum of the values on each faces of the domino"
        return self.face_a + self.face_b


if __name__ == "__main__":
    d1 = Domino(2, 6)
    d2 = Domino(4, 5)
    Domino.display_domino(d1)
    Domino.display_domino(d2)
    print("Sum of values' faces for d1: ", Domino.sum_values(d1))
    print("Sum of values' faces for d2: ", Domino.sum_values(d2))
    