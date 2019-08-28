from solutions.CHK import checkout_solution


class TestCheckout(object):
    def test_checkout(self):
        # General test
        assert checkout_solution.checkout('ACCAABBAAAACCD') == 440

        # Test A discount
        assert checkout_solution.checkout('AAAAAAAAAA') == 400
        assert checkout_solution.checkout('AAAAAAAAAAA') == 450
        assert checkout_solution.checkout('AAAAAAAAAAAA') == 500
        assert checkout_solution.checkout('AAAAAAAAAAAAA') == 530
        assert checkout_solution.checkout('AAAAAAAAAAAAAA') == 580

        # Test B discount
        assert checkout_solution.checkout('BCB') == 65

        # Test E discount: get 2 for 1 free B
        assert checkout_solution.checkout('ECBE') == 100
        assert checkout_solution.checkout('ECBEBBE') == 185

        # Test F discount, get 2 for 1 free
        assert checkout_solution.checkout('FECBEFBBEF') == 205
        assert checkout_solution.checkout('ECBEBFBEF') == 205
        assert checkout_solution.checkout('ECFBFEBFBEF') == 215
        assert checkout_solution.checkout('FECFBFEBFBEF') == 225
        assert checkout_solution.checkout('FFECFBFEBFBEF') == 225

    def test_valid_skus(self):
        assert checkout_solution.checkout('ABBBGBBBCCC') == -1
        assert checkout_solution.checkout('A0B') == -1
        assert checkout_solution.checkout(0) == -1


