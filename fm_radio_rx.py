#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fm Radio Rx
# Generated: Thu Nov 23 14:51:31 2017
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

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sip
import sys
import time


class fm_radio_rx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Fm Radio Rx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fm Radio Rx")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "fm_radio_rx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.volume_ui = volume_ui = 0
        self.freq_ui = freq_ui = 97.9
        self.volume = volume = volume_ui / 100
        self.sample_rate = sample_rate = 10e6
        self.freq = freq = freq_ui * 1e6
        self.fm_sample = fm_sample = 500e3
        self.audio_rate = audio_rate = 48e3

        ##################################################
        # Blocks
        ##################################################
        self._volume_ui_range = Range(0, 100, 1, 0, 200)
        self._volume_ui_win = RangeWidget(self._volume_ui_range, self.set_volume_ui, 'Volume', "counter_slider", float)
        self.top_layout.addWidget(self._volume_ui_win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=int(audio_rate/1000),
                decimation=int(fm_sample/10000),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	sample_rate, #bw
        	"Signals", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(sample_rate)
        self.osmosdr_source_0.set_center_freq(freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(2, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(int(sample_rate / fm_sample), firdes.low_pass(
        	1, sample_rate, 100e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self._freq_ui_range = Range(88, 108, 0.1, 97.9, 200)
        self._freq_ui_win = RangeWidget(self._freq_ui_range, self.set_freq_ui, 'Frequency', "counter_slider", float)
        self.top_layout.addWidget(self._freq_ui_win)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.audio_sink_0 = audio.sink(int(audio_rate), '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=fm_sample,
        	audio_decimation=10,
        )
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, volume)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fm_radio_rx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_volume_ui(self):
        return self.volume_ui

    def set_volume_ui(self, volume_ui):
        self.volume_ui = volume_ui
        self.set_volume(self.volume_ui / 100)

    def get_freq_ui(self):
        return self.freq_ui

    def set_freq_ui(self, freq_ui):
        self.freq_ui = freq_ui
        self.set_freq(self.freq_ui * 1e6)

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.analog_const_source_x_0.set_offset(self.volume)

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq, self.sample_rate)
        self.osmosdr_source_0.set_sample_rate(self.sample_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.sample_rate, 100e3, 10e3, firdes.WIN_HAMMING, 6.76))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.freq, self.sample_rate)
        self.osmosdr_source_0.set_center_freq(self.freq, 0)

    def get_fm_sample(self):
        return self.fm_sample

    def set_fm_sample(self, fm_sample):
        self.fm_sample = fm_sample

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate


def main(top_block_cls=fm_radio_rx, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
