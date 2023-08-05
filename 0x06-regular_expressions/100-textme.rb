#!/usr/bin/env ruby
# Regular expression that outputs [SENDER], [RECEIVER], [FLAGS]
puts ARGV[0].scan(/(?<=from)\w+/).join
