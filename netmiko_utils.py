from netmiko import ConnectHandler

def get_live_config(ip, username, password):
    device = {
        "device_type": "cisco_nxos",
        "ip": ip,
        "username": username,
        "password": password,
    }
    try:
        conn = ConnectHandler(**device)
        config = conn.send_command("show running-config")
        conn.disconnect()
        return config
    except Exception as e:
        return f"Error connecting: {e}"
