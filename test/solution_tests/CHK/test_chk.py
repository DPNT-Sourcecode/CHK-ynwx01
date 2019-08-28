from solutions.CHK import checkout_solution


class TestCheckout(object):
    def test_checkout(self):
        assert checkout_solution.checkout('ACCAABBAAAACCD') == 440
        assert checkout_solution.checkout('AAAAAAAAAA') == 400
        assert checkout_solution.checkout('AAAAAAAAAAA') == 450
        assert checkout_solution.checkout('AAAAAAAAAAAA') == 500
        assert checkout_solution.checkout('AAAAAAAAAAAAA') == 530
        assert checkout_solution.checkout('AAAAAAAAAAAAAA') == 580
        assert checkout_solution.checkout('BCB') == 65
        assert checkout_solution.checkout('ECBE') == 100
        assert checkout_solution.checkout('ECBEBBE') == 185

    def test_valid_skus(self):
        assert checkout_solution.checkout('ABBBFBBBCCC') == -1
        assert checkout_solution.checkout('A0B') == -1
        assert checkout_solution.checkout(0) == -1
