#!/usr/bin/env python

def main():
    input_file = 'duplicate_packets_check.out'
    packets_database = dict()
    with open(input_file, 'r') as packets_file:
        for line in packets_file:
            current_record = line.split()
            # first (0.) column, the sequence number is ignored
            current_timestamp = float(current_record[1])
            key = str(current_record[2:])
            if key in packets_database:
                previous_timestamp = packets_database[key]
                if current_timestamp - previous_timestamp < 2.0:
                    print('Found duplicates: '
                          'key = "%s", '
                          'previous timestamp = %.9f, '
                          'current record = "%s", '
                          'current timestamp = %.9f' %
                          (key, previous_timestamp,
                           current_record, current_timestamp))
            packets_database[key] = current_timestamp


if __name__ == "__main__":
    main()
