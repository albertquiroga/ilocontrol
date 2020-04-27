from servercontrol.commands import process_command

from albertquiroga_utils.cli.CLITool import CLITool


class ServerControlCLI(CLITool):

    def __init__(self):
        super(ServerControlCLI, self).__init__(name='server',
                                               description='Small Python CLI utilities to manage HP iLO servers',
                                               config_section='ServerControl',
                                               key_parameters={'server': ['address']},
                                               subparsers=False)

        # Connect command
        self.parser.add_argument('command', type=str, help='Command to execute',
                                 choices=['on', 'off', 'status'])
        self.parser.add_argument('address', type=str, help='IP address of the server')
        self.parser.add_argument('-u', '--user', type=str, help='Username to authenticate')
        self.parser.add_argument('-k', '--key', type=str, help='Path to the private key file to authenticate')
        self.parser.set_defaults(func=process_command)
