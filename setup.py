#!/usr/bin/env python
# Bootstrap setup tools
try:
    from setuptools import setup
except ImportError:
    try:
        import ez_setup
    except ImportError:
        print "Install failed: You don't have setuptools installed, and we couldn't install it for you"
    else:
        ez_setup.use_setuptools()
        from setuptools import setup

from distutils.command.install import INSTALL_SCHEMES
import os

from molly import __version__ as molly_version

from molly.installer.utils import get_packages_and_data
from molly.installer.commands import (DeployCommand, SysprepCommand,
                                CreateVirtualenvCommand, DBPrepCommand,
                                DBCreateCommand, SiteCreateCommand)

print """
                                 ;Ok;                                         
                                 lMM:                                         
                                .0MX.                                         
                                ;WMx                                          
                 .xx,           dMW;                                          
                 .oWWd.        .XM0.                                          
                   ,0M0,       ;MMo          .;xKx.                           
                    .oWWl      oMN'       .,dXMNx;.                           
                      ,0Wx.    ,dc.    .;dXMNk:.                              
   ;KX0d:.             .d0:           .XMNk:.                                 
   ;OXMMMK;  ..',..                   .;;.              ...   ...             
     .,0MMNx0NMMMMN0l.  .;ok000xc.                     dWWk. :NMK'            
       .KMMMMXkddONMMXllKMMWXKNMMNo.    .:ooc:;'..     xMMW, cMMMl            
      ;KMMMMd.    .OMMMMMXo'. .oMMMd.   .oOKXWMMMK.   .OMMN. lMMMc            
    .xWMMWMMx      :WMMMd.     .kMMW;       ...,;.    ;WMMx .KMMX.            
   .KMMWlkMM0    .lWMMMMc       :MMMd                .kMMW, :MMMo             
  .OMMX; dMM0    lMMMMMMd       ,MMMx     'ldkxo:.   ,WMMx  kMMX..cl'    .cl' 
 .xMMN,  xMM0   ;WMMkNMMd       ;MMMd    lWMMMMMMK,  dMMW, 'WMMl xMM0.   dMMO 
 :WMW:  .0MMx  'XMMx,WMMo       oMMMc 'oxWMMK,;XMMK..KMMk. dMMX..NMMo   .OMMk 
;0MMx   ,WMMc  xMMK.cMMM:      .KMMX. OMMMMMMWKKMMW';MMM: .KMMd :MMM,   :WMMx 
dMMM;  .kMM0. 'WMMc.0MMN.      :MMMo .NMMd:dkOOWMMK.dMMK. :MMM; oMMN.  ,XMMMo 
xMMW, .dMMW,  :MMW'oMMMo      .KMM0. .XMMk.  .xMMW: OMMx  oMMX. lMMN..:NMMMM: 
cXMMOl0MMWc   ;MMM0WMWd.     .0MMX'   oMMMOodKMMX:..0MMx  dMMX. 'NMM0KMMMMMW' 
 'OMMMMWO,    .oNMMM0:.      cWM0'    .cKWMMMMKl.   lWMx  ,XMX.  'OWMMXxXMMO. 
  .'::;.        .,,..         ...       ..,;,..      ...   ... .':lkK0kkWMM:  
                                                            .,xXMMMMMWMMMMM0, 
                                                           .dWMMKdc,.:XMMWMMNo
                                                           cMMWc.  .xWMMK;xXOc
                                                           cMMWkoxOWMMKl.     
                                                           .oNMMMMWKd,.       
                                                             :dOOxl           

Welcome to the Molly Installer!

http://mollyproject.org/
"""

# Tell distutils to put the data_files in platform-specific installation
# locations. See here for an explanation:
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

packages, data_files = get_packages_and_data(os.path.dirname(__file__))

setup(
    name = 'molly',
    version = molly_version,
    url = 'http://mollyproject.org/',
    author = 'The Molly Project',
    description ="A framework for building mobile information portals",
    packages = packages,
    data_files = data_files, 
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Academic Free License (AFL)',
        'Intended Audience :: Education',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Education',
        'Topic :: Internet',
    ],
    setup_requires = ["setuptools"],
    install_requires = [
        "python-Levenshtein",
        "pywurfl",
        "feedparser>=5.0",
        "simplejson",
        "rdflib",
        "python-dateutil==1.5",
        "Django==1.3",
        "oauth==1.0.1",
        "psycopg2",
        "PIL",
        "lxml",
        "python-ldap",
        "django-compress",
        "python-memcached",
        "South",
        "suds",
        "django-slimmer",
        'pyyaml',
    ],
    cmdclass = {
        'sysprep': SysprepCommand,
        'dbprep': DBPrepCommand,
        'dbcreate': DBCreateCommand,
        'sitecreate': SiteCreateCommand,
        'createvirtualenv': CreateVirtualenvCommand,
        'deploy': DeployCommand,
    }
)
