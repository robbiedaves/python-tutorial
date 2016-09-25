from Functions import Functions
from IfsAndLoops import IfsAndLoops
from Lists import Lists
from Numbers import Numbers
from Strings import Strings


class TutorialMain:

    def run(self):
        Numbers().numbers_demo()
        Strings().strings_demo()
        Lists().lists_demo()
        IfsAndLoops().ifs_and_loops_demo()
        Functions().functions_demo()

TutorialMain().run()
