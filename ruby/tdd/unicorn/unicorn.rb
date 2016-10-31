class Unicorn
	attr_reader :name

	def initialize(name, color="white")
		# save the name in @name
		@name = name
		@color = color
	end

	def name
		# return the instance variable from the initialize method
		@name
	end

	def color
		@color
	end

	def white?
		color == "white"
	end

	def say(something)
		"**;* #{something} **;*"
	end
end
