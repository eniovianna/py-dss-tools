# -*- encoding: utf-8 -*-
"""
 Created by Ênio Viana at 04/09/2021 at 20:37:43
 Project: py_dss_tools [set, 2021]
"""


class Transformer:
    name = "Transformer"
    name_plural = "Transformer"
    columns = ['%imag', '%loadloss', '%noloadloss', '%r', '%rs', 'bank', 'basefreq', 'bus', 'buses', 'conn',
               'conns', 'core', 'emergamps', 'emerghkva', 'enabled', 'faultrate', 'flrise', 'hsrise', 'kv', 'kva',
               'kvas', 'kvs', 'leadlag', 'like', 'm', 'maxtap', 'mintap', 'n', 'normamps', 'normhkva', 'numtaps',
               'pctperm', 'phases', 'ppm_antifloat', 'ratings', 'rdcohms', 'repair', 'rneut', 'seasons', 'sub',
               'subname', 'tap', 'taps', 'thermal', 'wdg', 'wdgcurrents', 'windings', 'x12', 'x13', 'x23',
               'xfmrcode', 'xhl', 'xht', 'xlt', 'xneut', 'xrconst', 'xscarray']

    def __init__(self):
        self.name = f"My_Transformer_{Transformer.id}"
        self.id = Transformer.id
        Transformer.id = Transformer.id + 1

    @property
    def name_(self):
        return self.name

    @name_.setter
    def name_(self, value: str):
        self.name_ = str(value)

    @staticmethod
    def new(self, **kwargs):
        value = str
        if '_name' in kwargs:
            self.name_ = kwargs.get('_name')
        # circuit.dss.text(
        #     f"New Transformer.{self.name_} phases=3 windings=2 buses=(684, 680) Conns=(Wye, Wye) kVs=(4.16,4.16) "
        #     "kVAs=(5000, 5000) %loadloss=2 xhl=4")

    def __str__(self):
        print(f"{str(self.id)} - {self.name}")
