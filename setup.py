from setuptools import setup, Extension
from Cython.Build import cythonize


setup(
    name="Stretch",
    ext_modules=cythonize(
        Extension(
            name="Stretch",
            sources=["Stretch.pyx"],
            language=["c++"],
            extra_compile_args=["-std=c++17"],
        ),
        compiler_directives={
            'embedsignature': True,
            'language_level': 3,
        },
    ),
    version="0.0.1",
)
