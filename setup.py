from setuptools import setup,find_packages

#from my_pip_package import __version__

setup(
    name='EPiCA',
    version='0.0.2',
    description='Exoplanetary Pierre Connes Algorithm (EPiCA). Algorithm for RV calculation.',
    url='https://github.com/aeictf/EPiCA',
    author='Anastasiia Ivanova',
    author_email='anastasia.ivanova@latmos.ipsl.fr',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research ',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    keywords='radial velocity rv exoplanet pipeline',
    packages=['EPiCA'],
    install_requires=[
        'numpy', 'astropy'],#, 'pandas', 'matplotlib'


    zip_safe=False

)
