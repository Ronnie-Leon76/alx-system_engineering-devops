#!/usr/bin/env ruby
# Regular expression matching htn or hbtn
puts ARGV[0].scan(/hbt{2,5}n/).join
