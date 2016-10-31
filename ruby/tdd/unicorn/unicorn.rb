class Unicorn
	def initialize(name)
		# save the name in @name
		@name = name
	end

	def name
		# return the instance variable from the initialize method
		@name
	end

	def color
		"white"
	end

	def white?
		true
	end
end
