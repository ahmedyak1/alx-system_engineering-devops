#!/usr/bin/env ruby
# This script accepts 1 arg and passes it to a regular expre


puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')

