import ipaddress
import math

def next_power_of_two(x):
    """Return the nearest power of 2 greater than or equal to x."""
    return 1 if x == 0 else 2**(math.ceil(math.log2(x)))

def calculate_subnets(network, host_requirements):
    host_requirements = sorted(host_requirements, reverse=True)
    
    subnets = []
    base_network = ipaddress.ip_network(network, strict=False)
    available_subnets = [base_network]
    
    for hosts in host_requirements:
        needed_hosts = hosts + 2
        subnet_size = next_power_of_two(needed_hosts)
        prefix = 32 - int(math.log2(subnet_size))
        
        allocated = None
        for i, candidate in enumerate(available_subnets):
            if candidate.prefixlen <= prefix:
                allocated = list(candidate.subnets(new_prefix=prefix))[0]
     #REM
                available_subnets.pop(i)
                available_subnets.extend(candidate.subnets(new_prefix=prefix))
                available_subnets.remove(allocated)
                break
        
        if allocated:
            subnets.append((hosts, allocated))
        else:
            print(f" Not enough space for {hosts} hosts.")
            return []
    
    return subnets

def main():
    network = input("Enter the base network (e.g. 192.168.1.0/24): ")
    num_subnets = int(input("Enter number of subnets: "))
    
    host_requirements = []
    for i in range(num_subnets):
        hosts = int(input(f"Enter number of hosts for subnet {i+1}: "))
        host_requirements.append(hosts)
    
    results = calculate_subnets(network, host_requirements)
    
    print("\n--- Subnetting Results ---")
    for i, (hosts, subnet) in enumerate(results, start=1):
        net = ipaddress.ip_network(subnet)
        print(f"\nSubnet {i}:")
        print(f"  Required hosts : {hosts}")
        print(f"  Allocated subnet: {net}")
        print(f"  Network address: {net.network_address}")
        print(f"  Broadcast addr : {net.broadcast_address}")
        print(f"  Usable hosts   : {list(net.hosts())[0]} - {list(net.hosts())[-1]}")
        print(f"  Subnet mask    : {net.netmask}")
        print(f"  Prefix length  : /{net.prefixlen}")

if __name__ == "__main__":
    main()
