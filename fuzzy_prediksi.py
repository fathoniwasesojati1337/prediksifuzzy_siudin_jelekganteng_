# -*- coding: utf-8 -*-

pip install -U scikit-fuzzy

import skfuzzy as fuzzy

from skfuzzy import control as system

import numpy as np

tinggi_badan = system.Antecedent(np.arange(0,200,0.1), 'tinggi_badan')

tinggi_badan.universe

berat_badan = system.Antecedent(np.arange(0,100,0.1), 'berat_badan')

performace = system.Consequent(np.arange(0,100,1), 'performance')

""" membership function """

tinggi_badan['pendek'] = fuzzy.trapmf(tinggi_badan.universe, [0,0,120,140])

tinggi_badan['sedang'] = fuzzy.trimf(tinggi_badan.universe, [120,140,170])

tinggi_badan['tinggi'] = fuzzy.trapmf(tinggi_badan.universe, [140,170,200,200])

tinggi_badan.view()

berat_badan['ringan'] = fuzzy.trapmf(berat_badan.universe, [0,0,45,50])

berat_badan['lumayan'] = fuzzy.trimf(berat_badan.universe, [45,55,65])

berat_badan['berat_banget'] = fuzzy.trapmf(berat_badan.universe, [60,70,100,100])

berat_badan.view()

performace['jelek'] = fuzzy.trapmf(performace.universe, [0,0,25,75])

performace['ganteng'] = fuzzy.trapmf(performace.universe, [25,75,100,100])

performace.view()

""" rules """

rules1 = system.Rule(tinggi_badan['tinggi'] & berat_badan['berat_banget'], performace['ganteng'])
rules1.view()

rules2 = system.Rule(tinggi_badan['tinggi'] & berat_badan['berat_banget'], performace['ganteng'])
rules3 = system.Rule(tinggi_badan['sedang'] & berat_badan['berat_banget'], performace['ganteng'])
rules4 = system.Rule(tinggi_badan['sedang'] & berat_badan['ringan'], performace['jelek'])
rules5 = system.Rule(tinggi_badan['pendek'] & berat_badan['berat_banget'], performace['jelek'])
rules6 = system.Rule(tinggi_badan['pendek'] & berat_badan['ringan'], performace['jelek'])

""" input decision (keputusan)"""

performace_control_udin = system.ControlSystem([rules1,rules2,rules3,rules4,rules5,rules6])
performace_control_udin.view()

performacepointsimulasi = system.ControlSystemSimulation(performace_control_udin)

performacepointsimulasi.input['berat_badan'] = 40
performacepointsimulasi.input['tinggi_badan'] = 110

performacepointsimulasi.compute()

performace.view(sim=performacepointsimulasi)
print("performance si udin : ", performacepointsimulasi.output['performance'])
