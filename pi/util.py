from clr import colors
class Messages:
    def Terminal(self):
        init = "Starting Pi Terminal"
        start_transmit = "Starting Transmission"
        end_transmit = "Transmission Ended"

class Start:
    bullshit_text  = [
        "Initializing project",
        "Checking dependencies",
        "Creating directory structure",
        "Generating configuration files",
        "Installing plugins",
        "Compiling assets",
        "Verifying compatibility",
        "Running tests",
        "Starting server",
        "Authenticating user",
        "Retrieving data",
        "Analyzing data",
        "Optimizing performance",
        "Debugging code",
        "Refactoring code",
        "Implementing new features",
        "Creating user interface",
        "Implementing data access layer",
        "Writing unit tests"
    ]
    def __init__(self) -> None:
        pass

    def load_sim(start_text :str, end_text :str, size :int, speed :int, c_fill :chr, c_empty :chr):
        import time
        file_size = size # size of the file to download in MB
        download_speed = speed # download speed in MB/s
        download_time = file_size / download_speed # time to download in seconds
        progress_bar_width = 30 # width of the progress bar in characters    
        print(f"\n\n\t{colors.rst}{start_text}")
        start_time = time.time() # record the start time
        elapsed_time = 0
        while elapsed_time < download_time:
            time.sleep(1) # wait for 1 second
            elapsed_time = time.time() - start_time # calculate the elapsed time
            progress = int(elapsed_time / download_time * progress_bar_width) # calculate the progress bar width
            print("\r", f"\t{colors.Lgray}[" + f"{colors.purple}{c_fill}{colors.rst}" * progress + f"{colors.Dgray}{c_empty}{colors.Lgray}" * (progress_bar_width - progress) + "]", f"{elapsed_time:.1f}s/{download_time:.1f}s{colors.rst}", end="")
        print(f"\n\t{colors.green}{end_text}{colors.rst}")

    def init_check():
        used = []
        print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        for i in range(5):
            import random
            name_ = random.choice(Start.bullshit_text)
            name = name_ if name_ not in used else random.choice(Start.bullshit_text)
            used.append(name)
            si = random.randint(75, 150)
            sp = random.randint(10, 22)
            s = f"{name}..."
            e = f"{name} complete"
            Start.load_sim(
                s,
                e,
                si,
                sp,
                'O',
                '_'
            )
        print("\n\n|__________________________________________________________________|")
