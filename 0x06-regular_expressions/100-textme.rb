#!/usr/bin/env ruby
puts ARGV[0].scan(/([^,]+),([^,]+),(.+)/).map { |m| "[#{m.join(',')}]" }.join
