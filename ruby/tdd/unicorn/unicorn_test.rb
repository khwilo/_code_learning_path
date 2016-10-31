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
	# this test makes all unicorns to be called Robert
	def test_it_has_a_name
		# create a new unicorn
		unicorn = Unicorn.new("Robert")

		# make an assertion
		assert_equal "Robert", unicorn.name
	end

	# this test triangulates the behaviour we want / expect
	def test_it_can_be_named_somethig_else
		unicorn = Unicorn.new("Joseph")
		assert_equal "Joseph", unicorn.name
	end
end

