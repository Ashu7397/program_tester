from pexpect import spawn, TIMEOUT, EOF
import os
import glob


COMPILER = "gcc"
CFLAGS = "-Wall"

TEMPLATE_WARNING = 'printf(is_stripped ? result_string : "Cannot find the pattern in the string'

class Program:
    def __init__(self, src_dir):
        self.dir = src_dir
        self.prev_dir = ""
        self.program = "./test"
        self.log_file = None

    def compile(self):
        files = [file for file in glob.glob("*.[ch]")]
        output = self._execute([COMPILER, CFLAGS, *files, "-o", self.program])
        # print("Output of Compile:", output)
        self.log_file.write("Failed To Compile With error: {}\n".format(output))
        if "error" in output:
            raise RuntimeError("Failed to compile")
        if "warning" in output:
            if TEMPLATE_WARNING not in output:
                raise RuntimeWarning("Warning")

    def _execute(self, args, inputs=None):
        self.log_file.write("Running `{}`\n".format(args))
        p = spawn(" ".join(args))
        output = ""

        if inputs is not None:
            for input in inputs:
                for prompt, value in [input]:
                    output += prompt
                    try:
                        p.expect(prompt, timeout=1)
                    except (TIMEOUT, EOF):
                        raise RuntimeError(output)
                    output += p.before.decode("utf-8").replace('\r', '')
                    p.sendline(value)

        try:
            p.expect(EOF)
        except TIMEOUT:
            raise RuntimeError(output)
        try:
            output += p.before.decode("utf-8").replace('\r', '')
        except UnicodeDecodeError:
            print("Cannot decode the text.. Possibly non English chars", end="")
        return output

    def run(self, args, inputs):
        return self._execute([self.program, args], inputs)

    def __enter__(self):
        self.prev_dir = os.path.abspath(os.getcwd())
        try:
            os.chdir(self.dir)
        except FileNotFoundError:
            raise RuntimeError("Could not find {}".format(self.dir))
        self.log_file = open("../test.log", "a")
        self.log_file.write("{}\n".format(self.dir.split("/")[-1]))
        self.log_file.write("#"*40+"\n")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        os.chdir(self.prev_dir)
        self.log_file.close()
