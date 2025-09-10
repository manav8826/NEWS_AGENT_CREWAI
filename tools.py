from dotenv import load_dotenv
load_dotenv()

import os

os.environ['SERPER_API_KEY'] =os.getenv('SERPER_API_KEY')

from crewai_tools.tools.serper import SerperDevTool

# intilaise the tool for internet searching capapbilites 
tool=SerperDevTool()