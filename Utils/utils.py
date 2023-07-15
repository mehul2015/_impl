import time
from colorama import Fore,Style

class Pair:
    def __init__(self,node, count : int) -> None:
        self.node = node
        self.count = count


def print_elapsed_time(start_time: float) -> None:
        elapsed_time = time.time() - start_time
        formatted_time = "{:.10f}".format(elapsed_time)
        print(Fore.GREEN + f"{formatted_time} seconds" + Style.RESET_ALL)