import os
import subprocess

# Define the service name and service file path
service_name = 'smartnodecontrol.service'
service_file_path = f'/etc/systemd/system/{service_name}'

# Get the directory of the current script
current_script_dir = os.path.dirname(os.path.realpath(__file__))

# Define the service content
service_content = f"""[Unit]
Description=Smart Node Control Service

[Service]
ExecStart=/usr/bin/python3 {os.path.join(current_script_dir, 'smartnoderestart.py')}
Restart=always
User={os.getlogin()}
WorkingDirectory={current_script_dir}
StandardOutput=inherit
StandardError=inherit

[Install]
WantedBy=multi-user.target
"""

# Check if the service file already exists
if not os.path.exists(service_file_path):
    # Create the service file
    with open(service_file_path, 'w') as service_file:
        service_file.write(service_content)
    print(f"Service file {service_name} created.")

    # Reload the systemd manager configuration
    subprocess.run(['sudo', 'systemctl', 'daemon-reload'], check=True)

    # Enable the service to start on boot
    subprocess.run(['sudo', 'systemctl', 'enable', service_name], check=True)

    # Start the service
    subprocess.run(['sudo', 'systemctl', 'start', service_name], check=True)
    print(f"Service {service_name} started and enabled on boot.")
else:
    # Start the service if it already exists
    subprocess.run(['sudo', 'systemctl', 'start', service_name], check=True)
    print(f"Service {service_name} already exists and has been started.")
