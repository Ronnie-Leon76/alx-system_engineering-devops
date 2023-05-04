#!/usr/bin/env ruby
# Regular expression that matches hbt{1,5}?n
puts ARGV[0].scan(/hbt*n/).join
