from conans import ConanFile, CMake

class TopoculeConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "boost/1.73.0", "gmp/6.2.1", "mpfr/4.1.0", "eigen/3.3.9", "cgal/5.2.1"
    generators = "cmake"
    # Shared libs in conan are poorly maintained regarding the rpath, though.
    default_options = {"openssl:shared": True}

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin") # From bin to bin
        self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin
        #self.copy("*.a", dst="bin", src="bin") # From bin to bin

    def build(self):
        # FIXME don't use auto-generation of conan
        cmake = CMake(self)
        cmake.configure()
        cmake.build()