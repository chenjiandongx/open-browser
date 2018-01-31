import argparse
import webbrowser

__version__ = "0.0.1"


def get_parser():
    """ 解析命令行参数

    :return:
    """
    parser = argparse.ArgumentParser(
        description='Open url with your browser.')
    parser.add_argument('url', metavar='Url', type=str, nargs='*',
                        help='the open url')
    parser.add_argument('-v', '--version', action='store_true',
                        help='displays the current version of open')
    return parser


def command_line_runner():
    """ 执行命令行操作

    :return:
    """
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print(__version__)
        return

    if not args['query']:
        parser.print_help()
        return

    webbrowser.open(args['query'])


if __name__ == "__main__":
    command_line_runner()
