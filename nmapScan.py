#!/usr/bin/python

import nmap
import argparse

def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)

    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print("[*] " + tgtHost + " tcp/" + tgtPort + " " + state)

def main():
    parser = argparse.ArgumentParser(description='nmapScan powerd by python')

    parser.add_argument('-H', metavar='host', help='specify target host')

    parser.add_argument('-P', metavar='ports', help='specify target port[s] separated by comma')

    args = parser.parse_args()

    tgtHost = args.H
    tgtPorts = str(args.P).split(',')

    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)

if __name__ == '__main__':
    main()
