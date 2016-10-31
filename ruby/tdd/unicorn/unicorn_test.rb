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

	def test_it_is_white_by_default
		unicorn = Unicorn.new("Margaret")
		assert_equal "white", unicorn.color
	end

	def test_it_knows_if_it_is_white
		unicorn = Unicorn.new("Gift")
		# assert_equal true, unicorn.white?
		assert unicorn.white?, "Gift should be white, but it isn't"
	end

	def test_it_does_not_have_to_be_white
		unicorn = Unicorn.new("Barbara", "purple")
		assert_equal "purple", unicorn.color
	end
end

