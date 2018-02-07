#!/usr/bin/env python


class MyValues(object):
    def __init__(self, pcap_sequence_number, timestamp):
        self.pcap_sequence_number = pcap_sequence_number
        self.timestamp = timestamp


def main():
    input_file = 'duplicate_packets_check.out'
    packets_database = dict()
    with open(input_file, 'r') as packets_file:
        for line in packets_file:
            current_record = line.split()
            current_pcap_sequence_number = current_record[0]
            current_timestamp = float(current_record[1])
            my_values = MyValues(current_pcap_sequence_number,
                                 current_timestamp)
            key = str(current_record[2:])
            if key in packets_database:
                previous_myvalue = packets_database[key]
                pcap_sequence_number = previous_myvalue.pcap_sequence_number
                previous_timestamp = previous_myvalue.timestamp
                if current_timestamp - previous_timestamp < 2.0:
                    print('Found duplicates: '
                          'key = "%s", '
                          'previous pcap_sequence_number = %s, '
                          'previous timestamp = %.9f, '
                          'current record = "%s", '
                          'current timestamp = %.9f' %
                          (key, pcap_sequence_number, previous_timestamp,
                           current_record, current_timestamp))
            packets_database[key] = my_values


if __name__ == "__main__":
    main()
