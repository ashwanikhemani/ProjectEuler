# -*- coding: utf-8 -*-
"""

@author: ashwa
"""

import minimalNetwork as minNet

def test_create_network():
    """ Test driver_score is calculated correctly """

    network = minNet.Network(7)
    test_file = "test_input.txt"
    network.createNetwork(test_file)

    exp_initialCost = 243

    actual_initial_cost = network.initialCost
    
    assert actual_initial_cost == exp_initialCost


def test_reduce_network():
    """ Test driver_score is calculated correctly """
    network = minNet.Network(7)
    test_file = "test_input.txt"
    network.createNetwork(test_file)
    exp_savings = 150
    
    network.reduceNetwork()
    
    actual_savings = network.savings
    
    assert actual_savings == exp_savings


#def main():
#
#    test_create_network()
#    
#    test_reduce_network()
#
