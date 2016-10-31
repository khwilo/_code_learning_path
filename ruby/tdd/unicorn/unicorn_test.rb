# Use the minitest gem version installed in your system
gem 'minitest', '~> 5.8'

# load gem
require 'minitest/autorun'

# add pretty colors in the terminal when your run the tests
require 'minitest/pride'

# require the unicorn file
require_relative 'unicorn'


# create a new test suite
class UnicornTest < Minitest::Test
	def test_it_has_a_name
		# create a new unicorn
		unicorn = Unicorn.new("Robert")

		# make an assertion
		assert_equal "Robert", unicorn.name
	end
end

