#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Demod
# Generated: Sun Jan 29 20:12:50 2017
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class demod(gr.top_block):

    def __init__(self, infile="", outfile=""):
        gr.top_block.__init__(self, "Demod")

        ##################################################
        # Parameters
        ##################################################
        self.infile = infile
        self.outfile = outfile

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.offset = offset = 220e3
        self.key_freq = key_freq = 433.92e6

        ##################################################
        # Blocks
        ##################################################
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((10000, ))
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_gr_complex*1, infile, False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, outfile, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_add_const_vxx_1 = blocks.add_const_vff((-0.5, ))
        self.band_pass_filter_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	100, samp_rate, 220e3, 270e3, 50e3, firdes.WIN_HAMMING, 6.76))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_add_const_vxx_1, 0))    
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.digital_binary_slicer_fb_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.band_pass_filter_0, 0))    
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_file_sink_0, 0))    

    def get_infile(self):
        return self.infile

    def set_infile(self, infile):
        self.infile = infile
        self.blocks_file_source_0_0.open(self.infile, False)

    def get_outfile(self):
        return self.outfile

    def set_outfile(self, outfile):
        self.outfile = outfile
        self.blocks_file_sink_0.open(self.outfile)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(100, self.samp_rate, 220e3, 270e3, 50e3, firdes.WIN_HAMMING, 6.76))

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset

    def get_key_freq(self):
        return self.key_freq

    def set_key_freq(self, key_freq):
        self.key_freq = key_freq


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--infile", dest="infile", type="string", default="",
        help="Set infile [default=%default]")
    parser.add_option(
        "", "--outfile", dest="outfile", type="string", default="",
        help="Set outfile [default=%default]")
    return parser


def main(top_block_cls=demod, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(infile=options.infile, outfile=options.outfile)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
