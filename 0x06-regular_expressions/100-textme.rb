#!/usr/bin/env ruby
# Regular expression that outputs [SENDER], [RECEIVER], [FLAGS]
puts ARGV[0].scan(\[from:(.*?)\] \[to:(.*?)] \[flags:(.*?)\]).join
