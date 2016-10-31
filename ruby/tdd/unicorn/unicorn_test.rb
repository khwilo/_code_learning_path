# Use the minitest gem version installed in your system
gem 'minitest', '~> 5.8'

# load gem
require 'minitest/autorun'

# add pretty colors in the terminal when your run the tests
require 'minitest/pride'

# create a new test suite
class UnicornTest < Minitest::Test
	# add a test by adding a method whose name starts with test
	def test_something
		assert_equal 2, 1 + 1
	end

	def test_something_else
		assert_equal 1, 2 - 1
	end

	def test_yet_another_thing
	end
end

