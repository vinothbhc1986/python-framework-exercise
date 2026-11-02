"""Pytest Fixtures."""

def find_average(nums: list[int]) -> float:
    """Calculate the average."""
    return sum(nums) / len(nums)

def find_biggest(nums: list[int]) -> int:
    """Return the biggest number"""
    return max(nums)

def find_smallest(nums: list[int]) -> int:
    """Return the smallest number"""
    return min(nums)