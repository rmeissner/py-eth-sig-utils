import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

reqs = 'requirements.txt'
dev_reqs = 'requirements-dev.txt'

install_requires = []
extras_require = {
    'dev': []
}

with open(reqs) as f:
    for line in f.read().splitlines():
        line = line.strip()
        if not line.startswith('#'):
            parts = line.strip().split(';')
            if len(parts) > 1:
                print('Warning: requirements line "{}" ignored, as it uses env markers, which are not supported in setuptools'.format(line))
            else:
                install_requires.append(parts)

if os.path.exists(dev_reqs):
    with open(dev_reqs) as f:
        for line in f.read().splitlines():
            extras_require['dev'].append(line.strip())

setuptools.setup(
    name="py_eth_sig_utils",
    version="0.4.0",
    license='MIT License',
    author="Richard Meissner",
    author_email="msc.meissner@gmail.com",
    description="Python Ethereum Signing Utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rmeissner/py-eth-sig-utils",
    packages=setuptools.find_packages(),
    platforms='Any',
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
