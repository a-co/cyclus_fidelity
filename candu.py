# candu.py
# cyclus sample file for a candu reactor

simulation = {"simulation": {
    "control": {
            'duration': '144', #duration of simulation (months)
            'dt': '86400', #time step, seconds
            'startmonth': '1',
            'startyear': '2020',
            'decay': 'never',
            'explicit_inventory': 'true'
            },
    "archetypes": {
        'spec': [{'lib': 'cycamore', 'name': 'Source'},
                {'lib': 'cycamore', 'name': 'Reactor'},
                {'lib': 'cycamore', 'name': 'Sink'},
                {'lib': 'agents', 'name': 'NullInst'},
                {'lib': 'agents', 'name': 'NullRegion'}
                ]
        },
    "facility": [{'name': 'Source', 'config':
                    {'Source': {'outcommod': 'c_uore',
                                'outrecipe': 'r_nat_u',
                                'throughput': '1e6'}}
                    },
                {'name': 'Reactor', 'config':
                    {'Reactor': {'fuel_incommods': {'val': 'c_uore'},
                        'fuel_inrecipes': {'val': 'r_nat_u'},
                        'fuel_outcommods': {'val': 'c_spent_fuel'},
                        'fuel_outrecipes': {'val': 'r_leu_spent'},
                        'cycle_time': '18',
                        'refuel_time': '1',
                        'assem_size': '3300',
                        'n_assem_core': '3',
                        'n_assem_batch': '1',
                        'power_cap': '1000'}}
                    },
                {'name': 'Sink', 'config':
                    {'Sink': {'in_commods': {'val':'c_spent_fuel'}}}}],

    "region": {
        'name': 'null_region',
        'config': {'NullRegion': None},
        "institution": [
                {"config": {"NullInst": None},
                "initialfacilitylist": {
                    "entry": [{'number': 1, 'prototype': 'Source'},
                             {'number': 1, 'prototype': 'Reactor'},
                             {'number': 1, 'prototype': 'Sink'}]
                        },
                    "name": "null_inst",
                    },
                ],
        },
    "recipe":  [{'name': 'r_nat_u', 'basis': 'mass',
                'nuclide': [{'id': '92235', 'comp': '0.00711'},
                            {'id': '92238', 'comp': '0.99289'}]},
                {'name': 'r_leu_spent', 'basis': 'mass',
                'nuclide': [{'id': '92235', 'comp': '0.01'},
                            {'id': '92238', 'comp': '0.94'},
                            {'id': '94239', 'comp': '0.01'},
                            {'id': '55135', 'comp': '0.3'}]}
                ]
    }
}
