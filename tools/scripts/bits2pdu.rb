#!/usr/bin/env ruby
#
# Reassembles a packet from the incoming bitstream.

bits = ARGF.gets
first1 = bits.index('1')
bits = bits[(first1-7)..-2]

bits.each_char.each_slice(8) do |s|
    print "" + s.join.to_i(2).to_s(16).rjust(2, '0')
end
puts

