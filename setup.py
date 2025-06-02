import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'lab3_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', 
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files (either .xml or .py):
        (os.path.join('share', package_name, 'launch'),
         glob('launch/*.xml') + glob('lauch/*.py'))
    ],
    scripts=['scripts/line_follow.py'],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='miti',
    maintainer_email='miti@phas.ubc.ca',
    description='ENPH 353 Lab 3 ROS',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
