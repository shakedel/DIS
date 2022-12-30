from setuptools import setup


setup(
    name='DIS',
    version='0.0.1',
    description='',
    # packages=find_packages(),
    package_dir = {
        'is_net': 'IS-Net',
        'is_net.models': 'IS-Net/models'
    },
    install_requires=[
        'torch',
        'torchvision',
        'matplotlib',
        'numpy',
        'Pillow',
        'scikit-image',
        'tqdm',
        'opencv-python',
    ],
)
