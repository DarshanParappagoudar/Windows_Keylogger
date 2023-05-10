import subprocess
import logging

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def detect_keyloggers():
    """
    This function checks the system processes and services for known keylogging malware.
    """
    try:
        # Load keylogger process names from file
        with open('keylogger_processes.txt', 'r') as f:
            keylogger_processes = f.read().splitlines()

        # Check running processes for keylogger process names
        running_processes = subprocess.check_output('tasklist').decode().split('\n')
        for process in running_processes:
            if any(process.startswith(name) for name in keylogger_processes):
                logger.warning(f"{process} may be a keylogger.")

        # Load keylogger service names from file
        with open('keylogger_services.txt', 'r') as f:
            keylogger_services = f.read().splitlines()

        # Check running services for keylogger service names
        running_services = subprocess.check_output('net start').decode().split('\n')
        for service in running_services:
            if any(service.startswith(name) for name in keylogger_services):
                logger.warning(f" {service} may be a keylogger.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error executing command: {e.cmd}, return code: {e.returncode}")


if __name__ == '__main__':
    detect_keyloggers()
