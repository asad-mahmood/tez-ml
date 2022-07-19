from setuptools import setup

setup(
    name='tez-ml',
    version='0.1.0',    
    description='A machine learning package based on scikit-learn.',
    url='https://github.com/asad-mahmood/tez-ml',
    author='Asad Mahmood',
    author_email='asad.mahmood.94@outlook.com',
    license='MIT',
    packages=['tez-ml'],
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

     classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10.5",
    ],
)