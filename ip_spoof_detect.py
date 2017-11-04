# Network IP Filtering

import socket
import struct


def main():
	# Get host
	host = socket.gethostbyname(socket.gethostname())
	print('\n --- IP Spoof Prevention Filter ---')
	print(' Host IP: {}'.format(host))

	# Create a raw socket and bind it
	conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
	conn.bind((host, 0))

	# Include IP headers
	conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
	# Enable promiscuous mode
	conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

	white_list = ['172.17.14.211', '172.17.15.125', '172.17.14.31']
	black_list = ['172.17.14.27', '172.17.15.190', '172.17.14.91']

	while True:
		# Receive data
		raw_data, addr = conn.recvfrom(65536)
		# time.sleep(1000)

		dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)

		print('\n IP Packet Ethernet Frame ')
		print(" > Destination MAC: {}".format(dest_mac), end=' | ')
		print("Source MAC: {}".format(src_mac))
		# print("Protocol: {}".format(eth_proto))

		# print('White List: ', white_list)
		# print('Black List: ', black_list)
		ip_addr = addr[0]

		if ip_addr in black_list:
			print(" > Blocked IP Address : "+ip_addr)
		elif ip_addr in white_list:
			print(" > Permitted IP Address : "+ip_addr)
		else:
			print(" > Detected New IP Address : "+ip_addr)
			choice = int(input(" Enter (1) to add to white list or (2) for blacklist : "))
			if choice == 1:
				white_list.append(ip_addr)
			else:
				black_list.append(ip_addr)
		# print(white_list)
		# print(black_list)

# Unpack ethernet frame
def ethernet_frame(data):
	dest_mac, src_mac, proto = struct.unpack('!6s6s2s', data[:14])
	return get_mac_addr(dest_mac), get_mac_addr(src_mac), get_protocol(proto), data[14:]


# Return formatted MAC address AA:BB:CC:DD:EE:FF
def get_mac_addr(bytes_addr):
	bytes_str = map('{:02x}'.format, bytes_addr)
	mac_address = ':'.join(bytes_str).upper()
	return mac_address


# Return formatted protocol ABCD
def get_protocol(bytes_proto):
	bytes_str = map('{:02x}'.format, bytes_proto)
	protocol = ''.join(bytes_str).upper()
	return protocol


main()
