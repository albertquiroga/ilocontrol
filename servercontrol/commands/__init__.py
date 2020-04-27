from argparse import Namespace

from paramiko.client import SSHClient

client = SSHClient()
client.load_system_host_keys()


def process_command(args: Namespace):
    dispatch[args.command](args)


def _turn_server_on(args: Namespace):
    print('on')
    _connect_and_run_command(args.address, 'power on')


def _turn_server_off(args: Namespace):
    print('off')
    _connect_and_run_command(args.address, 'power off')


def _get_server_status(args: Namespace):
    print('status')
    _connect_and_run_command(args.address, 'status')


def _connect_and_run_command(address: str, command: str) -> (list, list, list):
    client.connect(address)
    stdin, stdout, stderr = client.exec_command(command)
    stdin_lines = stdin.readlines()
    stdout_lines = stdout.readlines()
    stderr_lines = stderr.readlines()
    client.close()
    return stdin_lines, stdout_lines, stderr_lines


dispatch = {
    'on': _turn_server_on,
    'off': _turn_server_off,
    'status': _get_server_status
}
