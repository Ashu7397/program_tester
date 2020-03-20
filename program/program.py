from pexpect import spawn, TIMEOUT, EOF
from time import sleep
import os
import glob


COMPILER = "gcc"
CFLAGS = "-Wall"


class Program:
    def __init__(self, src_dir):
        self.dir = src_dir
        self.prev_dir = ""
        self.program = "./test"
        self.log_file = None

    def compile(self):
        files = [file for file in glob.glob("*.[ch]")]
        output = self._execute([COMPILER, CFLAGS, *files, "-o", self.program])
        if "error" in output:
            raise RuntimeError("Failed to compile")
        if "warning" in output:
            raise RuntimeWarning("Warning")

    def _execute(self, args, inputs=None):
        self.log_file.write("Running `{}`\n".format(args))
        p = spawn(" ".join(args))
        output = ""

        if inputs is not None:
            for prompt, value in inputs:
                output += prompt
                try:
                    p.expect(prompt, timeout=3)
                except TIMEOUT:
                    raise RuntimeError(output)
                output += p.before.decode("utf-8").replace('\r', '')
                p.sendline(value)

        p.expect(EOF)
        output += p.before.decode("utf-8").replace('\r', '')
        return output

    def run(self, args, inputs):
        return self._execute([self.program, args], inputs)

    def __enter__(self):
        self.prev_dir = os.path.abspath(os.getcwd())
        os.chdir(self.dir)
        self.log_file = open("command.log", "w")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        os.chdir(self.prev_dir)
        self.log_file.close()
