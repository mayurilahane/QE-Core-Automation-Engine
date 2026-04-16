# task 1 
status_codes = [200, 404, 500, 200, 201, 403]
success_codes = []
for code in status_codes:
    if code == 200:
        success_codes.append(code)


# Your turn: Try to write the comprehension version of this!
#success_codes = [code for code in status_codes if code == 200]

# task 2
ui_prices = ["$10", "$50", "$99"]
clean_prices = []
for price in ui_prices:
    clean_prices.append(price.replace("$", "")) # No 'if' condition needed here!

# clean_prices = [price.replace("$", "") for price in ui_prices]

# task 3
test_results = ["login: PASS", "checkout: FAIL", "cart: PASS", "logout: FAIL"]
failed_tests = []
for test in test_results:
    if "FAIL" in test:
        failed_tests.append(test)

# failed_tests = [test for test in test_results if "FAIL" in test] 
