import ipaddress
import sys

ip = "00.000.000.00"

try:
    ipaddress.IPv4Address(ip)
except Exception as e:
    print(f'error')

ip_i = [int(i) for i in ip.split('.')]
mask_i = [int(i) for i in ip.split('.')]
network_i = [ip_i[i] & mask_i[i] for i in range(4)]
host_i = [ip_i[i] &~ mask_i[i] for i in range(4)]

print(ip_i)
print(mask_i)
print(network_i)
print(host_i)

ip_b = "{0:08b}.{1:08b}.{2:08b}.{3:08b}".format(*ip_i)

print(ip_b)

def cidr_to_subnet_mask(cidr):
    # binary subnet mask
    binary_mask = '1' * cidr + '0' * (32 - cidr)
    # 8-bit
    subnet_mask = '.'.join(str(int(binary_mask[i:i+8], 2)) for i in range(0, 32, 8))
    return subnet_mask

# IP Adresi: 00.000.000.00

# CIDR /8
cidr1 = 8
subnet_mask1 = cidr_to_subnet_mask(cidr1)
print(f"CIDR /8 Subnet Mask: {subnet_mask1}")

# CIDR /16
cidr2 = 16
subnet_mask2 = cidr_to_subnet_mask(cidr2)
print(f"CIDR /16 Subnet Mask: {subnet_mask2}")