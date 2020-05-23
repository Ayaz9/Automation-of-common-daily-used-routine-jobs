
# pyshark module is used to parse pcap file
import pyshark, datetime

protocol_input = "udp".lower()  # same for tcp (tcp.islower())
cap_packet_num_list = []
cap_2_packet_num_list = []
cap_packet_id_list = []
cap_packet_id_list.sort()
cap_2_packet_id_list = []
cap_2_packet_id_list.sort()


src_to_dst_missed_packet_id = []
dst_to_src_missed_packet_id = []


# in below, you can always put your specific IP add, ports, pcaps

if protocol_input == "udp":
    cap = pyshark.FileCapture("src.pcapng", display_filter="ip.src== 192.168.0.10 and udp.srcport==57835 and ip.dst==144.254.221.39 and udp.dstport==443")  # put here source pcap name instead of "teams-filtered.pcapng"
    cap_2 = pyshark.FileCapture("src.pcapng", display_filter="ip.src== 192.168.0.10 and udp.srcport==57835 and ip.dst==144.254.221.39 and udp.dstport==443") # the same here but dst pcap name
elif protocol_input == "tcp":
    cap = pyshark.FileCapture("src.pcapng", display_filter="ip.src== 192.168.0.10 and tcp.srcport==61106 and ip.dst==144.254.221.39 and tcp.dstport==443")  # put here source pcap name instead of "teams-filtered.pcapng"
    cap_2 = pyshark.FileCapture("src.pcapng", display_filter="ip.src== 192.168.0.10 and tcp.srcport==61106 and ip.dst==144.254.221.39 and tcp.dstport==443") # the same here but dst pcap name



def find_ipv4_address():  # this function helps to create a list of packet IDs and numbers
    for ele in cap:
        packet_num = ele.number
        packet_id = int(ele.ip.id, 16)
        cap_packet_num_list.append(packet_num)
        cap_packet_id_list.append(packet_id)
    for ele_2 in cap_2:
        packet_2_num = ele_2.number
        packet_id_2 = int(ele_2.ip.id, 16)
        cap_2_packet_num_list.append(packet_2_num)
        cap_2_packet_id_list.append(packet_id_2)

def find_start_time():  # with this function we determine if the time difference is 30 sec in between first packets of pcaps
    first_time_src = cap[0].sniff_time
    first_time_dst = cap_2[0].sniff_time
    if first_time_src <= first_time_dst <= first_time_src + datetime.timedelta(seconds=30) or first_time_dst <= first_time_src <= first_time_dst + datetime.timedelta(seconds=30):
        return True
    else:
        print("First packet start time differs from each other more than 30 seconds")


def find_end_time():  # with this function we determine if the time difference is 30 sec in between last packets of pcaps
    last_time_src = cap[-1].sniff_time
    last_time_dst = cap_2[-1].sniff_time
    if last_time_src <= last_time_dst <= last_time_src + datetime.timedelta(seconds=30) or last_time_dst <= last_time_src <= last_time_dst + datetime.timedelta(seconds=30):
        return True
    else:
        print("Last packet start time differs from each other more than 30 seconds")



def compare_src_to_dst_packet_id():  # this function determines if some packets that are in source pcap which are not in destination pcap
    for num in cap_packet_id_list:
        if num not in cap_2_packet_id_list:
            src_to_dst_missed_packet_id.append(num)
    # print(dst_missed_packet_id) # I will check if I can add this under this function

def compare_dst_to_src_packet_id():  # this function determines some packets that are in destination pcap are not in source pcap
    for num in cap_2_packet_id_list:
        if num not in cap_packet_id_list:
            dst_to_src_missed_packet_id.append(num)



def compare_number_size():  # this function identifies if there is packet difference in source or in destination pcaps and if yes counting how many and printing which ones they are
    if len(cap_packet_num_list) > len(cap_2_packet_num_list):
        src_to_dst_missing_num = str(len(cap_packet_num_list) - len(cap_2_packet_num_list))
        print("There are " + src_to_dst_missing_num + " missing packets in the destination pcap file")
        compare_src_to_dst_packet_id()
        print(src_to_dst_missed_packet_id)
    elif len(cap_packet_num_list) < len(cap_2_packet_num_list):
        dst_to_src_missing_number = str(len(cap_2_packet_num_list) - len(cap_packet_num_list))
        print("There are " + dst_to_src_missing_number + " missing packets in the source pcap file")
        compare_dst_to_src_packet_id()
        print(dst_to_src_missed_packet_id)
    elif len(cap_packet_num_list) == len(cap_2_packet_num_list) :
        print("There are no missed packets in between two files based on given input")




if find_start_time() and find_end_time():  # here I am putting condition before going to analyze the pcaps, if those conditions are matching, then we analyze the pcaps
    find_ipv4_address()
    compare_number_size()


# continue writing from here, add what happens if start and end time not matches within 30 seconds


