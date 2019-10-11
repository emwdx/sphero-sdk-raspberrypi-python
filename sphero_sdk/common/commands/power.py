#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x13-power.json
# Device ID:          0x13
# Device Name:        power
# Timestamp:          10/10/2019 @ 21:40:31.379259 (UTC)

from sphero_sdk.common.enums.power_enums import CommandsEnum
from sphero_sdk.common.devices import DevicesEnum
from sphero_sdk.common.parameter import Parameter
from sphero_sdk.common.sequence_number_generator import SequenceNumberGenerator


def sleep(target, timeout): 
    return { 
        'did': DevicesEnum.power,
        'cid': CommandsEnum.sleep,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def wake(target, timeout): 
    return { 
        'did': DevicesEnum.power,
        'cid': CommandsEnum.wake,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def get_battery_percentage(target, timeout): 
    return { 
        'did': DevicesEnum.power,
        'cid': CommandsEnum.get_battery_percentage,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='percentage',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ]
    }


def get_battery_voltage_state(target, timeout): 
    return { 
        'did': DevicesEnum.power,
        'cid': CommandsEnum.get_battery_voltage_state,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='state',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ]
    }


def on_will_sleep_notify(target, timeout): 
    return { 
        'did': DevicesEnum.power,
        'cid': CommandsEnum.will_sleep_notify,
        'target': target,
        'timeout': timeout,
    }


def on_did_sleep_notify(target, timeout): 
    return { 
        'did': DevicesEnum.power,
        'cid': CommandsEnum.did_sleep_notify,
        'target': target,
        'timeout': timeout,
    }


def enable_battery_voltage_state_change_notify(is_enabled, target, timeout): 
    return { 
        'did': DevicesEnum.power,
        'cid': CommandsEnum.enable_battery_voltage_state_change_notify,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='isEnabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
        ],
    }


def on_battery_voltage_state_change_notify(target, timeout): 
    return { 
        'did': DevicesEnum.power,
        'cid': CommandsEnum.battery_voltage_state_change_notify,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='state',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ]
    }


def get_battery_voltage_in_volts(reading_type, target, timeout): 
    return { 
        'did': DevicesEnum.power,
        'cid': CommandsEnum.get_battery_voltage_in_volts,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='readingType',
                data_type='uint8_t',
                index=0,
                value=reading_type,
                size=1
            ),
        ],
        'outputs': [ 
            Parameter( 
                name='voltage',
                data_type='float',
                index=0,
                size=1,
            ),
        ]
    }


def get_battery_voltage_state_thresholds(target, timeout): 
    return { 
        'did': DevicesEnum.power,
        'cid': CommandsEnum.get_battery_voltage_state_thresholds,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='criticalThreshold',
                data_type='float',
                index=0,
                size=1,
            ),
            Parameter( 
                name='lowThreshold',
                data_type='float',
                index=1,
                size=1,
            ),
            Parameter( 
                name='hysteresis',
                data_type='float',
                index=2,
                size=1,
            ),
        ]
    }


def get_current_sense_amplifier_current(amplifier_id, target, timeout): 
    return { 
        'did': DevicesEnum.power,
        'cid': CommandsEnum.get_current_sense_amplifier_current,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='amplifierId',
                data_type='uint8_t',
                index=0,
                value=amplifier_id,
                size=1
            ),
        ],
        'outputs': [ 
            Parameter( 
                name='amplifierCurrent',
                data_type='float',
                index=0,
                size=1,
            ),
        ]
    }
