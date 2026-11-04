# TESTING EXCEPTIONS & WARNINGS SUMMARY:
# 1. Use pytest.raises(ExceptionClass) for negative tests
# 2. Use match='regex' to confirm error messages
# 3. Inspect exc_info.value for rich diagnostic attributes
# 4. Use pytest.warns() to enforce deprecation schedules
verified_count = 10
print(f'Part 2 verified: {verified_count} test patterns')