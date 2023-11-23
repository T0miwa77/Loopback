from netmiko import ConnectHandler 

router_ip = "192.168.56.101"
router_username = "cisco"
router_password = "cisco123!"

router = {
    "device_type": "cisco_ios",
    "ip": router_ip,
    "username": router_username,
    "password": router_password,
}

router_conn = ConnectHandler(**router)
router_conn.enable()

router_conn.send_config_set(["interface loopback0", "ip address 10.0.0.1 255.255.255.0"])

router_conn.send_config_set(["interface GigabitEthernet0/0", "ip address 192.169.1.1 255.255.255.0"])

router_conn.send_config_set(["router ospf 1", "network 10.0.0.0 0.0.0.255 area 0"])

router_conn.send_config_set(["hostname cisco", "enable secret cisco123!"])

router_conn.send_command("write memory")

import paramiko

computer_ip = "192.168.56.30"
computer_username = "user"
computer_password = "password"
router_loopback_ip = "10.0.0.1"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(computer_ip, username=computer_username, password=computer_password)

ssh.exec_commnand("route add 192,168.1.0 mask 255.255.255.0 192.168.56.101")

ping_command = f"ping {router_loopback_ip}"
stdin, stdout, stderr = ssh.exec_command(ping_command)

print(stdout.read().decode)

ssh.close()

