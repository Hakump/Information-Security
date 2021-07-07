import dpkt
from dpkt.ip import IP, IP_PROTO_UDP
from dpkt.udp import UDP
from dpkt.tcp import TCP
from dpkt.compat import compat_ord
import sys
import socket


def mac_addr(addr):
    return ':'.join('%02x' % compat_ord(b) for b in addr)


arg = sys.argv[1]
file = open(arg, "rb")

mac = ["7c:d1:c3:94:9e:b8", "d8:96:95:01:a5:c9", "f8:1a:67:cd:57:6e"]

ip = ["192.168.0.100", "192.168.0.103", "192.168.0.1"]

counts_port = [set([]), set([]), set([])]
counts_packet = [[], [], []]
ip2 = ["192.168.0.100", "192.168.0.101"]

list_ports = {}

packets = dpkt.pcap.Reader(file)
count = -1

for ts, buf in packets:
    count += 1
    eth = dpkt.ethernet.Ethernet(buf)
    if eth.type == dpkt.ethernet.ETH_TYPE_ARP:
        arp = eth.data
        if arp.op == dpkt.arp.ARP_OP_REPLY:
            for i in range(0, 3):
                if mac_addr(arp.sha) == mac[i] and socket.inet_ntoa(arp.spa) != ip[i]:
                    print("ARP spoofing!")
                    print("Src MAC: " + mac[i])
                    print("Dst MAC: " + socket.inet_ntoa(arp.tpa))
                    print("Packet number: " + str(count))
                    break

    if eth.type == dpkt.ethernet.ETH_TYPE_IP:
        ipp = eth.data
        if (ipp.p == dpkt.ip.IP_PROTO_TCP and ipp.data.flags & dpkt.tcp.TH_SYN) or ipp.p == dpkt.ip.IP_PROTO_UDP:
            tcp = ipp.data
            port = tcp.dport
            for i in range(2):
                if ip2[i] == socket.inet_ntoa(ipp.dst):
                    if port not in counts_port[i]:
                        counts_port[i].add(port)
                        counts_packet[i].append(count)
                    break
        if ipp.p == dpkt.ip.IP_PROTO_TCP:
            tcp = ipp.data
            port = tcp.dport
            key = socket.inet_ntoa(ipp.dst) + " " + str(port)
            if key in list_ports:
                templist = list_ports.get(key)
                templist.append([ts, count])
            else:
                list_ports.update({key: [[ts, count]]})

for i in range(len(ip2)):
    if len(counts_port[i]) >= 100:
        print("Port scan!")
        print("Dst IP: " + ip2[i])
        temp = len(counts_packet[i]) - 1
        string = "Packet number: "
        for j in range(temp):
            string += str(counts_packet[i][j]) + ", "
        string += str(counts_packet[i][temp])
        print(string)

file.close()

for key, ports in list_ports.items():
    i = 0
    for j in range(0, len(ports)):
        if ports[j][0] - ports[i][0] <= 1:
            if j - i == 100:
                name = key.split()
                print("SYN floods!")
                print("Dst IP: " + name[0])
                print("Dst Port: "+name[1])
                string = "Packet number: "
                for pos in range(i, j):
                    string += str(ports[pos][1]) + ", "
                string += str(ports[j][1])
                print(string)
                break
        else:
            while ports[j][0] - ports[i][0] > 1:
                i += 1
