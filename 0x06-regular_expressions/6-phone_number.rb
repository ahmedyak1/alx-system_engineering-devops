#!/usr/bin/env ruby
# Script accepts 1 arg and passe regulat expr

puts ARGV[0].scan(/^\d{10}$/).join

