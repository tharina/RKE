#!/usr/bin/env ruby
#
# Decodes a manchester encoded bitstream.

ARGF.each_char.each_slice 2 do |b1, b2|
    if b1 and b2
        if b1 + b2 == '01'
            print '0'
        elsif b1 + b2 == '10'
            print '1'
        elsif b1 + b2 == '11'
            exit
            #print '_'
        else
            print "\nError\n"
        end
    end
end
puts
