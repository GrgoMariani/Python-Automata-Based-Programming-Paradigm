class COMPARISONS:

    @staticmethod
    def less_than(num):
        return lambda x: x < num

    @staticmethod
    def between(num1, num2):
        return lambda x: num1 <= x <= num2

    @staticmethod
    def more_than(num):
        return lambda x: x > num

    @staticmethod
    def equal(num):
        return lambda x: x == num

    @staticmethod
    def not_equal(num):
        return lambda x: x != num

    @staticmethod
    def contains(string: str):
        return lambda x: x.count(string) > 0

    @staticmethod
    def one_of(items: str):
        return lambda x: x in items

    @staticmethod
    def none_of(items: str):
        return lambda x: x not in items

    @staticmethod
    def always_true():
        return lambda x: True

    @staticmethod
    def on_result_true():
        return lambda x: x

    @staticmethod
    def on_result_false():
        return lambda x: not x
