#!/usr/bin/env python

"""
Usage: {} <packets file> [minimum time distance in seconds]

Print out duplicates found in packets file.
The default minimum time distance for duplicates is {} seconds (it can be set
to any value, it will be precise for 28 places).
"""

from decimal import Decimal
import os
import sys

DEFAULT_MINIMUM_TIME_DELTA = 2.0


class PacketRecord(object):
    def __init__(self, line):
        self.full_record = line.split()
        # first column, the pcap sequence number is ignored
        self.timestamp = Decimal(self.full_record[1])
        self.key = str(self.full_record[2:])


def main():
    (input_file, minimum_time_delta) = check_arguments()
    find_duplicates(input_file, minimum_time_delta)


def check_arguments():
    argv_length = len(sys.argv)
    if argv_length < 2 or argv_length > 3:
        print(globals()['__doc__'].format(os.path.basename(sys.argv[0]),
                                          DEFAULT_MINIMUM_TIME_DELTA))
        sys.exit(1)

    input_file = sys.argv[1]
    minimum_time_delta = Decimal(DEFAULT_MINIMUM_TIME_DELTA)
    if argv_length == 3:
        minimum_time_delta = Decimal(sys.argv[2])
    return (input_file, minimum_time_delta)


def find_duplicates(input_file, minimum_time_delta):
    packets_database = dict()
    with open(input_file, 'r') as packets_file:
        for line in packets_file:
            record = PacketRecord(line)
            check_record_in_database(record, packets_database,
                                     minimum_time_delta)
            packets_database[record.key] = record


def check_record_in_database(record, packets_database, minimum_time_delta):
    key = record.key
    current_timestamp = record.timestamp
    if key in packets_database:
        previous_timestamp = packets_database[key].timestamp
        if current_timestamp - previous_timestamp < minimum_time_delta:
            print('Found duplicates: previous record = {}, current record = {}'
                  .format(packets_database[key].full_record,
                          record.full_record))


if __name__ == '__main__':
    main()
