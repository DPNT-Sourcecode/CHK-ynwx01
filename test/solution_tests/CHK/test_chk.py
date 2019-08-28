from solutions.CHK import checkout_solution


class TestCheckout(object):
    def test_checkout(self):
        assert checkout_solution.checkout('ACCAABAAAACCD') == 435
        assert checkout_solution.checkout('AAAAAAAAAA') == 440
        assert checkout_solution.checkout('BCB') == 110

    def test_valid_skus(self):
        assert checkout_solution.checkout('ABBBEBBBCCC') == -1
        assert checkout_solution.checkout('A0B') == -1
        assert checkout_solution.checkout(0) == -1

