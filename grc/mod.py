#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Mod
# Generated: Sun Jan 29 20:30:14 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx


class mod(grc_wxgui.top_block_gui):

    def __init__(self, infile=""):
        grc_wxgui.top_block_gui.__init__(self, title="Mod")

        ##################################################
        # Parameters
        ##################################################
        self.infile = infile

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.offset = offset = 220e3
        self.key_freq = key_freq = 433.92e6

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0_0.win)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(key_freq - offset, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(15, 0)
        self.osmosdr_sink_0.set_if_gain(47, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, infile, False)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, key_freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_uchar_to_float_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.osmosdr_sink_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.wxgui_scopesink2_0_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_multiply_xx_0, 0))    

    def get_infile(self):
        return self.infile

    def set_infile(self, infile):
        self.infile = infile
        self.blocks_file_source_0.open(self.infile, False)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0_0.set_sample_rate(self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self.osmosdr_sink_0.set_center_freq(self.key_freq - self.offset, 0)

    def get_key_freq(self):
        return self.key_freq

    def set_key_freq(self, key_freq):
        self.key_freq = key_freq
        self.osmosdr_sink_0.set_center_freq(self.key_freq - self.offset, 0)
        self.analog_sig_source_x_0.set_frequency(self.key_freq)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--infile", dest="infile", type="string", default="",
        help="Set infile [default=%default]")
    return parser


def main(top_block_cls=mod, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(infile=options.infile)
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
