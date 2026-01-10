import sys
import os

# Add project root to path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game_data import data
from higher_lower_game import get_random_entry, format_entry


class TestGameData:
    def test_data_is_not_empty(self):
        """Data list should not be empty"""
        assert len(data) > 0

    def test_data_entry_has_required_fields(self):
        """Each entry should have name, follower_count, description, and country"""
        required_fields = ['name', 'follower_count', 'description', 'country']
        for entry in data:
            for field in required_fields:
                assert field in entry

    def test_follower_count_is_integer(self):
        """Follower count should be an integer"""
        for entry in data:
            assert isinstance(entry['follower_count'], int)

    def test_follower_count_is_positive(self):
        """Follower count should be positive"""
        for entry in data:
            assert entry['follower_count'] > 0


class TestGetRandomEntry:
    def test_get_random_entry_returns_valid_entry(self):
        """get_random_entry should return an entry from data"""
        entry = get_random_entry()
        assert entry in data

    def test_get_random_entry_returns_dict(self):
        """get_random_entry should return a dictionary"""
        entry = get_random_entry()
        assert isinstance(entry, dict)

    def test_get_random_entry_excludes_entry(self):
        """get_random_entry should exclude specified entry"""
        exclude_entry = data[0]
        for _ in range(50):  # Run multiple times to increase confidence
            entry = get_random_entry(exclude=exclude_entry)
            assert entry != exclude_entry

    def test_get_random_entry_has_required_fields(self):
        """Returned entry should have all required fields"""
        entry = get_random_entry()
        assert 'name' in entry
        assert 'follower_count' in entry
        assert 'description' in entry
        assert 'country' in entry


class TestFormatEntry:
    def test_format_entry_contains_label(self):
        """Formatted string should contain the label"""
        entry = {'name': 'Test', 'description': 'Test desc', 'country': 'USA', 'follower_count': 100}
        result = format_entry("A", entry)
        assert "Compare A:" in result

    def test_format_entry_contains_name(self):
        """Formatted string should contain the name"""
        entry = {'name': 'Test Name', 'description': 'Test desc', 'country': 'USA', 'follower_count': 100}
        result = format_entry("A", entry)
        assert "Test Name" in result

    def test_format_entry_contains_description(self):
        """Formatted string should contain the description"""
        entry = {'name': 'Test', 'description': 'Famous person', 'country': 'USA', 'follower_count': 100}
        result = format_entry("A", entry)
        assert "Famous person" in result

    def test_format_entry_contains_country(self):
        """Formatted string should contain the country"""
        entry = {'name': 'Test', 'description': 'Test desc', 'country': 'Canada', 'follower_count': 100}
        result = format_entry("A", entry)
        assert "Canada" in result

    def test_format_entry_correct_format(self):
        """Formatted string should match expected format"""
        entry = {'name': 'Instagram', 'description': 'Social media platform', 'country': 'United States', 'follower_count': 346}
        result = format_entry("A", entry)
        expected = "Compare A: Instagram, a Social media platform, from United States"
        assert result == expected

    def test_format_entry_label_b(self):
        """Format should work with label B"""
        entry = {'name': 'Test', 'description': 'Desc', 'country': 'UK', 'follower_count': 50}
        result = format_entry("B", entry)
        assert "Compare B:" in result
