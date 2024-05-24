import subprocess
import time
import logging
import os

### Change this
process_path = '/root/rtm_lastest/raptoreumd'  # Path to RTM CORE raptoreumd
check_interval = 60  # Interval, how often to check whether raptoreumd is running (in seconds)
### Change this End

process_name = 'raptoreumd'
log_file = os.path.join(os.path.expanduser('~'), 'smartnodecontrol.log')  # Log file in the user's home directory

logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(message)s')

def is_process_running(process_name):
    try:
        output = subprocess.check_output(['pgrep', '-f', process_name])
        if output:
            return True
    except subprocess.CalledProcessError:
        return False
    except Exception as e:
        logging.error(f"Error checking if process {process_name} is running: {e}")
        return False

def start_process(process_path):
    try:
        subprocess.Popen([process_path])
        logging.info(f"{process_name} process started successfully.")
    except Exception as e:
        logging.error(f"Error starting process {process_name} with path {process_path}: {e}")
        print(f"Error starting process {process_name}: {e}")

def main():
    if not os.path.isfile(process_path):
        logging.error(f"The specified process path does not exist: {process_path}")
        print(f"The specified process path does not exist: {process_path}")
        return
    
    if not os.access(process_path, os.X_OK):
        logging.error(f"The specified process path is not executable: {process_path}")
        print(f"The specified process path is not executable: {process_path}")
        return
    
    while True:
        try:
            if not is_process_running(process_name):
                start_process(process_path)
                logging.info(f"{process_name} process had to be started because it was not listed in the process list.")
                print(f"Service {process_name} was started")
            else:
                logging.info(f"{process_name} is already running.")
            time.sleep(check_interval)
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            print(f"Error in main loop: {e}")
            time.sleep(check_interval)

if __name__ == "__main__":
    logging.info(f"Start Script")
    main()
