#!/usr/bin/env ruby

puts ARGV[0].scan(/([^,]+),([^,]+),(.+)/).map { |match| "[#{match.join(',')}]" }.join
