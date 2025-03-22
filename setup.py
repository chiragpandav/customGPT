from setuptools import setup

setup(name='customGPT',
      version='0.0.1',
      author='Chirag Pandav',
      packages=['mingpt'],
      description='A PyTorch re-implementation of GPT',
      license='MIT',
      install_requires=[
            'torch',
      ],
)
