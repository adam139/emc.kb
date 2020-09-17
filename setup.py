from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='emc.kb',
      version=version,
      description="a knowleage base for EMC project",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='python plone',
      author='Adam tang',
      author_email='yuejun.tang@gmail.com',
      url='https://github.com/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['emc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
#           'cx_Oracle == 5.2.1',
          'cx_Oracle ',
          'SQLAlchemy',
          'collective.autopermission',
          'plone.app.dexterity',
          'plone.namedfile [blobs]',
          'plone.app.registry',
          'plone.app.z3cform',
          'plone.app.relationfield',
          'z3c.caching',
          'zope.annotation',
#           'z3c.saconfig',
          # -*- Extra requirements: -*-
      ],
       extras_require={
          'test': ['plone.app.testing',]
      },
      entry_points="""
      # -*- Entry points: -*-
        [console_scripts]
        initdb = emc.kb.initdb:main
      [z3c.autoinclude.plugin]
      target = plone
      """,

      )
