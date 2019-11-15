from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy



pcl_include_dir = "E:/Prosjekter/lib/vcpkg/installed/x64-windows/include/pcl"
pcl_lib_dir = "E:/Prosjekter/lib/vcpkg/installed/x64-windows/lib"
include_dir = "E:/Prosjekter/lib/vcpkg/installed/x64-windows/include"

ext_modules = [Extension(
       "semantic3D",
       sources=["Semantic3D.pyx", "Sem3D.cxx",],  # source file(s)
       include_dirs=["./", numpy.get_include(),pcl_include_dir, include_dir],
       language="c++",
       library_dirs=[pcl_lib_dir],
       libraries=["pcl_common_release","pcl_kdtree_release","pcl_features_release","pcl_surface_release","pcl_io_release"],         
       extra_compile_args = [ "/std:c++14", "/openmp",],
       extra_link_args=["/std:c++14", '/openmp'],
  )]

setup(
    name = "Semantic3D_utils",
    ext_modules = ext_modules,
    cmdclass = {'build_ext': build_ext},
)
