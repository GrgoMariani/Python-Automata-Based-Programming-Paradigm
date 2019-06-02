import setuptools

long_description = "This is my long description"

from distutils.core import setup
setup(
  name = 'automatabpp',
  packages = ['automatabpp', 'automatabpp.commandqueue', 'automatabpp.comparisons', 'automatabpp.constants', 'automatabpp.machine', 'automatabpp.machines', 'automatabpp.metaclasses', 'automatabpp.state', 'automatabpp.xml'],
  version = '0.9.9',
  license='GPL 3',
  description = long_description,
  author = 'Grgo Mariani',
  author_email = 'grgo.mariani@protonmail.com',
  url = 'https://github.com/GrgoMariani/Python-Automata-Based-Programming-Paradigm',
  download_url = 'https://github.com/GrgoMariani/Python-Automata-Based-Programming-Paradigm/archive/v_099.tar.gz',    # I explain this later on
  keywords = ['Automata', 'Paradigm', 'Finite', 'State', 'Machine', 'yEd', 'Graph', 'Graphs', 'Behaviour'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    "Operating System :: OS Independent",
  ],
)