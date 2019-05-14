from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


setup(
    name="knowledge_base_qa",
    ext_modules=cythonize(
 [Extension("Route*", ["Route.pyx"]),],   # Extension包含了所有需要编译的py文件，这是简单示例
        build_dir="build",
        compiler_directives=dict(
            always_allow_keywords=True,
            language_level=3,   #  cythonize的语言设置成py3
        ),
    ),
    cmdclass=dict(
        build_ext=build_ext
    ),
    packages=[]
)
