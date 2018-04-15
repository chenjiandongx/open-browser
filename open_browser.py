import argparse
import webbrowser

__version__ = "0.1.0"

CHROME_PATH = r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


def get_parser():
    """
    解析命令行参数
    """
    parser = argparse.ArgumentParser(description="Open url with your browser.")
    parser.add_argument(
        "url",
        metavar="URL",
        type=str,
        help="the url you want to open with browser",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="displays the current version of `open`",
    )
    return parser


def command_line_runner():
    """
    执行命令行操作
    """
    parser = get_parser()
    args = vars(parser.parse_args())

    if args["version"]:
        print(__version__)
        return

    if not args["url"]:
        parser.print_help()
        return

    webbrowser.get(CHROME_PATH).open(args["url"])


if __name__ == "__main__":
    command_line_runner()
